# This subfolder contains all hardware-related classes. Each device is represented as a class, e.g.

* Potentiostat.
* Temperature sensor.
* Force sensor.
* CT Scanner.

## Potentiostat interface
All potentiostat implementations must provide

- connect().
- start_charge(current_mA, voltage_limit).
- stop().
- read_voltage().
- read_current().

## Temperature interface

- connect().
- read_temperature().