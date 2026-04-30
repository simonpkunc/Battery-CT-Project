# Image quality in my CT System
## What determines image quality
In my micro-CT system (Nikon XT H 225 ST 2x), image quality is mainly determined by
- noise.
- spatial resolution.
- detector resolution.
- detector properties.
- system geometry.
- reconstruction.

These factors directly affect wether small structural changes (such as swelling) can be detected and measured.

## 1) Noise
Noise is random variation in the measured signal.

### Effects
- reduces contrast between regions.
- makes segmentation more difficult.
- can hide small features.
- can mimic real structures.

### In my project
Noise limits the ability to detect small deformation or thickness changes. If swelling is small, it may be comparable to noise and therefore difficult to measure reliably.

## 1.1) Signal-to-noise ratio (SNR) and contrast-to-noise ratio (CNR)
- SNR describes how strong the signal is compared to noise.
- CNR describes how distinguishable two regions are relative to noise.

### Effects
- Low SNR -> noise images, unreliable measurements.
- Low CNR -> difficult to separate structures.

### In my project
- Low SNR reduce accuracy in thickness and volume measurements.
- Low CNR makes segmentation of layers difficult or impossible.

Both SNR and CNR determine wether structural changes can be detected at all.

## 2) Spatial resolution
Resolution determines the smallest feature that can be distinguished. It's limited by
- X-ray source size (focal spot).
- detector blur (PSF).
- motion.
- reconstruction.

### Important distinction
- voxel size is not equal to true resolution.
- true resolution is worse than the voxel size.

### In my project
Swelling must be larger than the effective resolution to be measurable.

## 3) Point Spread Funciton (PSF)
The PSF describes how a point object appears blurred in the image.

### Effects
- edges becomes less sharp.
- boundaries become smeared.
- small features appear larger or dissapear.

### In my project
PSF limits how precisely I can measure
- thickness.
- boundaries.
- small deformations.

## 4) Pixel and voxel size
- pixel = 2D detector element.
- voxel = 3D volume element.

### Effects
- sets sampling limit.
- defines smallest measurable change (in practice).

### In my project
Small changes in swelling must be larger than
- voxel size.
- effective resolution.

## 5) Artefacts
Artefacts are image distortions not representing real structure.

### Examples
- beam hardening.
- ring artefacts.
- reconstruction artfeacts.
- motion artefacts.

### Effects
- can be mistaken for real features.
- affect quantitative measurements.

### In my project
Artefacts may
- distort geometry.
- affect thickness and volume measurements.
- lead to misinterpretation.

## 6) Scan-to-scan stability
Since measurements are based on comparing multiple scans, stability between scans is critical.

### Requirements
- no movement of the sample between scans.
- consistent positioning.
- stable imaging conditions.

### Effects
- misalignment leads to incorrect measurement of deformation.
- differences between scans may be mistaken for real structural changes.

### In my project
Reliable measurement of swelling requires that differences between scans are caused by the battery, not by the measurement system. 

## 7) Contrast limitations
Contrast is determined by differences in attenuation.

### Problem
- graphite and similar materials have low contrast.
- different phases (material or components in the structure) may look similar.

### In my project
- segmentation is difficult.
- material identification is unreliable.
- measurements should rely more on geometry than material classification.

## Key insight for my project
CT image quality determines wether swelling can be measured at all. This means
- measurements are only valid if structural chnges are larget than
    - noise.
    - blur (PSF).
    - resolution limits.

Image quality directly defines the minimum detectable change. 

## Practical consequence
Reliable measurements of swelling should focus on geometry, displacement and deformation rather than exact material identification.

https://se.mathworks.com/help/images/image-quality-metrics.html