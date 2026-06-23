import os
import ctypes
from ctypes import c_long, c_double, byref
from pathlib import Path
from dataclasses import dataclass

DLL_PATH = r"C:\IviumStat\Software Development Driver\IVIUM_remdriver64.dll"

@dataclass
class IviumCycleTask:
    task_type: str          # "charge", "discharge", or "rest"
    current_mA: float = 0.0
    voltage_limit_v: float | None = None
    duration_s: float | None = None

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

def replace_line_if_found(data: bytes, key: bytes, value: bytes) -> tuple[bytes, bool]:
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
            return b"".join(lines), True

    return data, False

def create_cycle_imf(
    template_path: str,
    output_path: str,
    tasks: list[IviumCycleTask],
    number_of_cycles: int,
) -> str:
    """
    Creates a modified Ivium CycliScan .imf method.

    Ivium structure:
    - Tasks=<number of tasks in one cycle>
    - Cycles=<number of full cycles>

    Supported task types:
    - charge:    CC with E> voltage limit
    - discharge: CC with E< voltage limit
    - rest:      OCP/rest with Timer> duration
    """

    template_path = Path(template_path)
    output_path = Path(output_path)

    if not template_path.exists():
        raise FileNotFoundError(f"Could not find template method file: {template_path}")

    if len(tasks) < 1:
        raise ValueError("At least one task is required.")

    if number_of_cycles < 1:
        raise ValueError("Number of cycles must be at least 1.")

    data = template_path.read_bytes()
    lines = data.splitlines(keepends=True)

    def get_newline(line: bytes) -> bytes:
        if line.endswith(b"\r\n"):
            return b"\r\n"
        if line.endswith(b"\n"):
            return b"\n"
        return b""

    def set_value(line: bytes, value: str | bytes) -> bytes:
        newline = get_newline(line)

        if isinstance(value, str):
            value_bytes = value.encode("ascii")
        else:
            value_bytes = value

        key = line.split(b"=", 1)[0]
        return key + b"=" + value_bytes + newline

    def task_line_base(line: bytes) -> bytes:
        key = line.split(b"=", 1)[0]

        if b"[" in key:
            return key.split(b"[", 1)[0]

        return key

    def extract_task_template(task_index: int) -> list[bytes]:
        marker = f"[{task_index}]".encode("ascii")
        block = []

        for line in lines:
            if line.startswith(b"Tasks.") and marker in line:
                block.append(line)

        if not block:
            raise ValueError(f"Could not find task template for task {task_index}.")

        return block

    def convert_task_block(
        template_block: list[bytes],
        old_index: int,
        new_index: int,
        task: IviumCycleTask,
        task_label: str,
    ) -> list[bytes]:
        old_marker = f"[{old_index}]".encode("ascii")
        new_marker = f"[{new_index}]".encode("ascii")

        task_type = task.task_type.strip().lower()

        if task_type not in ("charge", "discharge", "rest"):
            raise ValueError(
                f"Unsupported task type: {task.task_type}. "
                "Use 'charge', 'discharge', or 'rest'."
            )

        if task_type in ("charge", "discharge") and task.voltage_limit_v is None:
            raise ValueError(f"Voltage limit is required for task type '{task_type}'.")

        if task_type == "rest" and task.duration_s is None:
            raise ValueError("Duration in seconds is required for rest tasks.")

        new_block = []

        for line in template_block:
            new_line = line.replace(old_marker, new_marker)
            base = task_line_base(new_line)

            if base == b"Tasks.Loop":
                new_line = set_value(new_line, "Single")

            elif base == b"Tasks.Mode":
                if task_type == "rest":
                    new_line = set_value(new_line, "OCP")
                else:
                    new_line = set_value(new_line, "CC")

            elif base == b"Tasks.Tech":
                new_line = set_value(new_line, "DC")

            elif base == b"Tasks.I":
                if task_type == "rest":
                    new_line = set_value(new_line, "0")
                else:
                    new_line = set_value(new_line, f"{task.current_mA:g}")

            elif base == b"Tasks.Iunit":
                new_line = set_value(new_line, "mA")

            elif base == b"Tasks.End1":
                if task_type == "charge":
                    new_line = set_value(new_line, "E>")
                elif task_type == "discharge":
                    new_line = set_value(new_line, "E<")
                else:
                    new_line = set_value(new_line, "Timer>")

            elif base == b"Tasks.End2":
                new_line = set_value(new_line, "select")

            elif base == b"Tasks.End3":
                new_line = set_value(new_line, "select")

            elif base == b"Tasks.End4":
                new_line = set_value(new_line, "select")

            elif base == b"Tasks.Label":
                new_line = set_value(new_line, task_label)

            elif base == b"Tasks.E>":
                if task_type == "charge":
                    new_line = set_value(new_line, f"{task.voltage_limit_v:g}")
                else:
                    new_line = set_value(new_line, "1")

            elif base == b"Tasks.E<":
                if task_type == "discharge":
                    new_line = set_value(new_line, f"{task.voltage_limit_v:g}")
                else:
                    new_line = set_value(new_line, "1")

            elif base == b"Tasks.Timer>":
                if task_type == "rest":
                    new_line = set_value(new_line, f"{task.duration_s:g}")
                else:
                    new_line = set_value(new_line, "10")

            elif base == b"Tasks.Duration":
                if task_type == "rest":
                    new_line = set_value(new_line, f"{task.duration_s:g}")

            elif base == b"Tasks.Timeunit":
                new_line = set_value(new_line, "s")

            new_block.append(new_line)

        return new_block

    tasks_line_index = None
    first_task_line_index = None
    after_task_section_index = None

    for i, line in enumerate(lines):
        if line.startswith(b"Tasks="):
            tasks_line_index = i
            break

    if tasks_line_index is None:
        raise ValueError("Could not find 'Tasks=' line in template method.")

    for i in range(tasks_line_index + 1, len(lines)):
        if lines[i].startswith(b"Tasks."):
            first_task_line_index = i
            break

    if first_task_line_index is None:
        raise ValueError("Could not find task section in template method.")

    for i in range(first_task_line_index, len(lines)):
        if not lines[i].startswith(b"Tasks."):
            after_task_section_index = i
            break

    if after_task_section_index is None:
        raise ValueError("Could not find end of task section in template method.")

    charge_template = extract_task_template(1)
    discharge_template = extract_task_template(2)

    new_lines = []

    new_lines.extend(lines[:tasks_line_index])
    new_lines.append(set_value(lines[tasks_line_index], str(len(tasks))))

    charge_label_used = False
    discharge_label_used = False

    for task_number, task in enumerate(tasks, start=1):
        task_type = task.task_type.strip().lower()

        if task_type == "charge":
            template_block = charge_template
            old_index = 1

            if not charge_label_used:
                task_label = "CH1:"
                charge_label_used = True
            else:
                task_label = "N:"

        elif task_type == "discharge":
            template_block = discharge_template
            old_index = 2

            if not discharge_label_used:
                task_label = "DCH1:"
                discharge_label_used = True
            else:
                task_label = "N:"

        elif task_type == "rest":
            template_block = charge_template
            old_index = 1
            task_label = "N:"

        else:
            raise ValueError(
                f"Unsupported task type: {task.task_type}. "
                "Use 'charge', 'discharge', or 'rest'."
            )

        new_lines.extend(
            convert_task_block(
                template_block=template_block,
                old_index=old_index,
                new_index=task_number,
                task=task,
                task_label=task_label,
            )
        )

    new_lines.extend(lines[after_task_section_index:])

    rebuilt_data = b"".join(new_lines)

    rebuilt_data = replace_line(
        rebuilt_data,
        b"Cycles=",
        f"{number_of_cycles:d}".encode("ascii"),
    )

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_bytes(rebuilt_data)

    return str(output_path)