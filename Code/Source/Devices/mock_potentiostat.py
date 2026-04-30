class MockPotentiostat: # Creates a class.
    def __init__(self): # Init is used here as a startfunction to set the starting values.
        self.voltage = 3.7 # Creates a variable belonging to the object.
        self.current = 0.0 # Sets the start current to 0.
        self.mode = "idle" # Start mode, meaning it does nothing.
    
    def connect(self): # Defines the method connect.
        print("MockPotentiostat connected.") # Whats printed when connect() is used.

    def start_charge(self, current_mA, voltage_limit): # The method that starts the charging. It uses two values.
        self.current = current_mA
        self.mode = "charging" # Changes from "idle" to "charging".
        print(f"Charging started: {current_mA} mA, limit {voltage_limit} V.") # f means a string.

    def stop(self): # The method that stops the potentiostat.
        self.current = 0.0
        self.mode = "idle" # Changes from "charging" to "idle".
        print("Potentiostat stopped.")
    
    def read_voltage(self): # The method that reads the voltage.
        if self.mode == "charging": # If it's in mode "charging", the voltage is raised with 0,01 V.
            self.voltage += 0.01
        return self.voltage # Sends the value to the variable voltage.
    
    def read_current(self):
        return self.current # Sends the value to the variable current.