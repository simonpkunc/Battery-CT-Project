**Dragonfly CT workflow**

1) **Open the dataset/session**

    - open the .ORSSession or dataset.
    - verify that the correct volume is loaded.
    - confirm that the volume orientation looks reasonable.

2) **Adjust window leveling (histogram)**

    - turn on **Log Y**.
    - adjust the histogram usng the yellow limits.
    - make the layer structure visible **without clipping information**.

    **Avoid**
    - too dark --> loss of low-contrast detail (**black clipping**)
    - too bright --> saturation of bright regions (**white clipping**)
    
    **Rule of thumb:** layers should be clear but still look natural.

3) **Check dataset properties**

    Go to **Basic properties** and note
    - voxel size.
    - dimensions.
    - bit depth (16-bit/32-bit)

    **Reason:** needed later for measurements and comparisons.

4) **Validate the volume (cine/scroll)**

    Scroll through the volume in
    - XY.
    - XZ.
    - YZ.

    Look for
    - continuous layer structure.
    - gradual changes between slices.
    - no sudden jumps or broken structures.
    - no corrupted regions or import artefacts.

    **Rule of thumb:** if it looks physically consistent while scrolling, the volume is likely valid.

5) **Test filtering (optional)**

    Only if needed.

    **Image processing panel --> Advanced**. Use **Preview first** and compare with original.

    **Recommended mindset:** apply the weakest filter that improves readability.

    Avoid
    - over-smoothing.
    - "painted" appearance.
    - artificial sharpening.

    **Important:** always filter a **copy/new dataset**, never the original.

6) **Find a representative region**

    Choose a region
    - with clear layer structure.
    - minimal artefacts.
    - consistent geometry.

    Avoid
    - edges.
    - cropped regions.
    - noisy/distorted.

    **Tip:** use the crosshair to stay in the same physical location across views.

7) **Inspect repeating layer pattern**

    Zoom in and identify the repeating grayscale structure.

    Example from testscan: thin bright line --> thin dark line --> wider gray region --> thin dark line --> thin bright line --> thin dark line --> **REPEAT**.

    **Important:** do not assign material labels (anode/cathode/separator/current collector) too early.

8) **Perform a first simple measurement**

    Measure something simple
    - local stack thickness.
    - layer spacing.
    - feature width.

    **Purpose:** verify voxel scaling and establish a baseline.

9) **Save representative screenshots**

    Save
    - overview image.
    - representative slice.
    - zoomed layer structure.

    Document
    - voxel size.
    - histogram settings.
    - slice range.
    - filtering used (if any).