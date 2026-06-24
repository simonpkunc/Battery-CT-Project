import re
import time

import serial


DEFAULT_PORT = "COM7"
DEFAULT_BAUD = 115200


def extract_temperature(line: str) -> float | None:
    """
    Extracts temperature from an Arduino line such as:
    'Temperature [C]: 23.45'
    """
    match = re.search(r"Temperature \[C\]:\s*([-+]?\d+(?:\.\d+)?)", line)

    if match:
        return float(match.group(1))

    return None


class TemperatureMonitor:
    """
    Reads temperature data from an Arduino serial connection.
    """

    def __init__(
        self,
        port: str = DEFAULT_PORT,
        baud: int = DEFAULT_BAUD,
        timeout_s: float = 1.0,
        warmup_s: float = 2.0,
    ):
        self.port = port
        self.baud = baud
        self.timeout_s = timeout_s
        self.warmup_s = warmup_s

        self.serial_connection: serial.Serial | None = None

    def open(self) -> None:
        if self.serial_connection is not None and self.serial_connection.is_open:
            return

        self.serial_connection = serial.Serial(
            self.port,
            self.baud,
            timeout=self.timeout_s,
        )

        # Give Arduino time to reset after opening the serial connection.
        time.sleep(self.warmup_s)

    def close(self) -> None:
        if self.serial_connection is not None and self.serial_connection.is_open:
            self.serial_connection.close()

    def read_line(self) -> str:
        if self.serial_connection is None or not self.serial_connection.is_open:
            raise RuntimeError("Temperature serial connection is not open.")

        return self.serial_connection.readline().decode(
            "utf-8",
            errors="replace",
        ).strip()

    def read_temperature(self) -> tuple[float | None, str]:
        """
        Reads one line from Arduino and tries to extract the temperature.

        Returns:
            temperature_C, raw_line

        If no valid temperature is found:
            temperature_C = None
        """
        line = self.read_line()

        if not line:
            return None, ""

        temperature_c = extract_temperature(line)
        return temperature_c, line