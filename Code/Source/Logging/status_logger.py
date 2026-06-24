from __future__ import annotations

import sys
import time
from contextlib import contextmanager
from datetime import datetime
from pathlib import Path
from typing import TextIO


FIELDS_WITH_PERIOD = (
    "state",
    "elapsed_time_s",
    "potential_v",
    "current_a",
    "temperature_c",
    "device_status",
    "cell_status",
    "status_parameter",
    "requested_tasks",
    "requested_cycles",
    "max_temperature_c",
    "max_safe_voltage_v",
    "min_safe_voltage_v",
    "max_safe_current_a",
    "tekscan_enabled",
    "tekscan_recording",
    "stop_reason",
)


class TeeStream:
    """
    Sends terminal output to both the original terminal and a log file.
    """

    def __init__(self, original_stream: TextIO, log_file: TextIO):
        self.original_stream = original_stream
        self.log_file = log_file

    def write(self, text: str) -> int:
        self.original_stream.write(text)
        self.log_file.write(text)
        self.log_file.flush()
        return len(text)

    def flush(self) -> None:
        self.original_stream.flush()
        self.log_file.flush()

    def isatty(self) -> bool:
        return self.original_stream.isatty()

    @property
    def encoding(self) -> str:
        return self.original_stream.encoding or "utf-8"


@contextmanager
def mirror_stdout_to_file(log_path: str | Path):
    """
    Mirrors everything printed to the terminal into a text log file.
    """
    log_path = Path(log_path)
    log_path.parent.mkdir(parents=True, exist_ok=True)

    original_stdout = sys.stdout
    original_stderr = sys.stderr

    with open(log_path, "a", encoding="utf-8", buffering=1) as log_file:
        sys.stdout = TeeStream(original_stdout, log_file)
        sys.stderr = TeeStream(original_stderr, log_file)

        try:
            print()
            print("Terminal logging started")
            print("========================")
            print(f"Terminal log file: {log_path}")
            print(f"Start time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
            print()
            yield

        finally:
            print()
            print("Terminal logging stopped")
            print("=========================")
            print(f"Stop time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
            print()

            sys.stdout = original_stdout
            sys.stderr = original_stderr


class ExperimentStatusLogger:
    """
    Writes a small status file that can be viewed remotely, for example via Google Drive.

    To avoid overwhelming the sync client, normal status updates are written at most
    once every min_write_interval_s seconds. Important updates can be forced.
    """

    def __init__(self, status_path: str | Path, min_write_interval_s: float = 15.0):
        self.status_path = Path(status_path)
        self.status_path.parent.mkdir(parents=True, exist_ok=True)
        self.min_write_interval_s = min_write_interval_s
        self._last_write_time = 0.0

    def write_status(self, force: bool = False, **fields) -> None:
        now_monotonic = time.monotonic()

        if (
            not force
            and (now_monotonic - self._last_write_time) < self.min_write_interval_s
        ):
            return

        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        lines = [
            "Battery CT experiment status",
            "============================",
            f"Last update: {now}",
            "",
        ]

        for key, value in fields.items():
            label = key.replace("_", " ").capitalize()

            if value is None:
                value_text = ""
            else:
                value_text = str(value)

            if key in FIELDS_WITH_PERIOD and value_text != "":
                value_text = value_text.rstrip(".") + "."

            lines.append(f"{label}: {value_text}")

        lines.append("")
        text = "\n".join(lines)

        with open(self.status_path, "w", encoding="utf-8") as file:
            file.write(text)
            file.flush()

        self._last_write_time = time.monotonic()