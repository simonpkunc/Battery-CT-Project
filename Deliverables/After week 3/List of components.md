# List of components
This is a first overview of components required for the experimental setup. The list is not final and will be refined during design and CAD development.

## 1) Mechanical components (battery holder)
- battery holder structure (what holds the battery, will be created in Solid Edge).
- mounting interface to rotating CT stage (threaded?)
- fastening mechanisms from the holder on the battery (screws, clamps (klämmor), springs, pressureplate etc.).
- support frames for sensors (what holds the sensors in place).
- alignment features to keep batery centered (slits (spår), edges etc.).

## 2) Sensors (must be able to communicate to a computer)
### Temperature measurement
- temperature sensor (e.g. thermocouple or PT100).
- sensor mounting solution.

### Force/pressure measurement
- pressure mapping sensor (tekscan).
- top constrint plate so that the sensor remains in place and starts with an even pressure (?).
- sensor positioning/fixation.

## 3) Electrical components
### Potentiostat
- BioLogic SP-50
- EC-lab software (hopefully included).

### Wiring
- electrical wires (battery connection).
- shielded cables (to reduce noise).
- connectors (what type?).

## 4) Data aquisition and control
- experimental control computer for controling potentiostat and logging data (most likely my own).
- control and data logging software (Python).

## 5) Integration in CT environment
- mount for holder on rotating stage.
- cable management system (very important due to rotation).
- strain reliefs cor cables (is this possible and necessary?).

## Safety-related components (from risk analysis)
- temperature limit (software-based).
- voltage limit (via potentiostat).
- emergency stop procedure (manual/system-level).
- mechanical stability features.

## Mental notes
Exact components will be selected later. Focus is on identifying required functionality, not specific models.
