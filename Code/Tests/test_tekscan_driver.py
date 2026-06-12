import sys
import time
from pathlib import Path

# Add Code/ folder to Python path so imports work when running from Tests/
code_folder = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(code_folder))

from Source.Devices.tekscan_driver import TekscanDriver

def main() -> None:
    print("Tekscan driver test")
    print("===================")
    print()
    print("Before running this test:")
    print("- Open I-Scan manually")
    print("- Load the correct sensor/map")
    print("- Make sure the realtime window is ready")
    print("- Make sure F2 and F4 work manually")
    print()

    input("Press Enter to start Tekscan recording with F2...")

    tekscan = TekscanDriver()

    tekscan.start_recording()

    print("Recording for 5 seconds...")
    time.sleep(5)

    tekscan.stop_recording()

    print("Tekscan recording stopped.")
    print("Test finished.")

if __name__ == "__main__":
    main()