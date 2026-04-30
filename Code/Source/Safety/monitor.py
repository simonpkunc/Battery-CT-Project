class SafetyMonitor:
    def __init__(self, max_temperature):
        self.max_temperature = max_temperature

    def check_temperature(self, temperature):
        if temperature > self.max_temperature:
            print("WARNING: Temperature too high!")
            return False
        return True