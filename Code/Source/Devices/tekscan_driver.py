import subprocess
import time

class TekscanDriver:
    """
    Simple Tekscan I-Scan controller.

    This does not read force data directly.
    It activates I-Scan and sends keyboard shortcuts.

    Requirements:
    - I-Scan must already be open.
    - The correct sensor/map must be selected.
    - A New Recording / real-time window must already be open.

    Shortcuts:
    F2 = start recording
    F4 = stop recording / stop playback
    Ctrl+R = alternative start recording
    Ctrl+T = alternative stop/play-stop
    """

    def __init__(
        self,
        window_title: str = "I-Scan",
        focus_delay_s: float = 1.0,
    ):
        self.window_title = window_title
        self.focus_delay_s = focus_delay_s

    def _send_key_with_powershell(self, key: str) -> None:
        delay_ms = int(self.focus_delay_s * 1000)

        command = f"""
$wshell = New-Object -ComObject WScript.Shell

$proc = Get-Process | Where-Object {{
    $_.ProcessName -like 'iscan*'
}} | Select-Object -First 1

if ($proc -ne $null) {{
    $success = $wshell.AppActivate($proc.Id)
}} else {{
    $success = $wshell.AppActivate('{self.window_title}')
}}

Start-Sleep -Milliseconds {delay_ms}

if (-not $success) {{
    Write-Output 'Could not activate I-Scan window.'
    exit 2
}}

$wshell.SendKeys('{key}')
Start-Sleep -Milliseconds 300
"""
        result = subprocess.run(
            [
                "powershell",
                "-NoProfile",
                "-ExecutionPolicy",
                "Bypass",
                "-Command",
                command,
            ],
            capture_output=True,
            text=True,
        )

        if result.stdout.strip():
            print(result.stdout.strip())

        if result.stderr.strip():
            print(result.stderr.strip())

        if result.returncode != 0:
            raise RuntimeError(
                f"Failed to send key {key} to I-Scan. "
                f"PowerShell return code: {result.returncode}"
            )

        time.sleep(0.3)

    def start_recording(self) -> None:
        print("Starting Tekscan recording with F2...")
        self._send_key_with_powershell("{F2}")

    def stop_recording(self) -> None:
        print("Stopping Tekscan recording with robust stop sequence...")

        # Important when IviumSoft was just clicked manually.
        time.sleep(1.2)

        stop_keys = [
            "{F4}",
            "{F4}",
            "^t",
            "{F4}",
        ]

        for key in stop_keys:
            print(f"Sending Tekscan stop key: {key}")
            self._send_key_with_powershell(key)
            time.sleep(0.6)

        print("Tekscan stop sequence finished.")

    def take_snapshot(self) -> None:
        print("Taking Tekscan snapshot with F3...")
        self._send_key_with_powershell("{F3}")