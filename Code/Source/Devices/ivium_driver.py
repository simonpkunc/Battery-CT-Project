import os
import time
import csv
import ctypes
from ctypes import c_long, c_double, byref
from pathlib import Path

DLL_PATH = r"C:\IviumStat\Software Development Driver\IVIUM_remdriver64.dll"

class IviumDriver:
    def __init__(self, dll_path: str):
        self.dll_path = Path(dll_path)

        if not self.dll_path.exists():
            raise FileNotFoundError(f"Could not find Ivium DLL: {self.dll_path}")

        os.add_dll_directory(str(self.dll_path.parent))
        os.chdir(str(self.dll_path.parent))

        self.dll = ctypes.WinDLL(str(self.dll_path))

        self.dll.IV_open.restype = c_long

        self.dll.IV_close.restype = c_long

        self.dll.IV_connect.restype = c_long
        self.dll.IV_connect.argtypes = [ctypes.POINTER(c_long)]

        self.dll.IV_getpotential.restype = c_long
        self.dll.IV_getpotential.argtypes = [ctypes.POINTER(c_double)]

        self.dll.IV_getcurrent.restype = c_long
        self.dll.IV_getcurrent.argtypes = [ctypes.POINTER(c_double)]

        self.dll.IV_setcellon.restype = c_long
        self.dll.IV_setcellon.argtypes = [ctypes.POINTER(c_long)]

        self.dll.IV_setconnectionmode.restype = c_long
        self.dll.IV_setconnectionmode.argtypes = [ctypes.POINTER(c_long)]

        self.dll.IV_startmethod.restype = c_long
        self.dll.IV_startmethod.argtypes = [ctypes.c_char_p]

        self.dll.IV_abort.restype = c_long
        self.dll.IV_abort.argtypes = []

        # Status functions
        self.dll.IV_getdevicestatus.restype = c_long

        self.dll.IV_getcellstatus.restype = c_long
        self.dll.IV_getcellstatus.argtypes = [ctypes.POINTER(c_long)]

        self.dll.IV_StatusParGet.restype = c_long
        self.dll.IV_StatusParGet.argtypes = [ctypes.POINTER(c_long)]

    def open(self) -> int:
        return self.dll.IV_open()

    def close(self) -> int:
        return self.dll.IV_close()

    def connect(self) -> int:
        value = c_long(1)
        return self.dll.IV_connect(byref(value))

    def get_potential(self) -> float:
        value = c_double()
        result = self.dll.IV_getpotential(byref(value))

        # Return code 3 appears while a method is running, but values are still valid.
        if result not in (0, 3):
            print("Warning: IV_getpotential returned:", result)

        return value.value

    def get_current(self) -> float:
        value = c_double()
        result = self.dll.IV_getcurrent(byref(value))

        # Return code 3 appears while a method is running, but values are still valid.
        if result not in (0, 3):
            print("Warning: IV_getcurrent returned:", result)

        return value.value

    def get_device_status(self) -> int:
        return self.dll.IV_getdevicestatus()

    def get_cell_status(self) -> int:
        value = c_long()
        result = self.dll.IV_getcellstatus(byref(value))

        if result not in (0, 3):
            print("Warning: IV_getcellstatus returned:", result)

        return value.value

    def get_status_parameter(self) -> int:
        value = c_long()
        result = self.dll.IV_StatusParGet(byref(value))

        if result not in (0, 3):
            print("Warning: IV_StatusParGet returned:", result)

        return value.value

    def start_method(self, method_path: str) -> int:
        return self.dll.IV_startmethod(method_path.encode("mbcs"))

    def abort(self) -> int:
        return self.dll.IV_abort()

    def set_cell_on(self, on: bool) -> int:
        value = c_long(1 if on else 0)
        return self.dll.IV_setcellon(byref(value))

    def set_connection_mode(self, on: bool) -> int:
        value = c_long(1 if on else 0)
        return self.dll.IV_setconnectionmode(byref(value))

def replace_line(data: bytes, key: bytes, value: bytes, required: bool = True) -> bytes:
    lines = data.splitlines(keepends=True)

    for i, line in enumerate(lines):
        if line.startswith(key):
            if line.endswith(b"\r\n"):
                newline = b"\r\n"
            elif line.endswith(b"\n"):
                newline = b"\n"
            else:
                newline = b""

            lines[i] = key + value + newline
            return b"".join(lines)

    if required:
        raise ValueError(f"Could not find line starting with {key.decode('ascii')!r}")

    return data

