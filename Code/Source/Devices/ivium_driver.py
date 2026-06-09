import os
import time
import ctypes
from ctypes import c_long, c_double, byref
from pathlib import Path


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

        self.dll.IV_setconnectionmode.restype = c_long
        self.dll.IV_setconnectionmode.argtypes = [ctypes.POINTER(c_long)]

        self.dll.IV_setcellon.restype = c_long
        self.dll.IV_setcellon.argtypes = [ctypes.POINTER(c_long)]

        self.dll.IV_setcurrent.restype = c_long
        self.dll.IV_setcurrent.argtypes = [ctypes.POINTER(c_double)]

    def open(self) -> int:
        return self.dll.IV_open()

    def close(self) -> int:
        return self.dll.IV_close()

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
        self.dll.IV_getpotential(byref(value))
        return value.value

    def get_current(self) -> float:
        value = c_double()
        self.dll.IV_getcurrent(byref(value))
        return value.value

    def stop(self) -> None:
        print("Stopping Ivium output...")
        print("Set current 0 A:", self.set_current(0.0))
        print("Cell off:", self.set_cell_on(False))
        print("Connection mode off:", self.set_connection_mode(False))


if __name__ == "__main__":
    ivium = IviumDriver(
        r"C:\IviumStat\Software Development Driver\IVIUM_remdriver64.dll"
    )

    result = ivium.open()
    print("Open:", result)

    if result != 0:
        raise SystemExit("IV_open failed.")

    print("Connecting...")
    print("Connect:", ivium.connect())

    print("Connection mode on:", ivium.set_connection_mode(True))
    print("Cell on:", ivium.set_cell_on(True))

    print("Set current 1 mA:", ivium.set_current(0.001))

    start_time = time.time()

    try:
        while True:
            elapsed = time.time() - start_time
            voltage = ivium.get_potential()
            current = ivium.get_current()

            print(f"t={elapsed:6.1f} s | E={voltage: .4f} V | I={current: .6f} A")

            if elapsed >= 20:
                print("Time limit reached.")
                break

            if voltage >= 4.20:
                print("Voltage limit reached.")
                break

            time.sleep(1)

    finally:
        ivium.stop()