import csv
import os
import re
import smtplib
import ssl
import time
from datetime import datetime
from email.message import EmailMessage
from pathlib import Path
import serial
from dotenv import load_dotenv

DEFAULT_PORT = "COM7"
DEFAULT_BAUD = 115200
DEFAULT_TEMP_LIMIT_C = 26.0

EMAIL_ENABLED = True

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
    def __init__(
        self,
        port: str = DEFAULT_PORT,
        baud: int = DEFAULT_BAUD,
        timeout_s: float = 1.0,
        temp_limit_c: float = DEFAULT_TEMP_LIMIT_C,
        email_enabled: bool = False,
        warmup_s: float = 2.0,
    ):
        self.port = port
        self.baud = baud
        self.timeout_s = timeout_s
        self.temp_limit_c = temp_limit_c
        self.email_enabled = email_enabled
        self.warmup_s = warmup_s

        self.serial_connection: serial.Serial | None = None

        self.sender_email = None
        self.sender_password = None
        self.receiver_email = None

        if self.email_enabled:
            self._load_email_settings()

    def _load_email_settings(self) -> None:
        env_path = Path(__file__).with_name("emailinfo.env")
        load_dotenv(env_path)

        self.sender_email = os.getenv("SENDER_EMAIL")
        self.sender_password = os.getenv("SENDER_PASSWORD")
        self.receiver_email = os.getenv("RECEIVER_EMAIL")

        if not self.sender_email or not self.sender_password or not self.receiver_email:
            raise RuntimeError("Email settings could not be loaded. Check emailinfo.env.")

    def open(self) -> None:
        if self.serial_connection is not None and self.serial_connection.is_open:
            return

        self.serial_connection = serial.Serial(
            self.port,
            self.baud,
            timeout=self.timeout_s,
        )

        # Give Arduino time to reset after opening serial connection.
        time.sleep(self.warmup_s)

    def close(self) -> None:
        if self.serial_connection is not None and self.serial_connection.is_open:
            self.serial_connection.close()

    def read_line(self) -> str:
        if self.serial_connection is None or not self.serial_connection.is_open:
            raise RuntimeError("Temperature serial connection is not open.")

        line = self.serial_connection.readline().decode("utf-8", errors="replace").strip()
        return line

    def read_temperature(self) -> tuple[float | None, str]:
        """
        Reads one line from Arduino and tries to extract temperature.

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

    def temperature_limit_exceeded(self, temperature_c: float | None) -> bool:
        if temperature_c is None:
            return False

        return temperature_c >= self.temp_limit_c

    def send_temperature_alarm(
        self,
        temperature_c: float,
        line: str,
        pc_time: str,
    ) -> None:
        if not self.email_enabled:
            return

        if not self.sender_email or not self.sender_password or not self.receiver_email:
            raise RuntimeError("Email settings are missing.")

        subject = "Temperature alarm - battery CT experiment"

        body = f"""Temperature limit exceeded.

PC time: {pc_time}
Temperature: {temperature_c:.2f} °C
Limit: {self.temp_limit_c:.2f} °C

Arduino line:
{line}

The Python logging script has stopped.
"""
        msg = EmailMessage()
        msg["From"] = self.sender_email
        msg["To"] = self.receiver_email
        msg["Subject"] = subject
        msg.set_content(body)

        context = ssl.create_default_context()

        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(
                self.sender_email.strip(),
                self.sender_password.replace(" ", "").strip(),
            )
            server.send_message(msg)

def run_temperature_logger(
    port: str = DEFAULT_PORT,
    baud: int = DEFAULT_BAUD,
    temp_limit_c: float = DEFAULT_TEMP_LIMIT_C,
    email_enabled: bool = EMAIL_ENABLED,
) -> None:
    """
    Standalone temperature logger.

    This keeps tempmoni.py usable by itself, but the important part for the
    combined experiment is the TemperatureMonitor class above.
    """
    filename = datetime.now().strftime("temperature_log_%Y-%m-%d_%H-%M-%S.csv")

    monitor = TemperatureMonitor(
        port=port,
        baud=baud,
        temp_limit_c=temp_limit_c,
        email_enabled=email_enabled,
    )

    monitor.open()

    try:
        with open(filename, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["pc_timestamp", "arduino_line", "temperature_C", "alarm"])
            file.flush()

            print(f"Logging from {port} to {filename}")
            print(f"Temperature limit: {temp_limit_c:.2f} °C")
            print("Press Ctrl+C to stop manually.")

            while True:
                temperature_c, line = monitor.read_temperature()

                if not line:
                    continue

                pc_time = datetime.now().strftime("%Y-%m-%d | %H:%M:%S.%f")[:-3]
                alarm = ""

                if monitor.temperature_limit_exceeded(temperature_c):
                    alarm = "TEMPERATURE_LIMIT_EXCEEDED"

                    writer.writerow([pc_time, line, temperature_c, alarm])
                    file.flush()

                    print(f"{pc_time} | {line} | ALARM: temperature limit exceeded")

                    if email_enabled:
                        try:
                            monitor.send_temperature_alarm(temperature_c, line, pc_time)
                            print("Alarm email sent.")
                        except Exception as e:
                            print(f"Failed to send alarm email: {e}")

                    print("Measurement stopped because temperature limit was exceeded.")
                    break

                writer.writerow([pc_time, line, temperature_c, alarm])
                file.flush()

                print(f"{pc_time} | {line}")

    except KeyboardInterrupt:
        print("\nLogging stopped manually.")

    finally:
        monitor.close()

if __name__ == "__main__":
    run_temperature_logger(
        port=DEFAULT_PORT,
        baud=DEFAULT_BAUD,
        temp_limit_c=DEFAULT_TEMP_LIMIT_C,
        email_enabled=EMAIL_ENABLED,
    )