import os
import yaml

from Source.Devices.mock_potentiostat import MockPotentiostat
from Source.Devices.mock_temp_sensor import MockTemperatureSensor
from Source.Safety.monitor import SafetyMonitor
from Source.Logging.data_logger import Datalogger
from Source.Experiment.controller import ExperimentController

def load_config(filepath):
    with open(filepath, "r") as file:
        return yaml.safe_load(file)
    
def main():
    print("Battery CT project started.")

    base_dir = os.path.dirname(__file__)
    config_path = os.path.join(base_dir, "Configuration", "experiment_config.yaml")
    config = load_config(config_path)

    max_temperature = config["safety"]["max_temperature_C"]

    potentiostat = MockPotentiostat()
    temp_sensor = MockTemperatureSensor()
    safety = SafetyMonitor(max_temperature = max_temperature)
    logger = Datalogger()

    controller = ExperimentController(potentiostat = potentiostat, temp_sensor = temp_sensor, safety = safety, logger = logger, config = config)

    controller.run()

if __name__ == "__main__":
    main()