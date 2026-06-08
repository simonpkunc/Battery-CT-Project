**THIS IS TO BE UPDATED!**
# Battery-CT-Project

## Overview
This thesis project aims to design, build and validate an experimental system for measuring swelling in lithium-ion batteries during electrochemcical cycling using micro-CT (computed tomography).

The system integrates
- a battery holder compatible with CT imaging.
- potentiostat for charge/discharge control.
- sensors for temperature (and potentially force).
- a Python-based control and data aquisition system.

## Current status
The project is currently focused on
- developing a modular software platform for experiment control.
- designing a battery holder with controlled mechanical constraint (to capture both swelling and force response).
- preparing for integration with real hardware (potentiostat, sensors, CT system)

Due to limited access to hardware (CT scanner and potentiostat), development is currently performed using simulated (mock) devices.

## Repository structure
Battery CT project
| 
|--> Cells                       # Documentation for each cell.
|--> Code/ \                      
|    |--> Configuration/         # YAML configuration-files for experiment.
|    |--> Data/                  # Logged experiment data (CSV-format).
|    |--> Source/              
|    |     |--> Devices/         # Mock and future real hardware interfaces.
|    |     |--> Experiment/      # Experiment controller logic.
|    |     |--> Logging/         # Data logging system.
|    |     |--> Safety/          # Safety monitoring (temperature etc.).
|    |--> Tests/                 # Basic testing scripts.
|    |--> main.py/               # Entry point.
| 
|--> Deliverables/               # Project outputs for each timeline.
|--> Holder/                     # Mechanical design (concepts for the holder).
|--> Logbook/                    # Daily/weekly progress (just for myself).
|--> Notes/                      # Technical notes and understanding.
|--> Papers/                     # Literature and other useful documents.
|--> .gitignore
|--> Experimental etup.md        # How everything will ce connected during the experiment.
|--> README.md/                  # Presentation of the project.