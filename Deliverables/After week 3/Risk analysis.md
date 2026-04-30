# Risk analysis - In-situ CT battery experiment
## 1) Purpose
The purpose of this document is to identify and analyze risks associated with performing **in-situ X-ray CT measurements of a battery during charging and discharging**.

The goal is not to be complete, but to
- identify the most critical risks early.
- understand how they are detected.
- define how the system should respond.

## 2) System overview
The system consists of
- X-ray CT scanner (Nikon XT H 225 ST 2x).
- rotating stage with battery holder.
- battery under test.
- potentiostat (BioLogic SP-50).
- Sensors
    - force/pressure.
    - temperature.
- experimental control computer (controls potentiostat and logs sensor data).
- CT control computer (controls scan and image aquisition).

## 3) Risk analysis method
For each risk, the following is defined
- what can happen?
- how is it detected?
- What does the system do?

## 4) Identified risks
### 4.1) Overheating of the battery
**What can happen?**
- temperature increases during charging/discharging (most likely just under charging).
- worst case scenario -> thermal runaway.
- damage to the battery, the holder and/or the CT scan.

**How is it detected?**
- by the temperature sensors on or near the battery.
- real-time monitoring via experimental control computer (via the simple dashborad mentioned in the project description?).

**What does the system do?**
- stop charging/discharging via potentiostat (this should be done via the code in Python).
- abort experiment if temperature exceeds threshold temperature (this should be done via the code in Python).
- define temperature limit (e.g. ± 2°C from baseline or absolute limit).

### 4.2 Overcharging/overvoltage
**What can happen?**
- battery voltage exceeds safe limits.
- internal damage (not swelling which is to be expected).

**How is it detected?**
- voltage monitoring in potentiostat.

**What does the system do?**
- the potentiostat enforces voltage limits.
- automatically stops charging if limits are exceeded.
- define safe voltage window (e.g. 2,5 - 4,1 V).

### 4.3) Short circuit
**What can happen?**
- incorrect wiring or contact failure inside the battery.
- rapid current increase -> heating.

**How is it detected?**
- sudden current spike in the potentiostat.
- unexpected voltage drop.

**What does the system do?**
- immediate shutdown via potentiostat (this should be done via the code in Python).
- manual inspection required before start.

### 4.4) Mechanical instability during rotation
**What can happen?**
- battery or holder moves during rotation causing motion artefacts in CT images.
- risk of collision inside the scanner.

**How is it detected?**
- visual inspection before the scan.
- irragularities in CT images.

**CAN'T THINK OF ANYTHING BETTER HERE AND ALSO NOTHING THAT MAKES THE CODE SEND A WARNING MESSAGE**.

**What does the system do?**
- ensure rigid mounting of the holder.
- balance the system before rotation.
- stop scan if instability is observed.

### 4.5) Cable interference with rotating stage
**What can happen?**
- the cables twists, stretches or brakes.
- traction (dragning) forces applied on the battery.
- damage to the equipment.

**How is it detected?**
- visual inspection.
- increasing mechanical resistance during rotation (also by visual inspection).

**What does the system do?**
- careful cable routing.
- use flexible cables.
- limit rotation range if necessary.

**CAN'T THINK OF ANYTHING BETTER HERE AND ALSO NOTHING THAT MAKES THE CODE SEND A WARNING MESSAGE**.
**HOW MUCH DOES THE STAGE HAVE TO ROTATE?**.

### 4.6) Sensor failure (temperature/force/pressure)
**What can happen?**
- sensor gives incorrect or no data.
- unsafe conditions go undetected.

**How is it detected?**
- unreasonable or constant sensor readings.
- signal loss.

**What does the system do?**
- abort experiment if critical sensor fails (this should be done via the code in Python).
- validate signals before starting experiment.

### 4.7) CT environment constraints
**What can happen?**
- materials interfere with X-ray imaging.
- metal parts create artifacts.
- equipment not compatible with CT environment.

**How is it detected?**
- image artefacts.
- prior knowledge/material selection.

**What does the system do?**
- use CT-compatible materials (e.g. polymers).
- minimize metal near imaging region.

### 4.8) Data synchronization issues
**What can happen?**
- sensor data and CT images are not aligned in time.
- difficult or invalid analysis.

**How is it detected?**
- inconsistent timestamps.
- mismatch bewteen events and images.

**What does the system do?**
- use consistent time reference (all the systems must use the same "clock" every time).
- log timestamps for all data streams.
- define clear experiment sequence (charge -> pause -> scan -> resume).

## 5) Preliminary safety limits
**THESE VALUES ARE INITIAL ESTIMATES AND MUST BE REFINED!**
- temperature limit: to be determined (e.g. max 40 - 60 °C depending on battery).
- voltage window: e.g. 2,5 - 4,1 V.
- current limits: defined in potentiostat setting (?).

## 6) Summary
The most critical risks are
- overheating.
- overcharging.
- cable interaction with rotation.
- mechanical instability.

These risks will directly influence
- holder design.
- sensor placement.
- cable routing.
- control logic.