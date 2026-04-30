# Summary JF Training Guide

## Purpose
This manual aims to **explain how to correctly set ut and optimise a CT scan** in order to obtain **high quality 3D imaging data**. The goal is to understand how **X-ray physics, sample positioning and scan parameters interact** and how these can be tuned to balance
* resolution.
* contrast.
* noise.
* penetration.

## Method
The manual describes a **practical workflow for CT scanning**, based on
* X-ray physics fundamentals (attenuation, scattering, beam hardening etc).
* iterative parameter tuning (kV, current, power, exposure etc).
* sample positioning strategies.

Instead of a fixed setup, the method is **iterative**.
1) Choose initial scan parameters.
2) Evaluate image quality (penetration, contrast, noise etc.).
3) Adjust parameters.
4) Repeat untill optimal conditions are reached.

## Key observations
### 1) CT imaging is based on X-ray attenuation
- CT images are essentially **2D X-ray projections from multiple angles**.
- contrast arises from **differences in attenuation** between materials.

### 2) There is a fundamental trade-off between image quality factors
- higher power -> more signal, less noise but more blur (larger focal spot).
- higher energy (kV) -> better penetration but lower contrast.
- longer exposure -> less noise but longer scan time. 

### 3) Beam hardening is a major source of artefacts
- low-energy X-rays are absorbed first.
- reamining beam becomes "harder".
- leads to non-uniform grey values and edge artefacts.

This can be reduced by adding **beam filtration (e.g. Cu filters)** or applying **software correction**.

### 4) Sample positioning strongly affects image quality
- horizontal flat surfaces -> cone beam artefacts.
- large thickness variations -> poor penetration.

Optimal positioning
- tilt the sample (~ 45°).
- minimise long path lengths.
- avoid parallell surfaces.

### 5) Penetration must be sufficient across the entire sample
The darkest region in the image must satisfy
- darkest pathlength > 1,5 x detector baseline.

If not, increase energy and/or adjust filtration.

### 6) Resolution is not only determined by voxel size
True resolution depends on
- voxel size.
- focal spot size.
- geometric magnification.

Key rule: **Focal spot size ≈ effective pixel size -> minimal blur**.

### 7) Noise is controlled by X-ray flux and aquisition time
Noice can be decreased by
- increasing power.
- increasing exposure time.
- averaging multiple frames.

Trade-offs are longer scan time and potential loss of sharpness.

## Key insights
**CT optimisation is a balancing problem**
- no single "best" setting exists.
- all parameters interact and must be tuned together.

**Sample positioning is as important as scan parameters**
- poor positioning -> artefacts that cannot be fixed later.
- good positioning -> improved penetration and image quality.

**Penetration and contrast must be balanced**
- too little penetration -> noice and artefacts.
- too much penetration -> loss of contrast.

**Beam filtration improves data quality**
- removes low-energy X-rays.
- reduces artefacts.
- improves consistency in grey values.

## Relevance for my project
### 1) Direct link between holder design and CT quality.
This manual shows that **sample positioning is critical** for
- reducing artefacts.
- improving penetration.
- achieving uniform image quality.

This directly impacts how the holder should be designed.

### 2) Importance of sample orientation
Tilting the sample
- reduces cone beam artefacts.
- improves image quality.

This supports designing a holder that
- allows controlled orientation.
- avoids flat horizontal surfaces.

### 3) Mechanical stability is essential
CT requires
- stable positioning during rotation.
- minimal movement.

This means that the holder must firmly secure the battery and minimise vibrations and drift.

### 4) Minimising material in the X-ray path
Since attenuation depends on material thickness and density,
- the material of the holder should be **low attenuation**.
- geometry should avoid blocking the beam.

### 5) Implications for measuring swelling
CT measures structural changes such as
- expansion.
- deformation.
- geometry changes.

Swelling will therefore appear as
- displacement.
- strain.
- shape evolution.

## Important distinction for my project
- This manual focuses on **how to acquire high-quality CT data**, not on electrochemical processes directly. However, it provides the **experimental foundation required to measure swelling**, since accurate CT data is necessary to detect
- small structural changes.
- deformation.
- volume expansion.

## Limitations
- strong dependence on user setup and experience.
- multiple competing trade-offs (resolution vs noise time).
- artefacts cannot always be fully removed in post-processing.

## Takeaway
This manual demonstrates that **successful CT imaging depends on careful balance between X-ray parameters, sample positioning and experimental setup**. Proper positioning and parameter selection are critical for achieving high-quality data and errors in setup can introduce artefacts that cannot be corrected later. For this project, the result highligt that **holder design, stability and orientation are essential factors for accurately measuring swelling using CT**.