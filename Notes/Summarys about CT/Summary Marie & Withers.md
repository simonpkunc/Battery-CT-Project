# Summary (mixed with connection to the project) of Quantitative X-ray Tomography by Maire & Withers

## Overview
X-ray computed tomography (CT) is a non-destructive imaging technique used to reconstruct the internal 3D structure of a material from multiple 2D radiographs taken at different angles. In my project it will be used to analyze internal structural changes in batteries, such as swelling, deformation and damage during operation.

---

# What CT measures
CT measures the attenuation (försvagning) of X-rays as they pass throug a material.
Attenuation depends on:
- Material density.
- Atomic number.
- Thickness.

This results in a 3D-map of grayscale values where:
- Bright regions = high attenuation (dense materials).
- Dark regions = low attenuation (voids, cracks and pores).

## In my project:
CT can be used to measure:
- Thickness changes.
- Internal voids or cracks.
- Structural deformation.
- Volume expansion (swelling).

---

# How images are built
CT imaging consists of three main steps:

1) Acquisition (skaffa sig)
    - The sample is rotated.
    - X-ray projections are taken at many angles.

2) Reconstruction
    - Mathematical algorithms reconstruct a 3D volume.
    - Each voxel (volumetric pixel) represent local attenuation.

3) Visualization & processing
    - Slices or full 3D volumes are analyzed.
    - Segmentation separates different phases/materials.

# Important to have in mind
The final image is not a direct pciture, but a **reconstruction based on mathematical inversion (baklänges)**.

---

# Key concepts

* Voxels
    - 3D pixels representing attenuation values.
    - Resolution depends on voxel size.

* Resolution
    - Limited by detector, optics and setup.
    - Trade-off between resolution and scan time.

* Contrast
    - Comes from differences in attenuation.
    - Can be weak between similar materials.

---

# Example analyses from the paper

1) Microstructure analysis.
    - Identifying pores, cracks and inclusions (inneslutningar).
    - Studying material morphology (läran om form).

2) Deformation analysis.
    - Tracking how structures change under load.
    - Using digital volume correlation (DVC).

3) Time-resolved (4D) CT.
    - Observing changes over time.
    - Useful for dynamic processess.

* For batteries:
    - Observe swelling during cycling.
    - Track crack formation.
    - Monitor structural degradation.

---

# What can I measure in batteries?

* Using CT, I can quantify:
    - Changes in thickness.
    - Changes in volume (swelling).
    - Internal cracks or defects.
    - Void formatation.
    - Structural heterogeneity.

This is directly relevant to **understanding how battery materials behave during charging/discharging.

---

# What can I not measure (project limitations)?

CT has several important limitations.

1) Limited resolution
    - Very small features may not be visible.

2) Low contrast between similar materials.
    - Difficult to distinguish materials with similar attenuation.

3) Noise and artefacts (distortions = förvrängningar)
    - Beam hardening (tänk löparna som fastnar i utkanten av skogen från podden).
    - Ring artefacts (circular distortions caused by miscalibrated or defective detector elements).
    - Motion artefacts (blurs caused by movement).

4) No direct chemical information
    - CT measures structure, not composition.

For this project:

- Cannot directly measure electrochemical properties (which the sensors will do).
- Cannot distinguish phases (ett område med enhetliga egenskaper) with very similar densities easily.

---

# Practical considerations

- Scan time vs resolution trade off.
- Sample size limitations.
- Data size can be very large.
- Reconstruction requires careful parameter tuning.

# Relevance to my project

CT is central to this project because it allows:

- Non-destructive analysis of battery aninternals.
- Quantification of swelling and deformation.
- Visualization of failure mechanisms.

# Key goal:

Use the data from the CT to extract measurable quantities such as:
- Thickness.
- Volume change.
- Structural evolution.

---

# Key take aways

- CT reconstructs 3D internal structure from X-ray prjections.
- It measures attenuation, not material density.
- Is is powerful for structural and morphological analysis.
- It is limited by resolution, contrast and artefacts (förvrängningar i bilderna).
- It is highly relevant for studying battery degradation and swelling.

---

# Personal reflection

CT does not "see" materials directly - it reconstructs a model based on x-ray attenuation, i.e. how much of x-ray (röntgenstrålning) has been attenuated. For example: 

- Numbers are translated into gray scale (0,1 = black, 0,5 = gray and 0,9 = white).
- Low number -> dark pixel (meaning much x-ray (röntgenstrålning) has passed through).
- High number -> light pixel (meaning little x-ray (röntgenstrålning) has passed through).

These numbers are in turn called **the linear attenuationcoefficient**.

This means that all results depend on

- Setup (voxel size, energy on the x-ray, geometry and number of projections).
- Reconstruction (mathematical algorithms, filtering and corrections).
- Interpretation (segmentation (what is material and what is not), threshhold values and what I assume I see).

For my project, I must always ask:
- What does this measurement actually represent physically?