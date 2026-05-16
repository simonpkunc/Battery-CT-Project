1) **Adjust the histogram (window leveling)**
Do not make the image to dark or to bright.

    - If the iamge is **to dark**, low-contrast details in the electrode/separator structure may disappear ("black clipping").
    - If the image is **to bright**, bright regions may saturate and structural information can be lost ("white clipping").
    - The goal is to make the layers visible **without over-enhancing the contrast** or losing grayscale information.

    **Rule of thumb:** the layers should be clear, but the image should still look natural - not overly contrasted.

2) **Test mild filtering only if needed**

Use preview first and compare with the original. Do not apply aggressive filtering since it can blur or artificially enhance the electrode/separator layers. If the filtered image starts to look "painted" or too sharp, the filter is to strong.

3) **Validate the volume by scrolling/cine mode in all planes**

Scroll/play through the full volume in **XY**, **XZ** and **YZ** to verify the continuity, consistency and realistic geometry. What to check:

    - continuous layer structure.
    - gradual geometric changes between slices.
    - no sudden jumps or broken structures.
    - no obvious import artefacts or corrupted regions.

**Reason:** a CT scan may look correct in a single slice but still contain artefacts or import issues. Reviewing the full volume helps confirm that the dataset is physically meaningful and suitable for analysis.

4) **Identify a representative baseline region (20-30 slices)**

Find an area where the layer structure is clear, continuous and minimally affected by artefacts. Use this as a reference region for later comparison. **Reason:** a representative region makes comparisons between scans/cycles more reproducible.

5) **Perform a first simple measurement**

Measure something simple (e.g. local stack thickness, spacing between visible layers, feature width etc.) **Reason:** confirms voxel scaling and creates a quantitative baseline.