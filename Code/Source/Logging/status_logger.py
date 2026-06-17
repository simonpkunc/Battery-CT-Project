from __future__ import annotations

import sys
from contextlib import contextmanager
from datetime import datetime
from pathlib import Path
from typing import TextIO


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
    Writes a small status file that can be viewed remotely, for example via OneDrive.
    """

    def __init__(self, status_path: str | Path):
        self.status_path = Path(status_path)
        self.status_path.parent.mkdir(parents=True, exist_ok=True)

    def write_status(self, **fields) -> None:
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

            lines.append(f"{label}: {value_text}")

        lines.append("")

        text = "\n".join(lines)

        temporary_path = self.status_path.with_suffix(".tmp")
        temporary_path.write_text(text, encoding="utf-8")
        temporary_path.replace(self.status_path)