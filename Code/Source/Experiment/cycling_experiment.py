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

        with open(log_path, "w", newline="", encoding="utf-8-sig") as file:
            writer = csv.writer(file, delimiter=";")

            writer.writerow(
                [
                    "Time [s]",
                    "Potential [V]",
                    "Current [A]",
                    "Temperature [°C]",
                    "Temperature line from Arduino",
                    "Device status",
                    "Cell status",
                    "Status parameter",
                    "Stop reason",
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

                row_stop_reason = ""

                if in_startup_grace:
                    print("Startup grace period active. Safety checks skipped.")

                else:
                    if method_was_running and device_status != 2:
                        row_stop_reason = "Aborted manually in IviumSoft."
                        print("Ivium method no longer running.")

                    elif method_was_running and cell_status == 0:
                        row_stop_reason = "Ivium cell off."
                        print("Ivium cell is off.")

                    elif voltage > settings.max_safe_voltage_v:
                        row_stop_reason = "Maximum voltage safety limit reached."
                        print("Maximum voltage safety limit reached.")
                        print(f"Measured voltage was {voltage:.4f} V")

                    elif voltage < settings.min_safe_voltage_v:
                        row_stop_reason = "Minimun voltage safety limit reached."
                        print("Minimum voltage safety limit reached.")
                        print(f"Measured voltage was {voltage:.4f} V")

                    elif abs(current) > settings.max_safe_current_a:
                        row_stop_reason = "Current safety limit reached."
                        print("Current safety limit reached.")
                        print(f"Measured current was {current:.6f} A")

                    elif (
                        settings.max_temperature_c is not None
                        and temperature_c is not None
                        and temperature_c >= settings.max_temperature_c
                    ):
                        row_stop_reason = "Temperature safety limit reached."
                        print("Temperature safety limit reached.")
                        print(f"Measured temperature was {temperature_c:.2f} °C")

                if row_stop_reason == "" and elapsed >= settings.max_runtime_s:
                    row_stop_reason = "time_limit"
                    print("Time limit reached.")

                if row_stop_reason != "":
                    stop_reason = row_stop_reason

                writer.writerow(
                    [
                        f"{elapsed:.3f}",
                        f"{voltage:.6f}",
                        f"{current:.9f}",
                        "" if temperature_c is None else f"{temperature_c:.2f}",
                        temperature_line,
                        device_status,
                        cell_status,
                        status_parameter,
                        row_stop_reason,
                    ]
                )
                file.flush()

                if row_stop_reason != "":
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