# CT in my project

## Project context
My project aims to use a laboratry-based micro-CT system to measure strcutural changes in batteries, especially swelling, during electrochemical cycling. The system combines X-ray imaging with battery testing in order to observe internal changes non-destructively over time.

The CT-system used in this project is a **Nikon XT H 225 ST 2x**, which is a **laboratory micro-CT system**. This means that it uses conventional X-ray tube, not synchrotron radiation. The main imaging mechanism is **absorption contrast**, meaning that image formation is based primarily on how strong different parts of the sample attenuate X-ray photons.

---

# What CT means in this project
In this project, CT is not just "taking a picture". It is a way to reconstruct the internal 3D structure of a battery from many X-ray projections taken at different angles.

The main purpose of CT here is to:
- observe the internal structure of the battery non-destructively.
- compare structures before, during and after charging and discharging.
- identify changes such as swelling, cracks, voids or deformation.
- quantify geometric changes in a reproducible way.

This is important because normal radiography only gives a 2D projection, where information is integrated along the X-ray path. CT, by contrast, reconstructs local attenuation values in 3D, which makes it possible to localize changes inside the sample.

---

# What the CT system actually does
## 1) X-ray generation
Inside the X-ray source, electrons are accelerated and then suddenly decelerated when they hit a metal target. This generates X-ray photons. Important points:
- the sample is **not** hit by electrons.
- the sample is hit by **X-ray photons**.

These photons then travel through the battery sample.

## 2) Interaction with the sample
As X-ray photons pass through the battery, some are:
- absorbed.
- scattered.

The combined effect is called **attenuation**. This means that the intensity of the X-ray beam decreases as it passes through the material. Dense or high-attenuation regions reduce the X-ray intensity more strongly, while voids or low-density regions reduce it less. So, CT does **not** directly "see" materials. It measures the attenuation of X-ray intensity caused by the sample.

## 3) Detection
After passing through the sample, the remaining X-ray photons reach the detector. The detector records how much X-ray intensity remains at each position. In simple terms:
- high remaining intensity means low attenuation.
- low reamining intensity means high attenuation.

This measurement is repeated for many projection angles as the sample rotates.

## 4) Projection data
Each measurement angle produces a 2D projection. Each projection contains information about the local attenuation along many X-ray paths. A single projection does not tell us exactly where attenuation happenden along the path; it only tells us the integrated effect. This is why one radiograph is not enough for my project. A bettery contains multiple internal layers and features that overlap in a 2D projection.

## 5) Reconstruction
The CT software takes projections from many different angles and reconstructs a 3D volume. Mathematically, the detector measures line integrals of attenuation. Reconstruciton algoritms, typically based on filtered back projection or related methods, estimate the local attenuation values throughout the sample volume. The final output is a 3D grid of **voxel**.

# Pixels, voxels and grayscale
## Pixel
A pixel is a 2D image element.

## Voxel
A voxel is 3D volume element. In CT, the reconstructed battery volume is made up of many voxels, and each voxel contains a value related to local attenuation. These attenuation values are visualized as grayscale:
- low attenuation -> darker area in the final picture.
- high attenuation -> lighter area in the final picture.

This means that voids, pores or cracks often appear darker, while denser areas appears brighter. Important note:
- this grayscale is a visualization of attenuation values, not a direct label of material density. A bright regios does not actually mean "this exact material", and a dark region does not automatically mean "this exact defect". Interpretation is still required.

# Why CT is useful for batteris
Batteries are complex layered systems. A simple 2D X-ray image can show that "something" is changing, but it usually cannot show exactly where that change is located in 3D. CT is useful in this project beacuse it can reveal
- layer thickness changes.
- local swelling.
- cracks.
- void formation.
- possible delamination or internal damage.

This is especially important when trying to understand how electrochemical cycling affects internal structure. For this project, the key advantage of CT is the internal 3D information without cutting the battery open.

# What can I measure with CT in this project?
## 1) Thickness changes
If a battery layer or region expands, CT can potentially detect changes in thickness. This is one of the most relevant measurements for swelling analysis.

## 2) Volume change
If the battery or some part of it changes size, CT can be used to estimate volume changes. This is more powerful than a single 2D thickness measurement beacuse it considers the full 3D geometry.

## 3) Shape change/deformation
By comparing scans from different states, CT can show wether the battery deforms uniformly or locally.

## 4) Internal damage
CT may reveal
- cracks.
- voids.
- gaps.
- separations between regions.

## 5) Structural heterogeneity
CT Can show wether changes are spatially uniform or concentrated in particular areas. This is important because battery degradation is often non-uniform.

