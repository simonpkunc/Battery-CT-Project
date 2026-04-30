# Measurable quantities
## Purpose
To define what is actually measurable in this project using X-ray CT and clarify the link between physical battery processes and observable quantities.

## What is "swelling" in this project?
Swelling refers to **structural expansion of the battery during operation**, caused by
- lithiation/delithiation of electrode materials.
- possible gas formation (typically minor under normal operation conditions).

In this project, swelling is interpreted as **geometric changes in the internal structure of the battery over time**.

CT does **NOT** measure
- lithium concentration directly.
- chemical reactions.

CT **DOES** measure
- changes in geometry and structure.

## Measurable quantities
### 1) Thickness
#### Definition
Change in thickness over time of
- entire cell.
- individual layers (**if resolvable**).

#### How CT measures it
- distance between boundaries in reconstructed 3D images.
- can be extracted from cross-sections or full volume.

#### What it represents physically
- electrode expansion due to lithiation.
- separator compression or expansion.

#### Limitations
- limited spatial resolution (voxel size).
- difficult if layer contrast is low.
- segmentation uncertainty.

### 2) Volume change
#### Definition
Change in total volume or volume of specific regions over time.

#### How CT measures it
- segmentation of 3D volume.
- comparison between time steps (before vs after or time series).

#### What it represents physically
- overall swelling of the cell.
- expansion of electrode materials.

#### Limitations
- requires reliable segmentation.
- sensitive to noise and thresholding.
- small changes may be difficult to detect.

### 3) Strain (via DVC)
#### Definition
Local deformation field inside the battery
- how much regions move relative to each other.

#### How CT measures it
- Digital Volume Correlation (DVC)
    - comparison of voxel patterns between two states (e.g. before and after cycling).
- tracks patterns in grayscale images between scans.

#### What it represents physically
- local expansion/contraction.
- heterogeneous swelling behaviour.

#### Limitations
- requires high image quality.
- computationally demanding.
- sensitive to noise and contrast.

## Direct vs indirect
### Directly measurable with CT
- geometry.
- thickness.
- volume.
- structural deformation.

### Indirectly inferred
- strain (via DVC).
- internal stresses (not directly measured).
- electrochemical activity (inferred from deformation).

### Not measurable with CT
- lithium concentration.
- electrochemical reactions.
- temperature (without external sensors).

## Minimum detectable change (estimate)
The smallest measurable change is limited by resolution
- voxel size (~ 1 um for this system).
- practical detection limit (~ 2-5 x voxel size).

Estimated
- thickness change > 2-5 um.
- smaller changes may be unreliable.

## Important note
Although the camera pixel size is ~ 1 um, the **effective resolution** is influenced by
- system optics.
- X-ray spot size.
- noise.
- reconstruction quality.

This means that the true detectable change is typically larger than the nominal pixel size.

## What is realistically measurable in this project (Nikon XT H 225)
### Likely feasible
- global thickness change of the cell.
- overall volume change.
- large structural deformation.

### Possibly feasible
- layer thickness (if contrast is sufficient).
- coarse strain fields.

### Likely difficult
- fine strain mapping.
- small local changes.
- weakly attenuating materials (e.g. graphite).

## Link to literature
### Maire et al.
- CT enables **quantitative 3D measurements**.
- suitable for volume, structure and damage analysis.

### Pietsch et al.
- strain can be measured using DVC.
- contrast limitations are important (especially for graphite).

### Finegan et al.
- CT captures **dynamic structural changes**.
- demonstrates what types of deformation are visible.

## Key takeaway
CT does not measure battery chemistry directly, but instead captures **structural and geometric changes over time**. Swelling in this project is defined and quantified as **changes in thickness, volume and internal deformation of the battery structure**. These quantities provide a measurable link between electrochemical processess and observable structural evolution.

In this project, with CT I will be able to directly measure
- geometry.
- thickness.
- volume.
- structural deformation.

In other words, this will be visible on the images after the imageanalysis. CT only provides raw data. However, I will also be able to measure (though indirectly with the help of some calculations)
- strain (DVC).
- internal stresses (estimated from the strain using material models and and assumptions such as Young's modulus).

## Important interpretation notes
- CT provides structural data, not direct physical measurements.
- All quantities are derived from image analysis (segmentation, DVC etc.)
- Measurements represent changes over time, not absolute values.
- Detectability is limited by spatial resolution (~ 2-5 um).
- Some quantities (e.g. stress) are not measured directly, but inferred from models and assumptions.
- CT provides raw volumetric data; all physical interpretation depends on post-processing and analysis.

## Implications for system design
Based on the measurable quantities and limitations
- the system must be able to detect changes > 2-5 um.
- high image quality is required -> stable setup and low noise.
- multiple scans are required -> the system must support repeated measurements over time.
- image analysis (segmentation, DVC) is essential -> data processing pipeline must be considered.
- measurements are relative -> alignment between scans are important.

Therefore, the system must:
- allow controlled cycling of the battery.
- ensure mechanical stability during scans.
- enable synchronization between electrochemistry and CT scanning.