# Summary - Quantifying microstructural dynamics and electrochemical activity of graphite and silicon-graphite lithium ion battery nodes by Pietsch et al.
## Purpose
This study aims to **quantify how electrode microstructure and elechtrochemical activity evolve during battery operation**, with a particular focus on **graphite and silicon-graphite anodes**. The goal is to understand how **lithiation and delithiation lead to structural changes**, and how these changes can be measured using X-ray tomography.

## Method
The authors use **synchrotron-based operando X-ray tomography**, combined with
- **Phase contrast imaging** -> improves visibility of weakly attenuating materials like graphite.
- **Digital Volume Correlation (DVC)** -> tracks local displacements and deformation in 3D over time.

Instead of relying only on grayscale or segmentation, DVC allows them to
- measure **local displacement fields**.
- calculate **strain and volume changes** directly from the CT data.

## Key observations
### 1) Graphite electrodes expand during lithiation
- Graphite expands by ~ 10 % on full lithiation.
- The electrode as a whole expands by ~ 6-7 %.
- Expansion is **anisotrpic**
    - mainly in the **through-plane (TP) direction**.
    - limited in-plane due to mechanical constraints.

### 2) Structural changes are small but measurable
- Changes in graphite are realtively small (~ 10 %), making them difficult to detect.
- DVC enables detection of these small changes without relying heavily on segmentation.

### 3) Lithiation is spatially non-uniform
- Lithiation starts at the **electrode-separator interface** and moves inward.
- This creates **gradients in state of charge (SOC)** within the electrode.

### 4) Microstructure changes only slightly for graphite
- Particle expansion is mostly accomodated by overall electrode expansion.
- Only small changes in
    - porosity.
    - tortuosity.
These changes are comparable to natural inhomogeneties in the electrode.

### 5) Silicon causes much larger deformation
- Silicon particles expand up to ~ 280 % (literature value).
- In composite electrodes
    - expansion becomes **strongly localized**.
    - deformation is **much larger and more heterogeneous**.
- Silicon expansion
    - reduces porosity.
    - changes microstructure.
    - may affect lithium transport.

## Key insights
**Electrochemical activity can be inferred from mechanical deformation**
- expansion = lithiation.
- contraction = delithiation.

**CT + DVC enables quantitative measurement of swelling**
- not just visualization, but actual measurement of straing and volume change.

**Microstructure influences transport**
- porosity and tortuosity affect lithium diffusion but small changes (graphite) may not strongly impact performance.

**Material choice strongly affects deformation**
- graphite -> small, uniform changes.
- silicon -> large, localized changes.

## Relevance for my project
### 1) Direct link between CT and swelling measurement
This paper shows that CT data can be used to
- measure **local deformation**.
- calculate **volume change and strain**.

This is exactly how swelling can be quantified in my project.

### 2) Swelling = electrochemical expansion
This study confirms that
- lithiation causes **physical expansion of electrode material**.

This expansion is measurable in CT as
- displacement.
- strain.
- voxel changes.

This directly supports using CT to measure **electrode swelling**.

### 3) Spatially non-uniform swelling
Swelling is
- not uniform.
- depends on position in the electrode.

This is important when interpreting CT data, since
- local measurements matter.
- averaging may hide important effects.

### 4) Limits of contrast in graphite
Graphite has
- low X-ray attenuation.
- poor contrast.

This means that
- segmentation (which is the process of separating different regions or materials in a CT image based on grayscale values) is difficult and that measurement should rely more on
    - geometry.
    - deformation.
    - displacement.

### 5) What CT actually measures in this context
CT does NOT measure lithium concentration directly. Instead, it measures structural changes caused by lithiation such as
- expansion.
- deformation.
- microstructure evolution.

## Important distinction for this project
This study focuses on **electrochemically induced expansion during lithiation**, which is directly aligned with the swelling studied in this project. Unlike thermal runaway studies, the changes here are **slower and smaller**, but still measurable using CT. This makes the paper highly relevant for understanding how swelling originates and how it can be quantified from CT data.

## Limitations
- Graphites has low contrast -> difficult imaging conditions.
- Small volume changes -> sensitive to noise and resolution.
Results depends on
- image quality.
- reconstruction.
- analysis method.

## Takeaway
This study demonstrates that **X-ray CT combined with digital volume correlation enables quantitative measurement of electrode swelling and deformation during battery operation**. Even small structural changes, such as those in grpahite, can be measured, while larger and more complex deformation occurs in silicon-conatining electrodes. The results show that swelling is spatially non-uniform and directly linked to electrochemical processess, makin CT a powerful tool for studying structural evolution in batteries.