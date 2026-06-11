import csv
import time
from dataclasses import dataclass
from pathlib import Path

from Source.Devices.ivium_driver import IviumDriver, create_cycle_imf, DLL_PATH
from Source.Devices.tempmoni import TemperatureMonitor


@dataclass
class ExperimentSettings:
    charge_current_uA: float
    discharge_current_uA: float
    upper_voltage_v: float
    lower_voltage_v: float

    max_runtime_s: float = 30.0
    startup_grace_s: float = 3.0

    max_safe_voltage_v: float = 4.25
    min_safe_voltage_v: float = 2.80
    max_safe_current_a: float = 0.0005

    temperature_port: str = "COM7"
    temperature_baud: int = 115200
    max_temperature_c: float | None = None

    log_name: str = "experiment_log.csv"


def run_battery_experiment(
    settings: ExperimentSettings,
    template_method_path: str,
    generated_method_path: str,
    log_path: str,
) -> None:
    template_method_path = str(Path(template_method_path).resolve())
    generated_method_path = str(Path(generated_method_path).resolve())
    log_path = Path(log_path).resolve()
    log_path.parent.mkdir(parents=True, exist_ok=True)

    print("Creating Ivium method file...")

    method_path = create_cycle_imf(
        template_path=template_method_path,
        output_path=generated_method_path,
        charge_current_uA=settings.charge_current_uA,
        discharge_current_uA=settings.discharge_current_uA,
        upper_voltage_v=settings.upper_voltage_v,
        lower_voltage_v=settings.lower_voltage_v,
    )

    print("Method file:", method_path)
    print("CSV log file:", log_path)

    print("Opening temperature monitor...")
    temperature_monitor = TemperatureMonitor(
        port=settings.temperature_port,
        baud=settings.temperature_baud,
        timeout_s=0.5,
        email_enabled=False,
    )
    temperature_monitor.open()
    print(f"Temperature monitor opened on {settings.temperature_port}")

    ivium = IviumDriver(DLL_PATH)

    stop_reason = "unknown"

    try:
        result = ivium.open()
        print("Open:", result)

        if result != 0:
            stop_reason = "ivium_open_failed"
            raise RuntimeError("IV_open failed. Make sure IviumSoft is open and connected.")

        print("Connecting...")
        connect_result = ivium.connect()
        print("Connect:", connect_result)

        print("Starting Ivium method...")
        start_result = ivium.start_method(method_path)
        print("Start method:", start_result)

        if start_result != 0:
            stop_reason = "ivium_startmethod_failed"
            raise RuntimeError("IV_startmethod failed. Check the .imf file and IviumSoft status.")

        start_time = time.time()
        method_was_running = False

        with open(log_path, "w", newline="") as file:
            writer = csv.writer(file)

            writer.writerow(
                [
                    "time_s",
                    "potential_V",
                    "current_A",
                    "temperature_C",
                    "temperature_line",
                    "device_status",
                    "cell_status",
                    "status_parameter",
                    "stop_reason",
                ]
            )
            file.flush()

            while True:
                elapsed = time.time() - start_time
                in_startup_grace = elapsed < settings.startup_grace_s

                voltage = ivium.get_potential()
                current = ivium.get_current()

                temperature_c, temperature_line = temperature_monitor.read_temperature()

                device_status = ivium.get_device_status()
                cell_status = ivium.get_cell_status()
                status_parameter = ivium.get_status_parameter()

                if device_status == 2:
                    method_was_running = True

                temp_text = "None" if temperature_c is None else f"{temperature_c:.2f}"

                print(
                    f"t={elapsed:6.1f} s | "
                    f"E={voltage: .4f} V | "
                    f"I={current: .6f} A | "
                    f"T={temp_text} C | "
                    f"dev={device_status} | "
                    f"cell={cell_status} | "
                    f"stat={status_parameter}"
                )

                writer.writerow(
                    [
                        elapsed,
                        voltage,
                        current,
                        temperature_c,
                        temperature_line,
                        device_status,
                        cell_status,
                        status_parameter,
                        "",
                    ]
                )
                file.flush()

                if in_startup_grace:
                    print("Startup grace period active. Safety checks skipped.")

                else:
                    if method_was_running and device_status != 2:
                        stop_reason = "ivium_method_completed_or_aborted"
                        print("Ivium method no longer running.")
                        break

                    if method_was_running and cell_status == 0:
                        stop_reason = "ivium_cell_off"
                        print("Ivium cell is off.")
                        break

                    if voltage > settings.max_safe_voltage_v:
                        stop_reason = "max_voltage_safety_limit"
                        print("Maximum voltage safety limit reached.")
                        print(f"Measured voltage was {voltage:.4f} V")
                        break

                    if voltage < settings.min_safe_voltage_v:
                        stop_reason = "min_voltage_safety_limit"
                        print("Minimum voltage safety limit reached.")
                        print(f"Measured voltage was {voltage:.4f} V")
                        break

                    if abs(current) > settings.max_safe_current_a:
                        stop_reason = "current_safety_limit"
                        print("Current safety limit reached.")
                        print(f"Measured current was {current:.6f} A")
                        break

                    if (
                        settings.max_temperature_c is not None
                        and temperature_c is not None
                        and temperature_c >= settings.max_temperature_c
                    ):
                        stop_reason = "temperature_safety_limit"
                        print("Temperature safety limit reached.")
                        print(f"Measured temperature was {temperature_c:.2f} °C")
                        break

                if elapsed >= settings.max_runtime_s:
                    stop_reason = "time_limit"
                    print("Time limit reached.")
                    break

                time.sleep(1)

    finally:
        print("Stopping experiment...")
        print("Stop reason:", stop_reason)

        try:
            print("Abort:", ivium.abort())
        except Exception as e:
            print(f"Abort failed: {e}")

        try:
            print("Cell off:", ivium.set_cell_on(False))
        except Exception as e:
            print(f"Cell off failed: {e}")

        try:
            print("Connection mode off:", ivium.set_connection_mode(False))
        except Exception as e:
            print(f"Connection mode off failed: {e}")

        try:
            print("Close:", ivium.close())
        except Exception as e:
            print(f"Ivium close failed: {e}")

        try:
            temperature_monitor.close()
            print("Temperature monitor closed.")
        except Exception as e:
            print(f"Temperature monitor close failed: {e}")

        print(f"Data saved to: {log_path}")