1) **Adjust the histogram (window leveling)**
Do not make the image to dark or to bright.

    - If the iamge is **to dark**, low-contrast details in the electrode/separator structure may disappear ("black clipping").
    - If the image is **to bright**, bright regions may saturate and structural information can be lost ("white clipping").
    - The goal is to make the layers visible **without over-enhancing the contrast** or losing grayscale information.

    **Rule of thumb:** the layers should be clear, but the image should still look natural - not overly contrasted.

2) **Test mild filtering only if needed**

Use preview first and compare with the original. Do not apply aggressive filtering since it can blur or artificially enhance the electrode/separator layers. If the filtered image starts to look "painted" or too sharp, the filter is to strong.

3) **Identify a representative region/slice**

Find an area where the layer structure is clear, continuous and not dominated by artefacts. Use this as a reference region for learning the workflow and for later comparisons. **Reason:** a representative region makes it easier to compare different scans later. Avoid regions near cropped edges, strong artefacts or areas where the structure is unclear.

4) **Validate the volume by scrolling/cine mode in all planes**

Scroll/play through the full volume in **XY**, **XZ** and **YZ** to verify the continuity, consistency and realistic geometry. What to check:

    - continuous layer structure.
    - gradual geometric changes between slices.
    - no sudden jumps or broken structures.
    - no obvious import artefacts or corrupted regions.

**Reason:** a CT scan may look correct in a single slice but still contain artefacts or import issues. Reviewing the full volume helps confirm that the dataset is physically meaningful and suitable for analysis.

5) **Identify a representative baseline region**

Choose a region with clear and consistent battery structure to use as a reference for later comparison between scans/cycles. **Reason:** a healthy reference region makes it easier to identify degradation or structural changes later.