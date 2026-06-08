import serial
import csv
import time
import re
import smtplib
import ssl
import os
from dotenv import load_dotenv
from datetime import datetime
from email.message import EmailMessage

load_dotenv()

PORT = "COM7"
BAUD = 115200

TEMP_LIMIT_C = 25.0  # Ändra denna för att ändra gränstemperaturen.

EMAIL_ENABLED = True

SENDER_EMAIL = os.getenv("SENDER_EMAIL")
SENDER_PASSWORD = os.getenv("SENDER_PASSWORD")
RECEIVER_EMAIL = os.getenv("RECEIVER_EMAIL")


def send_temperature_alarm(temperature, line, pc_time):
    subject = "Temperature alarm - battery CT experiment"
    body = f"""Temperature limit exceeded.

PC time: {pc_time}
Temperature: {temperature:.2f} °C
Limit: {TEMP_LIMIT_C:.2f} °C

Arduino line:
{line}

The Python logging script has stopped.
"""

    msg = EmailMessage()
    msg["From"] = SENDER_EMAIL
    msg["To"] = RECEIVER_EMAIL
    msg["Subject"] = subject
    msg.set_content(body)

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(SENDER_EMAIL, SENDER_PASSWORD)
        server.send_message(msg)


def extract_temperature(line):
    match = re.search(r"Temperature \[C\]:\s*([-+]?\d+(?:\.\d+)?)", line)

    if match:
        return float(match.group(1))

    return None


filename = datetime.now().strftime("temperature_log_%Y-%m-%d_%H-%M-%S.csv")

with serial.Serial(PORT, BAUD, timeout=2) as ser, open(filename, "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["pc_timestamp", "arduino_line", "temperature_C", "alarm"])

    print(f"Logging from {PORT} to {filename}")
    print(f"Temperature limit: {TEMP_LIMIT_C:.2f} °C")
    print("Press Ctrl+C to stop manually.")

    time.sleep(2)

    try:
        while True:
            line = ser.readline().decode("utf-8", errors="replace").strip()

            if line:
                pc_time = datetime.now().strftime("%Y-%m-%d | %H:%M:%S.%f")[:-3]
                temperature = extract_temperature(line)

                alarm = ""

                if temperature is not None and temperature >= TEMP_LIMIT_C:
                    alarm = "TEMPERATURE_LIMIT_EXCEEDED"

                    writer.writerow([pc_time, line, temperature, alarm])
                    file.flush()

                    print(f"{pc_time} | {line} | ALARM: temperature limit exceeded")

                    if EMAIL_ENABLED:
                        try:
                            send_temperature_alarm(temperature, line, pc_time)
                            print("Alarm email sent.")
                        except Exception as e:
                            print(f"Failed to send alarm email: {e}")

                    print("Measurement stopped because temperature limit was exceeded.")
                    break

                writer.writerow([pc_time, line, temperature, alarm])
                file.flush()

                print(f"{pc_time} | {line}")

    except KeyboardInterrupt:
        print("\nLogging stopped manually.")