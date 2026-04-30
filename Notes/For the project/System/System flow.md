System flow - CT-based battery swelling experiment
## Purpose
To define how the experiment is performed step-by-step, including how electrochemical cycling and CT scanning are combined.

## Overview
The experiment consists of repeated cycles of
- electrochemical operation (charging/discharging).
- pausing the process.
- CT scanning.
- Resuming operation.

The goal is to capture structural changes over time.

## Step-by-step process
### Step 1) Prepare cell
- insert coin cell into holder.
- ensure mechanical stability.
- connect to potentiostat (BioLogic SP-50).
- verify electrical connection.
- set temperature conditions (if applicable).

### Step 2) Initial CT-scan (reference)
- perform CT scan before cycling.
- this serves as the baseline for all measurements.

Output should be a reference 3D volume.

### Step 3) Start electrochemical cycling
- apply current or voltage (charge/discharging).
- Monitor
    - voltage.
    - current.
    - time.

### Step 4) Pause electrochemical process
- stop or hold electrochemical process.
- ensure stable state before scanning.

**IMPORTANT**
- no movement of the cell.
- stable conditions.

### Step 5) CT scan
- perform CT scan (~ 1-2 hours).
- aquire projection images.
- reconstruct into 3D volume.

Output should be time-resolved 3D dataset.

### Step 6) Resume cycling
- continue electrochemical operation.
- Repeat steps 4-6 at predefined intervals.

### Step 7) Repeat measurements
- perform multiple scans (e.g. 10-20 in total).
- each scan corresponds to a different state of the battery.

## Key parameters
### Number of scans
- limited by scan time (~ 1-2 hours per scan)
- typical is 10-20 scans per experiment.

### When to scan
- at specific states of charge (SOC).
- at defined time intervals.
- when significant changes are expected.

### Scan duration vs dynamics
- CT scans are slow compared to electrochemical processes.
- measurements represent quasi-static states.

## Synchrotronization
The system must coordinate
- potentiostat (electrochemical control).
- CT scanner (imaging).

### Requirements
- ability to pause and resume cycling.
- clear definition of scan timing.
- consistent experimental protocol.

## Sample orientation
The orientation of the coin cell relative to the X-ray beam affects
- contrast.
- visibility of layers.
- measurement accuracy.

Must be defined and kept constant throughout the experiment.

## Data flow
1) X-ray projections aqquired.
2) Reconstruction performed (Nikon system).
3) 3D volumes stored (large data, GB scale).
4) Post-processing
    - segmentation.
    - deformation analysis (DVC).
    - measurement of thickness and volume.

## Potential issues
- movement during scan -> misalignment.
- long scan time -> changes during aquisition.
- low contrast -> difficult segmentation.
- noise -> limits detectability.
- data size -> storage and processing challenges

## Key insight
The experiment is not continuous, but **intermittent**
- electrochemical process runs.
- is paused.
- CT captures a snapshot.

Measurements represent discrete states, not continuous evolution.