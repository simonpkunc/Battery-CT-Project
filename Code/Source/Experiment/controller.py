class ExperimentController:
    def __init__(self, potentiostat, temp_sensor, safety, logger, config):
        self.potentiostat = potentiostat
        self.temp_sensor = temp_sensor
        self.safety = safety
        self.logger = logger
        self.config = config

    def run(self):
        print("Experiment started.")

        charge_current = self.config["experiment"]["charge_current_mA"]
        voltage_limit = self.config["experiment"]["voltage_limit_V"]
        num_steps = self.config["experiment"]["num_steps"]

        self.potentiostat.connect()
        self.temp_sensor.connect()
        
        self.potentiostat.start_charge(current_mA = charge_current, voltage_limit = voltage_limit)

        for i in range(num_steps):
            voltage = self.potentiostat.read_voltage()
            current = self.potentiostat.read_current()
            temperature = self.temp_sensor.read_temperature()

            print(f"Voltage: {voltage:.2f} V | Current: {current} mA | Temperature: {temperature} °C")
        
            self.logger.log_data(voltage, current, temperature)

            if not self.safety.check_temperature(temperature):
                print("Stopping experiment due to safety limit.")
                self.logger.log_data(voltage, current, temperature, status = "STOPPED", message = "Temperature exceeded safety limit.")
                break

        self.potentiostat.stop()
        print("Experiment finished.")