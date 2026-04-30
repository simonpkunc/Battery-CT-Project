import random

class MockTemperatureSensor:
    def __init__(self):
        self.temperature = 25.0 # Start temperature in celsius.

    def connect(self):
        print("MockTemperatureSensor connected.")

    def read_temperature(self): # Simulate small variations.
        self.temperature += random.uniform(-0.1, 0.2)
        return self.temperature