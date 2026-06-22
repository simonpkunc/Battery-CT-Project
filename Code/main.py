from datetime import datetime
from pathlib import Path
from Source.Devices.ivium_driver import IviumCycleTask
from Source.Experiment.cycling_experiment import (
    ExperimentSettings,
    run_battery_experiment,)
from Source.Logging.status_logger import mirror_stdout_to_file

NOMINAL_CAPACITY_MAH = 110.0

def ask_float(prompt: str, default: float) -> float:
    user_input = input(f"{prompt} [{default}]: ").strip()

    if user_input == "":
        return default

    return float(user_input.replace(",", "."))

def ask_int(prompt: str, default: int) -> int:
    user_input = input(f"{prompt} [{default}]: ").strip()

    if user_input == "":
        return default

    return int(user_input)

def ask_yes_no(prompt: str, default: bool = False) -> bool:
    default_text = "y" if default else "n"
    user_input = input(f"{prompt} [y/n, default {default_text}]: ").strip().lower()

    if user_input == "":
        return default

    return user_input in ("y", "yes", "j", "ja")

def ask_task_type(task_number: int, default: str) -> str:
    while True:
        user_input = input(
            f"Task {task_number} type [charge/discharge/rest, default {default}]: "
        ).strip().lower()

        if user_input == "":
            return default

        if user_input in ("charge", "ch", "c", "laddning", "ladda"):
            return "charge"

        if user_input in ("discharge", "dch", "d", "urladdning", "urladda"):
            return "discharge"

        if user_input in ("rest", "ocp", "pause", "paus", "vilopaus", "vila"):
            return "rest"

        print("Invalid task type. Use 'charge', 'discharge', or 'rest'.")

def sanitize_filename_part(text: str, default: str = "battery_experiment") -> str:
    text = text.strip()

    if text == "":
        return default

    allowed_characters = []

    for character in text:
        if character.isalnum():
            allowed_characters.append(character)
        elif character in (" ", "-", "_"):
            allowed_characters.append("_")

    cleaned = "".join(allowed_characters)

    while "__" in cleaned:
        cleaned = cleaned.replace("__", "_")

    cleaned = cleaned.strip("_")

    if cleaned == "":
        return default

    return cleaned

def current_to_c_rate(current_mA: float) -> float:
    return abs(current_mA) / NOMINAL_CAPACITY_MAH

def build_tasks_from_user_input() -> list[IviumCycleTask]:
    number_of_tasks = ask_int("Number of tasks in one cycle", 3)

    if number_of_tasks < 1:
        raise ValueError("Number of tasks must be at least 1.")

    tasks = []

    print()
    print("Define tasks")
    print("============")
    print("Supported task types:")
    print("- charge:    CC charge until E > voltage limit")
    print("- discharge: CC discharge until E < voltage limit")
    print("- rest:      OCP/rest for a selected duration")
    print()

    default_three_task_sequence = ["charge", "rest", "discharge"]

    for task_number in range(1, number_of_tasks + 1):
        if number_of_tasks == 3:
            default_type = default_three_task_sequence[task_number - 1]
        elif task_number % 2 == 1:
            default_type = "charge"
        else:
            default_type = "discharge"

        task_type = ask_task_type(task_number, default=default_type)

        if task_type == "charge":
            default_current_mA = 22.0
            default_voltage_limit_v = 4.20

            current_mA = ask_float(
                f"Task {task_number} current [mA]",
                default_current_mA,
            )
            current_mA = abs(current_mA)

            voltage_limit_v = ask_float(
                f"Task {task_number} voltage limit [V]",
                default_voltage_limit_v,
            )

            tasks.append(
                IviumCycleTask(
                    task_type=task_type,
                    current_mA=current_mA,
                    voltage_limit_v=voltage_limit_v,
                )
            )

        elif task_type == "discharge":
            default_current_mA = -22.0
            default_voltage_limit_v = 3.00

            current_mA = ask_float(
                f"Task {task_number} current [mA]",
                default_current_mA,
            )
            current_mA = -abs(current_mA)

            voltage_limit_v = ask_float(
                f"Task {task_number} voltage limit [V]",
                default_voltage_limit_v,
            )

            tasks.append(
                IviumCycleTask(
                    task_type=task_type,
                    current_mA=current_mA,
                    voltage_limit_v=voltage_limit_v,
                )
            )

        elif task_type == "rest":
            duration_s = ask_float(
                f"Task {task_number} rest duration [s]",
                120.0,
            )

            tasks.append(
                IviumCycleTask(
                    task_type=task_type,
                    duration_s=duration_s,
                )
            )

        print()

    return tasks

