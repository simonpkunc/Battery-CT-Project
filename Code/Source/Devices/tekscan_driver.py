import time
from dataclasses import dataclass


@dataclass
class TekscanDriver:
    """
    Basic automation driver for Tekscan I-Scan.

    This driver does not read pressure data directly.
    It only sends keyboard commands to I-Scan.

    Expected I-Scan setup before use:
    - I-Scan is open.
    - The correct sensor/map is selected.
    - A New Recording / real-time window is open.
    - The real-time window is active, or can be found by window title.
    - F2 starts recording.
    - F4 stops recording.
    """

    window_title_keywords: tuple[str, ...] = (
        "I-Scan",
        "IScan",
        "Tekscan",
        "TekScan",
    )

    activate_window_before_command: bool = True
    activation_delay_s: float = 0.5
    key_delay_s: float = 0.2

    start_key: str = "f2"
    stop_key: str = "f4"

    def start_recording(self) -> None:
        """
        Start I-Scan recording by sending F2.
        """
        self._send_key_to_iscan(self.start_key)

    def stop_recording(self) -> None:
        """
        Stop I-Scan recording by sending F4.
        """
        self._send_key_to_iscan(self.stop_key)

    def _send_key_to_iscan(self, key: str) -> None:
        """
        Activate I-Scan if possible and send one keyboard key.
        """
        pyautogui = self._require_pyautogui()

        if self.activate_window_before_command:
            self._activate_iscan_window_if_possible()

        pyautogui.press(key)
        time.sleep(self.key_delay_s)

    def _activate_iscan_window_if_possible(self) -> bool:
        """
        Try to activate the I-Scan window.

        Returns True if a matching window was found and activation was attempted.
        Returns False if pygetwindow is unavailable or if no matching window is found.

        This function is intentionally non-critical. The experiment should still be
        able to run if the user has already made the correct I-Scan window active.
        """
        try:
            import pygetwindow as gw
        except ImportError:
            return False

        try:
            windows = gw.getAllWindows()
        except Exception:
            return False

        for window in windows:
            title = window.title or ""

            if self._title_matches_iscan(title):
                try:
                    if window.isMinimized:
                        window.restore()

                    window.activate()
                    time.sleep(self.activation_delay_s)
                    return True

                except Exception:
                    return False

        return False

    def _title_matches_iscan(self, title: str) -> bool:
        """
        Check whether a window title looks like an I-Scan/Tekscan window.
        """
        title_lower = title.lower()

        for keyword in self.window_title_keywords:
            if keyword.lower() in title_lower:
                return True

        return False

    @staticmethod
    def _require_pyautogui():
        """
        Import pyautogui only when a keyboard command is actually needed.
        """
        try:
            import pyautogui
        except ImportError as exc:
            raise RuntimeError(
                "pyautogui is required to control Tekscan I-Scan. "
                "Install it with: pip install pyautogui"
            ) from exc

        return pyautogui