# System description
## 1) Overview
This project involves an experimental setup for *in-situ* (measuring while the battery is being used) X-ray computed tomography (CT) of a battery during operation. The system combines a CT scanner with an external electrochemical control system and additional sensors to monitor the battery behvaior during charging and discharging. The setup consists of two main subsystems:
- the CT system (imaging).
- the experimental system (battery, sensors and control)

## 2) CT system
The CT (Nikon XT H 225 ST 2x) system is responsible for aquiring 3D images of the battery.

### Components
- X-ray source: generates X-ray beams that pass through the battery.
- detector: captures transmitted X-ray beams and produces projection images.
- rotating stage: rotates the battery during scanning to enable 3D reconstruction.
- CT control computer: controls the scan and reconstructs images from projection data.

### Function
The X-ray source emits beams that pass through the battery. The detector records projection images at multiple angles as the rotating stage rotates the sample. These projections are reconstructed into a 3D volume by the CT computer.

## 3) Experimental setup
The experimental setup is placed inside the CT scanner and contains the battery and measurement hardware.

### Components
- battery: the sample under investigation.
- battery holder: mechanically supports the battery and is mounted on the rotating stage.
- pressure sensor: measure mechanical changes as swelling.
- temperature sensors: monitor the temperature in the battery.

### Function
The battery is held in place while rotating. Sensors continuously measure mechanical and/or thermal properties during operation.

**AD/CHANGE WHAT SENSORS ARE ACTUALLY USED AND IF SOMETHING IS UNCLEAR, WRITE IT DOWN!**.

## 4) Electrical control system
### Components
- potentiostat (Biologic SP-50).

### Function
The potentiostat controls and measures the electrochemical behavior of the battery by
- applying current or voltage (charging/discharging).
- measuring voltage and current response.

The potentiostat is connected directly to the battery terminals (positive and negative poles).

**AD A SENTENCE ABOUT HOW THE POTENTIOSTAT IS USED**.

## 5) Data aquisition and control
### Components
- experimental control computer.

### Function
This computer is responsible for
- controlling the potentiostat (charging/discharging cycles).
- logging data from
    - potentiostat (current and voltage).
    - sensors (all of them).

The experimental computer operates independently from the CT control system.

## 6) Interface and signal flow
The system consists of several interacting subsystems connected through electrical and data interfaces.

### CT system
- projection data: detector -> CT computer.
- scan control signals: CT computer -> scanner.

### Experimental system
- sensor data (force, pressure, temperature etc): sensors -> experimental data.
- control signals: experimental computer <-> potentiostat.
- electrical signals (current and voltage): potentiostat <-> battery.

## 7) Important considerations
- **Rotating and cabling**
    - the battery holder rotates during CT scanning, which impose constraints on cable routing to avoid twisting or damage.
- **Separation of systems**
    - The CT system and experimental control system operate independently but must be synchronized during experiments.
- **Measurement synchronization**
    - Data from CT and sensors should be correlated in time to enable meaningful analysis.
- **Limited space in the CT**.
- **Disturbance during imaging**.

## Summary
The system integrates imaging, electrochemical control and mechanical sensing to study battery behavior in real time. The CT system provides structural information, while the experimental system provides electrochemical and mechanical data, enabling comprehensive analysis of the battery during operation.