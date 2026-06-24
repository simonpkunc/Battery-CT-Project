import csv
import time
import msvcrt
from dataclasses import dataclass
from pathlib import Path
from Source.Logging.status_logger import ExperimentStatusLogger

from Source.Devices.ivium_driver import (
    IviumDriver,
    create_cycle_imf,
    DLL_PATH,
    IviumCycleTask,
)
from Source.Devices.tempmoni import TemperatureMonitor
from Source.Devices.tekscan_driver import TekscanDriver

@dataclass
class ExperimentSettings:
    tasks: list[IviumCycleTask]
    number_of_cycles: int

    startup_grace_s: float = 3.0
    hard_timeout_s: float = 24 * 60 * 60

    max_safe_voltage_v: float = 4.25
    min_safe_voltage_v: float = 2.80
    max_safe_current_a: float = 0.15

    temperature_port: str = "COM7"
    temperature_baud: int = 115200
    max_temperature_c: float | None = None

    use_tekscan: bool = False

    log_name: str = "experiment_log.csv"

def terminal_escape_pressed() -> bool:
    """
    Returns True if Esc has been pressed in the terminal.

    This works on Windows terminals. The terminal must have focus.
    """
    if not msvcrt.kbhit():
        return False

    key = msvcrt.getwch()

    return key == "\x1b"

