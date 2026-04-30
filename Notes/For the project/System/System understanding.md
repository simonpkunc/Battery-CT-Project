# System understanging - CT + battery + charging
## What do I actually measure?
I do not measure
- materials directly.
- lithium concentration.
- electrochemical reactions.

I measure
- X-ray attenuation.
- reconstructed as voxel values.
- interpreted as structure.

Therefore: CT measures structural changes, not chemistry.

## What CT represents in my project
The CT system produces a 3D volume where each voxel represents local attenuation. This is interpreted as geometry, structure and boundaries so CT = a structural model of the battery.

## What happens in the battery (physical process)
During charging
- lithium ions (Li^{+}) move thorugh the electrolyte
- electrons (e^{-}) move through the external circuit.
- both are inserted into the graphite electrode.

This causes expansion of the graphite structure and mechanical deformation which is called lithiation.

## Key connection
Lithium insertion -> structural changes -> CT detects geometry changes.

## What CT can capture
CT can measure
- thickness changes.
- volume changes.
- deformation.
- displacement.
- structural heterogeneity.

These are indirect effects of electrochemical processess.

## What CT cannot capture directly
CT cannot measure
- lithium concentration.
- reaction rates.
- state of charge.
- electrochemical properties.

Therefore, interpretation is required to connect structure to physics.

## How CT + battery + charging connect to eachother
1) Battery is charged.
2) Lithium moves into graphite (lithiation).
3) Graphite expands.
4) Structure changes.
5) CT captures this as voxel changes.
6) Changes are quantified as
    - deformation.
    - strain.
    - displacement.
    - volume change.

## What I actually measure (final form)
In this project, I measure geometric changes caused by lithium insertion and NOT lithium itself.

## Important insight
Swelling is not a new feature. It is a small change in existing structure. Therefore, detection depends on resolution and image quality.

## Measurement strategy
Because segmentation is difficult (low contrast) I should focus on deformation fields (DVC), displacement and geometry-based measurements rather than strict material segmentation.

## Final understanding
CT in this project should be understood as **a method for measuring structural deformation caused by electrochemical processess**.

## One-sentence summary
CT measures the structural expansion caused by lithium insertion into the graphite electrode during charging.