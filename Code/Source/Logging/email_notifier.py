from __future__ import annotations

import os
import smtplib
import ssl
from dataclasses import dataclass
from datetime import datetime
from email.message import EmailMessage
from pathlib import Path
from typing import Mapping

@dataclass(frozen=True)
class EmailSettings:
    smtp_server: str
    smtp_port: int
    sender_email: str
    sender_password: str
    recipient_email: str
    subject_prefix: str = "Battery CT experiment alert!"
    timeout_s: float = 10.0


def read_env_file(env_path: str | Path) -> dict[str, str]:
    """
    Reads a simple .env-style file.

    Supported format:
        KEY = value

    Empty lines and lines starting with # are ignored. 
    """
    env_path = Path(env_path)

    if not env_path.exists():
        raise FileNotFoundError(f"Could not find email settings file: {env_path}")
    
    values: dict[str, str] = {}

    for raw_line in env_path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()

        if not line:
            continue

        if line.startswith("#"):
            continue

        if "=" not in line:
            continue

        key, value = line.split("=", 1)
        key = key.strip()
        value = value.strip().strip('"').strip("'")

        if key:
            values[key] = value

    return values

def get_first_value(
    values: Mapping[str, str],
    *keys: str,
    default: str | None = None,       
) -> str | None:
    for key in keys:
        value = values.get(key)

        if value is not None and value.strip() != "":
            return value.strip()
        
    return default

def load_email_settings(env_path: str | Path) -> EmailSettings:
    """
    Loads email settings from an env. file.

    Expected keys:
        SMTP_SERVER = smtp.gmail.com
        SMTP_PORT = 465
        EMAIL_SENDER = your_email@gmail.com
        EMAIL_PASSWORD = your_app_password
        EMAIL_RECIPIENT = recipient_email@example.com

    Optional:
        EMAIL_SUBJECT_PREFIX = Battery CT Experiment alert!
    """
    values = dict(os.environ)
    values.update(read_env_file(env_path))

    smtp_server = get_first_value(
        values,
        "SMTP_SERVER",
        default="smtp.gmail.com",
    )

    smtp_port_text = get_first_value(
        values,
        "SMTP_PORT",
        default="465",
    )

    sender_email = get_first_value(
        values,
        "EMAIL_SENDER",
        "SENDER_EMAIL",
        "EMAIL_ADDRESS",
    )

    sender_password = get_first_value(
        values,
        "EMAIL_PASSWORD",
        "SENDER_PASSWORD",
        "APP_PASSWORD",
    )

    recipient_email = get_first_value(
        values,
        "EMAIL_RECIPIENT",
        "RECIPIENT_EMAIL",
        "EMAIL_TO",
    )

    subject_prefix = get_first_value(
        values,
        "EMAIL_SUBJECT_PREFIX",
        default="Battery CT experiment alert!"
    )

    missing = []

    if sender_email is None:
        missing.append("EMAIL_SENDER")

    if sender_password is None:
        missing.append("EMAIL_PASSWORD")

    if recipient_email is None:
        missing.append("EMAIL_RECIPIENT")

    if missing:
        raise ValueError(
            "Missing required email setting(s): " + ", ".join(missing)
        )
    
    return EmailSettings(
        smtp_server=str(smtp_server),
        smtp_port=int(str(smtp_port_text)),
        sender_email=str(sender_email),
        sender_password=str(sender_password),
        recipient_email=str(recipient_email),
        subject_prefix=str(subject_prefix),
    )

def send_email(
        email_settings: EmailSettings,
        subject: str,
        body: str,
) -> None:
    """
    Sends one plain-text email.
    """
    message = EmailMessage()
    message["From"] = email_settings.sender_email
    message["To"] = email_settings.recipient_email
    message["Subject"] = subject
    message.set_content(body)

    context = ssl.create_default_context()

    if email_settings.smtp_port == 465:
        with smtplib.SMTP_SSL(
            email_settings.smtp_server,
            email_settings.smtp_port,
            context=context,
            timeout=email_settings.timeout_s,
        ) as server:
            server.login(
                email_settings.sender_email,
                email_settings.sender_password,
            )
            server.send_message(message)

    else:
        with smtplib.SMTP(
            email_settings.smtp_server,
            email_settings.smtp_port,
            timeout=email_settings.timeout_s,
        ) as server:
            server.starttls(context=context)
            server.login(
                email_settings.sender_email,
                email_settings.sender_password,
            )
            server.send_message(message)

def send_safety_alert_email(
        email_settings: EmailSettings,
        stop_reason: str,
        details: Mapping[str, object],
) -> None:
    """
    Sends an email when the experiment is stopped by a safety condition.
    """
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    subject = f"{email_settings.subject_prefix}"

    lines = [
        "Battery CT experiment safety alert!",
        "==================================",
        "",
        f"Time: {now}",
        f"Stop reason: {stop_reason}",
        "",
        "Latest experiment values:"
    ]

    for key, value in details.items():
        lines.append(f"- {key}: {value}")

    lines.append("")
    lines.append("The experiment control code has detected a safety stop condition")

    body = "\n".join(lines)

    send_email(
        email_settings=email_settings,
        subject=subject,
        body=body
    )