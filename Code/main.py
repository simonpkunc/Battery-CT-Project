from datetime import datetime
from pathlib import Path

from Source.Experiment.cycling_experiment import (
    ExperimentSettings,
    run_battery_experiment,
)


def ask_float(prompt: str, default: float) -> float:
    user_input = input(f"{prompt} [{default}]: ").strip()

    if user_input == "":
        return default

    return float(user_input.replace(",", "."))


def ask_yes_no(prompt: str, default: bool = False) -> bool:
    default_text = "y" if default else "n"
    user_input = input(f"{prompt} [y/n, default {default_text}]: ").strip().lower()

    if user_input == "":
        return default

    return user_input in ("y", "yes", "j", "ja")


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


def main() -> None:
    print()
    print("Battery CT experiment control")
    print("=============================")
    print()
    print("Make sure that:")
    print("- IviumSoft is open and connected")
    print("- Arduino Serial Monitor is closed")
    print("- The battery/dummy load is connected correctly")
    print()

    run_setup = ask_yes_no("Start setup?", default=True)

    if not run_setup:
        print("Experiment cancelled.")
        return

    print()
    print("Enter experiment settings.")
    print("Press Enter to use the default value.")
    print()

    experiment_name_input = input("Experiment name [battery_test]: ").strip()
    experiment_name = sanitize_filename_part(experiment_name_input, default="battery_test")

    charge_current_uA = ask_float("Charge current [uA]", 100.0)
    discharge_current_uA = ask_float("Discharge current [uA]", -100.0)

    upper_voltage_v = ask_float("Upper voltage limit [V]", 4.20)
    lower_voltage_v = ask_float("Lower voltage limit [V]", 3.00)

    max_temperature_c = ask_float("Maximum temperature [deg C]", 35.0)
    max_runtime_s = ask_float("Maximum runtime [s]", 30.0)

    max_safe_voltage_v = ask_float("Absolute maximum safe voltage [V]", 4.25)
    min_safe_voltage_v = ask_float("Absolute minimum safe voltage [V]", 2.80)
    max_safe_current_a = ask_float("Absolute maximum safe current [A]", 0.0005)

    temperature_port = input("Temperature port [COM7]: ").strip()

    if temperature_port == "":
        temperature_port = "COM7"

    temperature_baud = 115200

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
    log_path = logs_folder / f"{timestamp}_{experiment_name}.csv"

    settings = ExperimentSettings(
        charge_current_uA=charge_current_uA,
        discharge_current_uA=discharge_current_uA,
        upper_voltage_v=upper_voltage_v,
        lower_voltage_v=lower_voltage_v,
        max_runtime_s=max_runtime_s,
        startup_grace_s=3.0,
        max_safe_voltage_v=max_safe_voltage_v,
        min_safe_voltage_v=min_safe_voltage_v,
        max_safe_current_a=max_safe_current_a,
        temperature_port=temperature_port,
        temperature_baud=temperature_baud,
        max_temperature_c=max_temperature_c,
        log_name=log_path.name,
    )

    print()
    print("Experiment summary")
    print("==================")
    print(f"Experiment name:             {experiment_name}")
    print(f"Charge current:              {settings.charge_current_uA} uA")
    print(f"Discharge current:           {settings.discharge_current_uA} uA")
    print(f"Upper voltage limit:         {settings.upper_voltage_v} V")
    print(f"Lower voltage limit:         {settings.lower_voltage_v} V")
    print(f"Maximum temperature:         {settings.max_temperature_c} deg C")
    print(f"Maximum runtime:             {settings.max_runtime_s} s")
    print(f"Startup grace period:        {settings.startup_grace_s} s")
    print(f"Maximum safe voltage:        {settings.max_safe_voltage_v} V")
    print(f"Minimum safe voltage:        {settings.min_safe_voltage_v} V")
    print(f"Maximum safe current:        {settings.max_safe_current_a} A")
    print(f"Temperature port:            {settings.temperature_port}")
    print(f"Template method:             {template_method_path}")
    print(f"Generated method:            {generated_method_path}")
    print(f"Log file:                    {log_path}")
    print()

    confirm = ask_yes_no("Start experiment now?", default=False)

    if not confirm:
        print("Experiment cancelled.")
        return

    run_battery_experiment(
        settings=settings,
        template_method_path=str(template_method_path),
        generated_method_path=str(generated_method_path),
        log_path=str(log_path),
    )


if __name__ == "__main__":
    main()