# What I probably can not measure reliably
## 1) Very small nanoscale features
The system resolution is limited. Features much smaller than the voxel size or system resolution may not be vissible. So CT is powerful, but not unlimited.

## 2) Exact material identity from grayscale alone
CT primarily measures attenuation, not chemistry. Two different materials with similar attenuation may appear very similar in the image. This means that CT is not, by itself, a chemical identification tool.

## 3) Electrochemical properties directly
CT can not directly measure
- lithium concentration.
- current distribution.
- local electrochemical reaction rate.
- state of charge.

It only gives structural information unless combined with other methods.

## 4) Perfectly sharp boundaries
Because of finite resolution, detector blur, noise and reconstruction limits, boundaries may appear blurred. This affects precision when measuring very small thickness changes.

# Why 3D is essential in this project
A standard radiograph integrates attenuation along the beam path. That means internal structures overlap in the image. For batteries, this is a major limitation because:
- multiple layers overlap.
- local swelling may be hidden.
- cracks or voids may be difficult to localize.

CT solves this by reconstructing local attenuation values in 3D. This allows for:
- slicing the object virtually.
- localizing features.
- measuring geometry in volume rather than just projection.

So for swelling analysis, CT is not just "better quality X-ray". It is a fundamentally more informative method.

# Important limitations in my project
## 1) Resolution
Resolution determines the smallest detectable feature. Even if the nominal voxel size is small, actual effective resolution may be worse because of:
- source size.
- detector blur.
- motion.
- reconstruction.

This means that I must be careful not to over-interpret tiny features.

## 2) Noise
Noise can make features harder to distinguish. In practise, noise may:
- reduce contrast.
- complicate segmentation.
- mimic small features.

## 3) Artefacts
Artefacts are distortions that do not represent the real structure. Examples include:
- beam hardening.
- ring artefacts.
- reconstruction artefacts.
- motion artefacts.

These are especially important because they can affect both interpretation and quantitative measurements.

## 4) Contrast limitations
If two phases or regions have very similar attenuation, they may be difficult to separate in the reconstructed data. This is a major issue in many materials systems and may also affect battery imaging.

## 5) Dependence on setup and reconstruction
The final CT images depend on:
- scan parameters.
- X-ray energy range.
- number of projections.
- reconstruction method.
- filtering.
- segmentation choices.

This means that CT results are not purely "objective pictures". They are reconstructed representations based on measured attenuation.

# Image interpretation in this project
When interpreting CT images, I should remember:
1) The image shows attenuation values, not material labels.
2) Bright usually means higher attenuation.
3) Dark usually means lower attenuation.
4) Boundaries may be blurred by system limitations.
5) Artefacts may look like real features.
6) Interpretation must always be linked to physical plausibility.

A good question to ask is: does this feature represent a real structural change or could it come from noise, artefacts, reconstruction or limited contrast?

# Segmentation and quantification
To go from image to measurement, the data usually needs to be segmented. Segmentation means separating the reconstructed volume into regions of interest, for example:
- material vs void.
- outer boundary vs background.
- one internal region vs another.

This is where CT becomes quantitative. After segmentation, one can calculate:
- thickness
- area
- volume
- shape descriptors
- changes over time

For this project, segmentation will likely be one of the key steps in converting CT images into swelling measurements.

# Why this matters for my thesis
The goal of the project is not only to obatin images, but to obtain **meaningful measurements**. Therefore, CT must be understood at three levels:

## 1) Measurement level
How the X-ray data is physically generated and recorded.

## 2) Reconstruciton level
How projection data becomes a 3D image.

## 3) Interpretation level
How that 3D image becomes scientific information.

If any of these steps are misunderstood, the final conclusion may be misleading.

# Practical summary for my project
In practical terms, the CT workflow in my project is:
1) Place the battery in the CT system.
2) Rotate the sample and collect many projections.
3) Measure transmitted X-ray intensity at each angle.
4) Reconstruct a 3D volume.
5) Analyze voxel values and grayscale structure.
6) Segment relevant regions.
7) Extract measurements such as thickness, volume or structural changes.
8) Compare scans across different battery states.

# Key take aways
- My Nikon system uses laboratory micro-CT based on X-ray attenuation.
- CT measures transmitted intensity and reconstructs local attenuation values.
- The final 3D dataset consists of voxels with attenuation-related values.
- CT is useful because it provides internal 3D structural information non-destructively.
- The main quantities relevant to my project are thickness, contrast and interpretation.
- The main limitations are resolution, noise, artefacts, contrast and interpretations.

# Personal interpreation
For my project, CT should be understood as a method for converting differences in X-ray attenuation into a 3D structural model of the battery. That model can then be used to measure swelling and structural change, but only if I reamin aware of its limitations and the assumptions introduced by imaging, reconstruction and analysis.

