# Requirements specification - In-situ CT battery experiment
## Purpose
The purpose of this document is to define the requirements for an experimental setup that enables **in-situ X-ray CT imaging of a battery during electrchamical cycling**, i.e. what I will build (CT environment excluded). The requirements are based on
- system design.
- risk analysis.
- measurement goals.

### 1) System overview
The system shall enable
- X-ray CT imaging of a battery.
- controlled charging and discharging using a potentiostat.
- measurement of temperature and mechanical response (force/pressure).
- synchronized data aquisition.

### 2) Functional requirements
- the system shall allow **electrochemical cycling** of the battery (charge/discharge).
- the system shall allow **pausing the cycling** during CT scanning.
- the system shall enable **in-situ CT imaging** of the battery.
- the system shall support a defined experiment sequence
    - charge -> paus until stable conditions -> scan -> resume.
- the system shall allow **real-time monitoring** of
    - voltage.
    - current.
    - temperature.
    - force/pressure.

### 3) Measurement requirements
- the system shall measure **temperature** at or near the battery.
- the system shall measure **force or pressure** applied to the battery.
- the system shall log
    - voltage.
    - current.
    - temperature.
    - force/pressure.
- all measurements shall include **timestamps**.
- all data streams shall use a **common time reference**.
- the system shall allow correlation between CT images and measurement data.

### 4) Mechanical requirements
- the battery shall be **rigidly fixed** in the holder.
- the holder shall prevent **relative motion** between battery and holder.
- the holder shall be **stable during rotation**.
- the system shall be **balanced** to avoid vibrations during rotation.
- the holder shall be compatible with **CT imaging**.
    - minimal X-ray attenuation.
    - minimal imaging artefacts.
- cables shall be routed such that they
    - do not apply torque to the stage during rotation.
    - do not interfere with rotation.
- the holder shall fit within the **CT scanner geometry constraints**.

### 5) Electrical requirements
- the system shall allow electrical connection to
    - positive electrode.
    - negative electrode.
- the potentiostat shall controll
    - voltage.
    - current.
- the system shall ensure **stable electrical contact** during rotation.
- wiring shall not interfere with
    - mechanical stability.
    - CT imaging.

### 6) Safety requirements
- the system shall stop cycling if temperature exceeds a defined threshold.
- the system shall enforce voltage limits (e.g. 2,5 - 4,1 V).
- the system shall detect abnormal current behavior (e.g. short circuit between layers).
- the system shall allow manual abort of the experiment.
- the system shall prevent
    - cable damage.
    - michanical collision inside the CT scanner.
- the system shall operate safely within the **CT environment**.

Necessary points above should be alerted to the user via email.

### 7) Data and control requirements
- the system shall log all experimental data to a **single control computer**.
- the system shall stora data in a structured format.
- the system shall allow synchronization between
    - CT scan events.
    - electrochemical cycling.
    - sensor measurements.
- the system shall allow basic control of
    - charging/discharging.
    - experiment timing.

### 8) Constraints related to the CT environment
- the system must be compatible with
    - Nikon XT H 225 ST 2x.
- the experimental setup must fit within the available space in the CT scanner.
- materials used must be compatible with X-ray imaging.
- the setup must allow rotation of the sample.

### 9) Summary
This requirement specification defines the minimum functionality needed to
- perform in-situ CT imaging.
- control electrochemical cycling.
- measure key physical parameters.
- ensure safe and stable operation.