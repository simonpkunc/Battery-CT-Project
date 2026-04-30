import csv # Makes so that Python can create CSV-files.
import os # Used to create and manage searchways/maps.

base_dir = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
data_dir = os.path.join(base_dir, "Data")

os.makedirs(data_dir, exist_ok = True)

from datetime import datetime # For the timestamp.

class Datalogger: # Creates the loggerclass.
    def __init__(self, filename = "experiment_log.csv"):
        timestamp = datetime.now().strftime("date [%Y-%m-%d] & time [%H-%M-%S]")
        self.filename = f"Experiment log for cell #, {timestamp}.csv"
        self.filepath = os.path.join("Code", "Data", self.filename)

        os.makedirs("Code/Data", exist_ok = True)
        # When the log is created, it sets the filename, creates the searchway, creates the map "Data" if it does not already exist and creates the CSV-file.

        with open(self.filepath, mode = "w", newline = "") as file:
            writer = csv.writer(file)
            writer.writerow(["Timestamp", "Voltage [V]", "Current [mA]", "Temperature [C]", "Status", "Message"])

    def log_data(self, voltage, current, temperature, status = "Running", message = ""):
        timestamp = datetime.now().isoformat()

        with open(self.filepath, mode = "a", newline = "") as file:
            writer = csv.writer(file)
            writer.writerow([timestamp, voltage, current, temperature, status, message])
            # Every time this method is called, a timestamp is created and a new row is added to the CSV-file.