# X-ray physics (why CT works)
## Why different materials appear diffrently
In CT, contrast does not come from "seeing" materials directly. Instead, it comes from how strongly different parts of the sample **attenuate X-ray photons**. Attenuation depends mainly on:
- material density.
- atomic number (Z).
- thickness of the material along the X-ray graph.

Materials with higher density or higher atomic number attenuate X-rays more strongly. This means:
- metals or dense components -> high attenuation -> brighter in the image.
- pores, voids or low-density regions -> low attenuation -> darker.

For batteries, this is important because:
- current collectors and dense materials are easier to see.
- graphite, electrolyte and similar phases may have similar attenuation -> low contrast.

So, visibility in CT is not guaranteed. It depends on wether different regions attenuate X-rays differently enough to be distinguished.

## What creates contrast
Contrast in CT images is created by **differences in attenuation** between neighboring regions. If two regions attenuate X-rays differently:
- they will appear with different grayscale values. 
- the boundary between them becomes visible.

If two regions have similar attenuation:
- they may look almost identical.
- boundaries may be difficult or impossible to detect.

In this project, this is critical because:
- swelling is often a small geometric change.
- not a completely new material.

This means that:
- I am not always detecting "new features".
- I am often detecting **small changes in existing structures**.

So contrast must be sufficient to:
- separate layers.
- detect thickness changes.
- identify voids or deformation.

## What limits what can I see?
Even if attenuation differences exist, several factors limit what can actually be observed in CT:

### 1) Resolution
The system can only resolve features larger than a certain size. Features smaller than this will not be visible or will appear blurred.

### 2) Noise
Noise introduces random variations in intensity, which can:
- reduce contrast.
- hide small features.
- make interpretation uncertain.

### 3) Artefacts
Artefacts are image distortions that do not represent real structure, for example:
- beam hardening.
- ring artefacts.
- reconstruciton errors.

These can sometimes look like real features and must be interpreted carefully.

### 4) Limited contrast
If two materials have similar attenuation, they may not be distinguishable even if they are physically different.

## What this means for my project
For this project, CT should be understood as a method that:
- measures attenuation differences.
- reconstructs them into a 3D structure.

However, what I can actually observe depends on:
- whether structural changes produce detectable attenuation differences.
- whether those differences are larger than noise and resolution limits.

This is especially important for swelling analysis, because:
- swelling is often a **small geometric change**.
- not a large change in material composition.

So detecting swelling relies on:
- being able to resolve small thickness or volume changes.
- having enough contrast to separate relevant structures.
- avoiding misinterpretation due to noise or artefacts.

In practice, this means that CT is powerful, but all measurements must be intepreted with awareness of its physical limitations.

# X-ray absorption (material dependence)
X-ray absorption is governed by how photons interact with the electroic structure of a material. Electrons can absord X-ray photons if the photon energy matches allowed energy transitions, meaning that absorption depends on both atomic structure and photon energy. This implies that different materials do not attenuate X-rays in the same way. Even if two materials have similar density, differences in atomic composition can lead to different absorption behavior.

In a laboratory micro CT-system, a broad X-ray energy spectrum is used. Therefore, the measured signal represents an effective attenuation over many photon energies, rather than a single well-defined energy. Fine absorption features are not directly resolved, but they still influence the overall contrast.

For this project, this means that contrast between different regions in the battery depends on their effective attenuation, which is influenced by both material composition and the X-ray spectrum. As a result, some materials or phases may be difficult to distinguish if their attenuation is similar.

# System-level limitations (source, optic and detector)
The performance of a micro-CT system is determined by the combined effects of the X-ray source, imaging geometry and detector. The X-ray source influences image sharpness through its focal spot size. A finite source size leads to geometric unshaprness, meaning that the reconstructed image is a blurred representation of the true structure. This limits the smallest detectable feature. The imaging system introduces additional limitations through optical effects and system geometry. These contribute to further image blur and distortions, meaning that measured structures may not perfectly match the real physical dimensions. The detector determines how the transmitted X-ray signal is recorded. Several factors are critical:
- noise introduces uncertainty in the measured intensity and reduces the ability to distinguish small differences.
- the point-spread function describes how a single point in the object appears spread out in the image, reducing effective resolution.
- pixel size limits the sampling of the image and sets a lower bound on measurable feature size.

Together, these effects define the effective spatial resolution and measurement accuracy of the CT system. For this project, this means that electrode swelling can only be detected and quantified if the structural changes are larger than the combined limitations of source size, image blur and detector resolution. Small or subtle changes may be difficult to resolve or may appear smoothed in the reconstructed area.