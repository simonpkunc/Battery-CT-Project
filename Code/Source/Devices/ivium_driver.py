import os
import time
import csv
import ctypes
from ctypes import c_long, c_double, byref
from pathlib import Path


class IviumDriver:
    def __init__(self, dll_path: str):
        self.dll_path = Path(dll_path)

        if not self.dll_path.exists():
            raise FileNotFoundError(f"Could not find Ivium DLL: {self.dll_path}")

        # Needed so Windows can find DLL dependencies in the same folder.
        os.add_dll_directory(str(self.dll_path.parent))

        # Keep this for now because your DLL communication works with it.
        # The CSV path is now absolute, so this will not affect where the CSV is saved.
        os.chdir(str(self.dll_path.parent))

        self.dll = ctypes.WinDLL(str(self.dll_path))

        self.dll.IV_open.restype = c_long

        self.dll.IV_connect.restype = c_long
        self.dll.IV_connect.argtypes = [ctypes.POINTER(c_long)]

        self.dll.IV_getpotential.restype = c_long
        self.dll.IV_getpotential.argtypes = [ctypes.POINTER(c_double)]

        self.dll.IV_getcurrent.restype = c_long
        self.dll.IV_getcurrent.argtypes = [ctypes.POINTER(c_double)]

        self.dll.IV_setconnectionmode.restype = c_long
        self.dll.IV_setconnectionmode.argtypes = [ctypes.POINTER(c_long)]

        self.dll.IV_setcellon.restype = c_long
        self.dll.IV_setcellon.argtypes = [ctypes.POINTER(c_long)]

        self.dll.IV_setcurrent.restype = c_long
        self.dll.IV_setcurrent.argtypes = [ctypes.POINTER(c_double)]

    def open(self) -> int:
        return self.dll.IV_open()

    def connect(self) -> int:
        value = c_long(1)
        return self.dll.IV_connect(byref(value))

    def set_connection_mode(self, on: bool) -> int:
        value = c_long(1 if on else 0)
        return self.dll.IV_setconnectionmode(byref(value))

    def set_cell_on(self, on: bool) -> int:
        value = c_long(1 if on else 0)
        return self.dll.IV_setcellon(byref(value))

    def set_current(self, current_a: float) -> int:
        value = c_double(current_a)
        return self.dll.IV_setcurrent(byref(value))

    def get_potential(self) -> float:
        value = c_double()
        result = self.dll.IV_getpotential(byref(value))

        if result != 0:
            print("Warning: IV_getpotential returned:", result)

        return value.value

    def get_current(self) -> float:
        value = c_double()
        result = self.dll.IV_getcurrent(byref(value))

        if result != 0:
            print("Warning: IV_getcurrent returned:", result)

        return value.value

    def stop(self) -> None:
        print("Stopping Ivium output...")
        print("Set current 0 A:", self.set_current(0.0))
        print("Cell off:", self.set_cell_on(False))
        print("Connection mode off:", self.set_connection_mode(False))


def run_current_test(
    current_a: float = 0.001,
    duration_s: float = 20.0,
    voltage_limit_v: float = 4.20,
    log_path: str = "ivium_test_log.csv",
) -> None:
    log_path = Path(log_path).resolve()
    log_path.parent.mkdir(parents=True, exist_ok=True)

    print("CSV will be saved to:", log_path)

    ivium = IviumDriver(
        r"C:\IviumStat\Software Development Driver\IVIUM_remdriver64.dll"
    )

    result = ivium.open()
    print("Open:", result)

    if result != 0:
        raise SystemExit("IV_open failed. Make sure IviumSoft is open and connected.")

    print("Connecting...")
    print("Connect:", ivium.connect())

    print("Connection mode on:", ivium.set_connection_mode(True))
    print("Cell on:", ivium.set_cell_on(True))
    print(f"Set current {current_a} A:", ivium.set_current(current_a))

    start_time = time.time()

    try:
        with open(log_path, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["time_s", "potential_V", "current_A"])
            file.flush()

            while True:
                elapsed = time.time() - start_time
                voltage = ivium.get_potential()
                current = ivium.get_current()

                writer.writerow([elapsed, voltage, current])
                file.flush()

                print(
                    f"t={elapsed:6.1f} s | "
                    f"E={voltage: .4f} V | "
                    f"I={current: .6f} A"
                )

                if elapsed >= duration_s:
                    print("Time limit reached.")
                    break

                if voltage >= voltage_limit_v:
                    print("Voltage limit reached.")
                    break

                time.sleep(1)

    finally:
        ivium.stop()
        print(f"Data saved to: {log_path}")


if __name__ == "__main__":
    script_folder = Path(__file__).parent
    log_file = script_folder / "ivium_test_log.csv"

    run_current_test(
        current_a=0.001,
        duration_s=20,
        voltage_limit_v=4.20,
        log_path=str(log_file),
    )