def create_cycle_imf(
    template_path: str,
    output_path: str,
    charge_current_uA: float,
    discharge_current_uA: float,
    upper_voltage_v: float,
    lower_voltage_v: float,
) -> str:
    """
    Creates a modified copy of a two-task Ivium .imf method.

    Expected template:
    Task 1: CC charge, ending at E >
    Task 2: CC discharge, ending at E <

    It modifies:
    - Tasks.I[1]
    - Tasks.E>[1]
    - Tasks.I[2]
    - Tasks.E<[2]
    """
    template_path = Path(template_path)
    output_path = Path(output_path)

    if not template_path.exists():
        raise FileNotFoundError(f"Could not find template method file: {template_path}")

    data = template_path.read_bytes()

    data = replace_line(data, b"Tasks.I[1]=", f"{charge_current_uA:g}".encode("ascii"))
    data = replace_line(data, b"Tasks.E>[1]=", f"{upper_voltage_v:g}".encode("ascii"))

    data = replace_line(data, b"Tasks.I[2]=", f"{discharge_current_uA:g}".encode("ascii"))
    data = replace_line(data, b"Tasks.E<[2]=", f"{lower_voltage_v:g}".encode("ascii"))

    data = replace_line(data, b"Tasks.Iunit[1]=", b"uA", required=False)
    data = replace_line(data, b"Tasks.Iunit[2]=", b"uA", required=False)

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_bytes(data)

    return str(output_path)

def run_ivium_cycle(
    method_path: str,
    log_path: str,
    max_runtime_s: float = 30.0,
    safety_abs_voltage_v: float = 4.25,
    safety_abs_current_a: float = 0.001,
) -> None:
    method_path = str(Path(method_path).resolve())
    log_path = Path(log_path).resolve()
    log_path.parent.mkdir(parents=True, exist_ok=True)

    print("Method file:", method_path)
    print("CSV will be saved to:", log_path)

    ivium = IviumDriver(DLL_PATH)

    result = ivium.open()
    print("Open:", result)

    if result != 0:
        raise SystemExit("IV_open failed. Make sure IviumSoft is open and connected.")

    print("Connecting...")
    print("Connect:", ivium.connect())

    print("Starting method...")
    start_result = ivium.start_method(method_path)
    print("Start method:", start_result)

    if start_result != 0:
        raise SystemExit("IV_startmethod failed. Check the .imf file and IviumSoft status.")

    start_time = time.time()

    method_was_running = False

    try:
        with open(log_path, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(
                [
                    "time_s",
                    "potential_V",
                    "current_A",
                    "device_status",
                    "cell_status",
                    "status_parameter",
                ]
            )
            file.flush()

            while True:
                elapsed = time.time() - start_time

                voltage = ivium.get_potential()
                current = ivium.get_current()

                device_status = ivium.get_device_status()
                cell_status = ivium.get_cell_status()
                status_parameter = ivium.get_status_parameter()

                if device_status == 2:
                    method_was_running = True

                if method_was_running and device_status != 2:
                    print("Ivium method no longer running.")
                    print("Assuming method was completed or aborted.")
                    break

                if method_was_running and cell_status == 0:
                    print("Ivium cell is off.")
                    print("Assuming method was completed or aborted.")
                    break

                writer.writerow(
                    [
                        elapsed,
                        voltage,
                        current,
                        device_status,
                        cell_status,
                        status_parameter,
                    ]
                )
                file.flush()

                print(
                    f"t={elapsed:6.1f} s | "
                    f"E={voltage: .4f} V | "
                    f"I={current: .6f} A | "
                    f"dev={device_status} | "
                    f"cell={cell_status} | "
                    f"stat={status_parameter}"
                )

                if abs(voltage) > safety_abs_voltage_v:
                    print("Voltage safety limit reached.")
                    print(f"Measured voltage was {voltage:.4f} V")
                    break

                if abs(current) > safety_abs_current_a:
                    print("Current safety limit reached.")
                    print(f"Measured current was {current:.6f} A")
                    break

                if elapsed >= max_runtime_s:
                    print("Time limit reached.")
                    break

                time.sleep(1)

    finally:
        print("Aborting Ivium method...")
        print("Abort:", ivium.abort())
        print("Cell off:", ivium.set_cell_on(False))
        print("Connection mode off:", ivium.set_connection_mode(False))
        print("Close:", ivium.close())
        print(f"Data saved to: {log_path}")

if __name__ == "__main__":
    script_folder = Path(__file__).resolve().parent

    # Expected project structure:
    # Code/Source/Devices/ivium_driver.py
    # Code/Configuration/ivium_cycle_template.imf
    code_folder = script_folder.parent.parent
    config_folder = code_folder / "Configuration"

    template_file = config_folder / "ivium_cycle_template.imf"

    generated_methods_folder = code_folder / "Data" / "Generated methods"
    generated_methods_folder.mkdir(parents=True, exist_ok=True)

    generated_file = generated_methods_folder / "generated_ivium_cycle.imf"

    log_file = script_folder / "ivium_cycle_test_log.csv"

    # Abort-status test with dummy load.
    #
    # With 9.97 kOhm:
    # +150 uA gives about +1.50 V.
    #
    # upper_voltage_v=2.0 means Task 1 will keep running and not finish immediately.
    # This gives you time to press Abort in IviumSoft and watch dev/cell/stat change.
    generated_method = create_cycle_imf(
        template_path=str(template_file),
        output_path=str(generated_file),
        charge_current_uA=150,
        discharge_current_uA=-150,
        upper_voltage_v=4.2,
        lower_voltage_v=-3.0,
    )

    run_ivium_cycle(
        method_path=generated_method,
        log_path=str(log_file),
        max_runtime_s=30,
        safety_abs_voltage_v=4.25,
        safety_abs_current_a=0.001,
    )