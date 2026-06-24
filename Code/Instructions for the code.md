## Instructions for the code
This document describes the strucuture and purpouse of the code and how it is supposed to be used. The code is used to run battery cycling experiments with simultaneous potentiostat control, temperature monitoring, Tekscan pressure recording, data logging, safety features and remote status updates. It consists of one main script and several supporting modules, each communicating with different components.

**Required software before running the code**
- IviumSoft.
- I-Scan.
- Arduino IDE.

**Required components before running the code**
- Ivium potentiostat (CompactStat2.h).
- Tekscan pressure sensor (5051 or 5101) and Tekscan Evolution Handle.
- Arduino Nano ESP32.
- MAX31865 PT100 RTD Temperature Sensor Amplifier.
- PT100 sensor.

**Required wiring**

**Structure**\
The folder *Code/* contains the Python code, configuration files and generated output folders.

*Code/*\
├── Configuration/\
├── Data/\
├── Source/\
├── Instructions for the code.md\
├── main.py

**main.py**\
This is the main entry point for running an experiment. It is responsible for:
- asking the user for experiment settings.
- defining the charge, rest and discharge tasks.
- defining the number of cycles.
- setting safet limits.
- choosing whether Tekscan recording should be used or not.
- creating file paths for logs and generated methods.
- printing an experiment summary.
- starting the main experiment function.

The actual experiment loop is not written directly in *main.py*. Instead, *main.py* creates an *ExperimentSettings* object and passes it to *run_battery_experiment(...)* in *Source/Experiment/cycling_experiment.py*. This keeps the *main.py* as the user-facing setup script, while the detailed experiment logic is kept in the folder *Source/Experiment/*.

**Configuration**\
This folder contains files that define or support experiment configuration. It is intended for files that are needed before an experiment starts, such as Ivium method templates.

*Configuration/*\
├── ivium_cycle_template.imf

The most important file is *ivium_cycling_template.imf* which is used as a template when generating an Ivium method file for the requested charge/rest/discharge sequence. Once a method is generated, it is written to *Data/Generated_methods*.

**Data**\
This folder contains subfolders which contain outputs from an experiment.

*Data/*\
├── Generated methods/\
├── Logs/\
├── Status/

In total, there are three subfolders. *Generated methods* contains the generated Ivium method for the experiment, *Logs* contains all the data from the experiment and *Status* contains *latest_status.txt*, which can be used for remote monitoring during an experiment. Since these are generated during an experiment, they should not be pushed to GitHub.

**Source**\
This folder contains subfolders which contain the active source code used by the experiment.

*Source/*\
├── Devices/\
├── Experiment/\
├── Logging/\
├── Safety/

The source code is deivided by responsibility: 
- *Devices/* contains hardware and interface code.
- *Experiment/* contains the main experiment logic.
- *Logging/* contains status logging tools.
- *Safety/* is reserved for safety-related code and documentation.

*Source/Devices/*\
This folder contains code that communicates with external devices or software.

*Devices/*

├── emailinfo.env\
├── ivium_driver.py\
├── tekscan_driver.py\
├── tempmoni.py

*emailinfo.env* is a file containing the emailinformation for the email that recievs a warningmail if something goes wrong. This is local and should not be pushed to GitHub.

*ivium_driver.py* is the file that handles communication with  Ivium potentiostat thorugh the Ivium DLL. It is responsible for
- opening and connecting to the potentiostat.
- reading potential.
- reading current.
- reading device and cell status.
- starting an Ivium method.
- aborting an Ivium method.
- switching the cell on and off.
- generating Ivium *.imf* method files from a template.

It also defines the *IviumCycleTask* class, which is used to describe charge, discharge and rest steps.

*tempmoni.py* is the file that handles temperature monitoring through the Arduino serial communication. It is responsible for
- connecting to the Arduino over a COM port.
- reading temperature data from the seria output.
- returning the latest measured temperature to the experiment loop.

*tekscan_driver.py* handles basic automation of TekScan I-Scan recording. It is responsible for
- activating the I-Scan window.
- starting recording.
- stopping recording.
- sending keyboard shortcuts to I-Scan.

This files does not read pressure data directly. It only controls the recording state in I-scan.

*Source/Experiments/*\
This folder contains the main experiment logic.

*cycling_experiment.py* is the central experiment file. It is responsible for
- creating the genereated Ivium method file.
- starting the temperature monitor.
- starting Tekscan recording if enabled.
- starting the Ivium method.
- reading voltage and current from Ivium.
- reading temperature from the Arduino.
- checking safety limits.
- writing CSV data.
- updating the remote status file. 
- detecting manual stop requests.
- shutting down Ivium and Tekscan safely.

The active safety checks are currently implemented inside *cycling_experiment.py*. The current safety mechanisms include
- maximum voltage limit.
- minimum voltage limit.
- maximum current limit.
- minimum current limit.
- maximum temperature limit.
- manual stop using *Esc* in the terminal.
- manual abort detection from IviumSoft.
- cleanup and shutdown after stop.

The main function in this file is *run_battery_experiment(...)* where the loop continues until one of the stop conditions is reached. 

*Source/Logging/*\
This folder contains a file (*status_logger.py*) with code used for live monitoring and terminal logging. It is responsible for
- mirroring terminal output to a terminal log file.
- writing *latest_status.txt*.
- limiting how often the status file is updated so that OneDrive can sync it.
- forcing status updates at important points such as experiments start and stop.

The latest *latest_status.txt* file is intended for remote monitoring through OneDrive.

**Main workflow**
1) The user starts main.py.
2) The user enters experiment settings.
3) main.py creates the experiment settings and file paths.
4) cycling_experiment.py generates the Ivium method file.
5) The Ivium method, temperature monitor and Tekscan recording are started.
6) Voltage, current, temperature and status are logged during the experiment.
7) The experiment stops when a stop condition is reached.
8) Ivium and Tekscan are shut down safel.