def main() -> None:
    print()
    print("Battery CT experiment control")
    print("=============================")
    print()
    print("Before starting, make sure that:")
    print("- IviumSoft is open and connected.")
    print("- IviumSoft shows approximately the same voltage as the multimeter.")
    print("- Arduino Serial Monitor is closed.")
    print("- The battery/dummy load is connected correctly.")
    print("- I-Scan is opened and the correct files for calibration equilibration are loaded.")
    print()

    run_setup = ask_yes_no("Start experiment?", default=True)

    if not run_setup:
        print("Experiment cancelled.")
        return

    print()
    print("Enter experiment settings.")
    print("Press Enter to use the default value in the brackets.")
    print()

    experiment_name_input = input("Experiment name [battery_test]: ").strip()
    experiment_name = sanitize_filename_part(experiment_name_input, default="battery_test")

    tasks = build_tasks_from_user_input()

    number_of_cycles = ask_int("Number of cycles", 1)

    max_temperature_c = ask_float("Maximum temperature [deg C]", 35.0)

    max_safe_voltage_v = ask_float("Absolute maximum safe voltage [V]", 4.25)
    min_safe_voltage_v = ask_float("Absolute minimum safe voltage [V]", 2.80)
    max_safe_current_a = ask_float("Absolute maximum safe current [A]", 0.15)

    temperature_port = input("Temperature port [COM7]: ").strip()

    if temperature_port == "":
        temperature_port = "COM7"

    temperature_baud = 115200

    use_tekscan = ask_yes_no("Use Tekscan recording?", default=False)

    if use_tekscan:
        print()
        print("Tekscan checklist")
        print("=================")
        print("Before continuing, make sure that:")
        print("- I-Scan is open")
        print("- The correct sensor/map is selected")
        print("- A New Recording / real-time window is open")
        print("- The pressure legend / scale window is closed")
        print("- The real-time window is active")
        print("- Manual F2 starts recording")
        print("- Manual F4 stops recording")
        print()
        input("Press Enter when I-Scan is ready...")

    code_folder = Path(__file__).resolve().parent

    config_folder = code_folder / "Configuration"
    data_folder = code_folder / "Data"

    generated_methods_folder = data_folder / "generated_methods"
    logs_folder = data_folder / "logs"

    generated_methods_folder.mkdir(parents=True, exist_ok=True)
    logs_folder.mkdir(parents=True, exist_ok=True)

    template_method_path = config_folder / "ivium_cycle_template.imf"
    generated_method_path = generated_methods_folder / "generated_ivium_cycle.imf"

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    log_path = logs_folder/f"{timestamp}_{experiment_name}.csv"
    terminal_log_path = logs_folder/f"{timestamp}_{experiment_name}_terminal_log.txt"
    status_path = data_folder/"status"/"latest_status.txt"

    settings = ExperimentSettings(
        tasks=tasks,
        number_of_cycles=number_of_cycles,
        startup_grace_s=3.0,
        hard_timeout_s=24 * 60 * 60,
        max_safe_voltage_v=max_safe_voltage_v,
        min_safe_voltage_v=min_safe_voltage_v,
        max_safe_current_a=max_safe_current_a,
        temperature_port=temperature_port,
        temperature_baud=temperature_baud,
        max_temperature_c=max_temperature_c,
        use_tekscan=use_tekscan,
        log_name=log_path.name,)

    print()
    print("Experiment summary")
    print("==================")
    print(f"Experiment name:             {experiment_name}")
    print(f"Number of tasks in cycle:    {len(settings.tasks)}")
    print(f"Number of cycles:            {settings.number_of_cycles}")
    print(f"Terminal log file:           {terminal_log_path}")
    print(f"Latest status file:          {status_path}") 
    print()

    for i, task in enumerate(settings.tasks, start=1):
        print(f"Task {i}")
        print(f"  Type:                     {task.task_type}")

        if task.task_type == "charge":
            c_rate = current_to_c_rate(task.current_mA)
            print(f"  Current:                  {task.current_mA} mA")
            print(f"  Approx. C-rate:           {c_rate:.3f} C")
            print(f"  End condition:            E > {task.voltage_limit_v} V")

        elif task.task_type == "discharge":
            c_rate = current_to_c_rate(task.current_mA)
            print(f"  Current:                  {task.current_mA} mA")
            print(f"  Approx. C-rate:           {c_rate:.3f} C")
            print(f"  End condition:            E < {task.voltage_limit_v} V")

        elif task.task_type == "rest":
            print(f"  Mode:                     OCP / rest")
            print(f"  Duration:                 {task.duration_s} s")

        print()

    print(f"Maximum temperature:         {settings.max_temperature_c} deg C")
    print(f"Startup grace period:        {settings.startup_grace_s} s")
    print(f"Hard safety timeout:         {settings.hard_timeout_s} s")
    print(f"Maximum safe voltage:        {settings.max_safe_voltage_v} V")
    print(f"Minimum safe voltage:        {settings.min_safe_voltage_v} V")
    print(f"Maximum safe current:        {settings.max_safe_current_a} A")
    print(f"Temperature port:            {settings.temperature_port}")
    print(f"Use Tekscan recording:       {settings.use_tekscan}")
    print(f"Template method:             {template_method_path}")
    print(f"Generated method:            {generated_method_path}")
    print(f"Log file:                    {log_path}")
    print()

    print("Reference for this cell:")
    print(f"- Nominal capacity:           {NOMINAL_CAPACITY_MAH} mAh")
    print("- 0.2C current:               22 mA")
    print("- 1C current:                 110 mA")
    print()

    confirm = ask_yes_no("Start experiment now?", default=False)

    if not confirm:
        print("Experiment cancelled.")
        return

    with mirror_stdout_to_file(terminal_log_path):
        run_battery_experiment(
            settings = settings,
            template_method_path = str(template_method_path),
            generated_method_path = str(generated_method_path),
            log_path = str(log_path),
        )

if __name__ == "__main__":
    main()