def run_battery_experiment(
    settings: ExperimentSettings,
    template_method_path: str,
    generated_method_path: str,
    log_path: str,
    status_path: str,
) -> None:
    template_method_path = str(Path(template_method_path).resolve())
    generated_method_path = str(Path(generated_method_path).resolve())
    log_path = Path(log_path).resolve()
    log_path.parent.mkdir(parents=True, exist_ok=True)

    status_path = Path(status_path).resolve()
    terminal_log_path = log_path.with_name(log_path.stem + "_terminal_log.txt")

    status_logger = ExperimentStatusLogger(status_path)

    status_logger.write_status(
        force = True,
        state = "Starting experiment",
        csv_log = log_path,
        terminal_log = terminal_log_path,
        requested_tasks = len(settings.tasks),
        requested_cycles = settings.number_of_cycles,
        tekscan_enabled = settings.use_tekscan,
        stop_reason = "",
    )

    if len(settings.tasks) < 1:
        raise ValueError("At least one task is required.")

    if settings.number_of_cycles < 1:
        raise ValueError("Number of cycles must be at least 1.")

    print("Creating Ivium method file...")

    method_path = create_cycle_imf(
        template_path=template_method_path,
        output_path=generated_method_path,
        tasks=settings.tasks,
        number_of_cycles=settings.number_of_cycles,
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

    tekscan = None
    tekscan_recording_started = False

    if settings.use_tekscan:
        tekscan = TekscanDriver()
        print("Tekscan recording is enabled.")
        print("I-Scan must already have an active New Recording window open.")

    stop_reason = "Unknown."
    ivium_shutdown_sent = False

    def stop_tekscan_recording_if_needed(force: bool = False) -> None:
        nonlocal tekscan_recording_started

        if tekscan is None:
            return

        if not tekscan_recording_started and not force:
            return

        try:
            if force and not tekscan_recording_started:
                print("Forcing Tekscan stop command even though internal flag is off.")

            print("Stopping Tekscan recording...")
            tekscan.stop_recording()
            print("Tekscan recording stop command sent.")

        except Exception as e:
            print(f"Tekscan stop failed: {e}")

        finally:
            tekscan_recording_started = False

    def shutdown_ivium_output_if_needed() -> None:
        nonlocal ivium_shutdown_sent

        if ivium_shutdown_sent:
            return

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

        ivium_shutdown_sent = True

    try:
        result = ivium.open()
        print("Open:", result)

        if result != 0:
            stop_reason = "Failed to open Ivium."
            raise RuntimeError("Failed to open Ivium. Make sure IviumSoft is open and connected.")

        print("Connecting...")
        connect_result = ivium.connect()
        print("Connect:", connect_result)

        print()
        print("Initial Ivium reading")
        print("=====================")

        initial_voltage = None
        initial_current = None
        initial_voltage_ok = False

        for attempt in range(1, 11):
            initial_voltage = ivium.get_potential()
            initial_current = ivium.get_current()

            print(
                f"Attempt {attempt}/10: "
                f"E={initial_voltage:.6f} V | "
                f"I={initial_current:.9f} A"
            )

            if settings.min_safe_voltage_v <= initial_voltage <= settings.max_safe_voltage_v:
                initial_voltage_ok = True
                break

            time.sleep(0.5)

        print()

        if not initial_voltage_ok:
            print("WARNING: Initial Ivium voltage is outside the safe voltage range.")
            print(f"Measured initial voltage: {initial_voltage:.6f} V")
            print(f"Allowed range: {settings.min_safe_voltage_v:.3f} V to {settings.max_safe_voltage_v:.3f} V")
            print()
            print("This can happen if Ivium gives a false first reading.")
            print("Before continuing, check that IviumSoft shows approximately the same voltage as the multimeter.")
            print()

            user_input = input("Continue anyway? [y/N]: ").strip().lower()

            if user_input not in ("y", "yes", "j", "ja"):
                stop_reason = "Initial voltage outside safe range."
                raise RuntimeError("Experiment cancelled because initial Ivium voltage was outside the safe range.")

        print("Initial voltage check completed.")
        print()

        if settings.use_tekscan and tekscan is not None:
            print("Starting Tekscan recording...")
            tekscan.start_recording()
            tekscan_recording_started = True
            print("Tekscan recording start command sent.")

        print("Starting Ivium method...")
        start_result = ivium.start_method(method_path)
        print("Start method:", start_result)

        if start_result != 0:
            stop_reason = "Ivium startmethod failed."
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
                    "Device status",
                    "Cell status",
                    "Status parameter",
                    "Requested tasks",
                    "Requested cycles",
                    "Tekscan recording",
                    "Stop reason",
                ]
            )
            file.flush()

            latest_elapsed_s = None
            latest_voltage_v = None
            latest_current_a = None
            latest_temperature_c = None
            latest_device_status = None
            latest_cell_status = None
            latest_status_parameter = None
            latest_tekscan_status = None
            latest_stop_reason = ""

            while True:
                elapsed = time.time() - start_time
                in_startup_grace = elapsed < settings.startup_grace_s

                voltage = ivium.get_potential()
                current = ivium.get_current()

                temperature_c, _temperature_line = temperature_monitor.read_temperature()

                device_status = ivium.get_device_status()
                cell_status = ivium.get_cell_status()
                status_parameter = ivium.get_status_parameter()

                if device_status == 2:
                    method_was_running = True

                temp_text = "None" if temperature_c is None else f"{temperature_c:.2f}"
                tekscan_status = "on" if tekscan_recording_started else "off"

                print(
                    f"t={elapsed:8.1f} s | "
                    f"E={voltage: .4f} V | "
                    f"I={current: .6f} A | "
                    f"T={temp_text} C | "
                    f"dev={device_status} | "
                    f"cell={cell_status} | "
                    f"stat={status_parameter} | "
                    f"tasks={len(settings.tasks)} | "
                    f"cycles={settings.number_of_cycles} | "
                    f"Tekscan={tekscan_status}"
                )

                row_stop_reason = ""

                if in_startup_grace:
                    print("Startup grace period active. Safety checks skipped.")

                else:
                    if method_was_running and device_status != 2:
                        row_stop_reason = "ivium_method_completed_or_aborted"
                        print("Ivium method no longer running.")

                    elif method_was_running and cell_status == 0:
                        row_stop_reason = "ivium_cell_off"
                        print("Ivium cell is off.")

                    elif voltage > settings.max_safe_voltage_v:
                        row_stop_reason = "max_voltage_safety_limit"
                        print("Maximum voltage safety limit reached.")
                        print(f"Measured voltage was {voltage:.4f} V")

                    elif voltage < settings.min_safe_voltage_v:
                        row_stop_reason = "min_voltage_safety_limit"
                        print("Minimum voltage safety limit reached.")
                        print(f"Measured voltage was {voltage:.4f} V")

                    elif abs(current) > settings.max_safe_current_a:
                        row_stop_reason = "current_safety_limit"
                        print("Current safety limit reached.")
                        print(f"Measured current was {current:.6f} A")

                    elif (
                        settings.max_temperature_c is not None
                        and temperature_c is not None
                        and temperature_c >= settings.max_temperature_c
                    ):
                        row_stop_reason = "temperature_safety_limit"
                        print("Temperature safety limit reached.")
                        print(f"Measured temperature was {temperature_c:.2f} °C")

                if row_stop_reason == "" and terminal_escape_pressed():
                    row_stop_reason = "manual terminal escape."
                    print("Manual stop requested from terminal with Esc.")

                if row_stop_reason == "" and elapsed >= settings.hard_timeout_s:
                    row_stop_reason = "hard_timeout"
                    print("Hard timeout reached.")

                if row_stop_reason != "":
                    stop_reason = row_stop_reason

                status_state = "running."

                if row_stop_reason != "":
                    status_state = "stopping."

                latest_elapsed_s = elapsed
                latest_voltage_v = voltage
                latest_current_a = current
                latest_temperature_c = temperature_c
                latest_device_status = device_status
                latest_cell_status = cell_status
                latest_status_parameter = status_parameter
                latest_tekscan_status = tekscan_status
                latest_stop_reason = row_stop_reason

                status_logger.write_status(
                    state=status_state,
                    elapsed_time_s=f"{elapsed:.1f}",
                    potential_v=f"{voltage:.6f}",
                    current_a=f"{current:.9f}",
                    temperature_c="" if temperature_c is None else f"{temperature_c:.2f}",
                    device_status=device_status,
                    cell_status=cell_status,
                    status_parameter=status_parameter,
                    requested_tasks=len(settings.tasks),
                    requested_cycles=settings.number_of_cycles,
                    max_temperature_c="" if settings.max_temperature_c is None else settings.max_temperature_c,
                    max_safe_voltage_v=settings.max_safe_voltage_v,
                    min_safe_voltage_v=settings.min_safe_voltage_v,
                    max_safe_current_a=settings.max_safe_current_a,
                    tekscan_enabled=settings.use_tekscan,
                    tekscan_recording=tekscan_status,
                    csv_log=log_path,
                    terminal_log=terminal_log_path,
                    stop_reason=row_stop_reason,
                )

                writer.writerow(
                    [
                        f"{elapsed:.3f}",
                        f"{voltage:.6f}",
                        f"{current:.9f}",
                        "" if temperature_c is None else f"{temperature_c:.2f}",
                        device_status,
                        cell_status,
                        status_parameter,
                        len(settings.tasks),
                        settings.number_of_cycles,
                        tekscan_status,
                        row_stop_reason,
                    ]
                )
                file.flush()

                if row_stop_reason != "":
                    print("STOP DETECTED IN LOOP")
                    print(f"Stop reason in loop: {row_stop_reason}")

                    if row_stop_reason == "ivium_method_completed_or_aborted":
                        print("Ivium already stopped or manually aborted. Stopping Tekscan now.")
                        stop_tekscan_recording_if_needed(force=settings.use_tekscan)

                    else:
                        print("Python-triggered stop. Aborting Ivium before stopping Tekscan.")
                        shutdown_ivium_output_if_needed()
                        stop_tekscan_recording_if_needed(force=settings.use_tekscan)

                    break

                time.sleep(1)

    finally:
        print("Stopping experiment...")
        print("Stop reason:", stop_reason)

        try:
            status_logger.write_status(
                force=True,
                state="Stopping and cleaning up",
                elapsed_time_s="" if latest_elapsed_s is None else f"{latest_elapsed_s:.1f}",
                potential_v="" if latest_voltage_v is None else f"{latest_voltage_v:.6f}",
                current_a="" if latest_current_a is None else f"{latest_current_a:.9f}",
                temperature_c="" if latest_temperature_c is None else f"{latest_temperature_c:.2f}",
                device_status=latest_device_status,
                cell_status=latest_cell_status,
                status_parameter=latest_status_parameter,
                requested_tasks=len(settings.tasks),
                requested_cycles=settings.number_of_cycles,
                max_temperature_c="" if settings.max_temperature_c is None else settings.max_temperature_c,
                max_safe_voltage_v=settings.max_safe_voltage_v,
                min_safe_voltage_v=settings.min_safe_voltage_v,
                max_safe_current_a=settings.max_safe_current_a,
                tekscan_enabled=settings.use_tekscan,
                tekscan_recording=latest_tekscan_status,
                csv_log=log_path,
                terminal_log=terminal_log_path,
                stop_reason=stop_reason,
            )
        
        except Exception as e:
            print(f"Status update failed: {e}")

        stop_tekscan_recording_if_needed(force=settings.use_tekscan)
        shutdown_ivium_output_if_needed()

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
        try:
            status_logger.write_status(
                force = True,
                state="stopped",
                elapsed_time_s="" if latest_elapsed_s is None else f"{latest_elapsed_s:.1f}",
                potential_v="" if latest_voltage_v is None else f"{latest_voltage_v:.6f}",
                current_a="" if latest_current_a is None else f"{latest_current_a:.9f}",
                temperature_c="" if latest_temperature_c is None else f"{latest_temperature_c:.2f}",
                device_status=latest_device_status,
                cell_status=latest_cell_status,
                status_parameter=latest_status_parameter,
                requested_tasks=len(settings.tasks),
                requested_cycles=settings.number_of_cycles,
                max_temperature_c="" if settings.max_temperature_c is None else settings.max_temperature_c,
                max_safe_voltage_v=settings.max_safe_voltage_v,
                min_safe_voltage_v=settings.min_safe_voltage_v,
                max_safe_current_a=settings.max_safe_current_a,
                tekscan_enabled=settings.use_tekscan,
                tekscan_recording=latest_tekscan_status,
                csv_log=log_path,
                terminal_log=terminal_log_path,
                stop_reason=stop_reason,
            )
        except Exception as e:
            print(f"Final status update failed: {e}")