# Geometry and composition

## Reading key

**O** = observable in frames. **M** = a measurement with an explicit method. **T** = a reproducible reconstruction target. All physical dimensions below are T; no model/blueprint/real-world scale was supplied. See `../measurements/palette_samples.json` for exact sampling boxes and `../measurements/caption_samples.json` for measured caption crops.

## Screen layout

| View | Observed composition | Reconstruction target |
|---|---|---|
| House wide | Roof/house dominate top half; driveway points toward garage; soil visible below | House 70–105% of frame width, active surface 35–65%, soil face lower 20–40% |
| Driveway overhead | Garage at top; long rectangular surface nearly parallel to image edges | Driveway centered, 45–65% frame width; preserve side lawn strips and footpath as orientation cues |
| Layer section | Camera lowers to show thin slab, thicker granular base and deep earth | Layer edge at 45–65% frame height; active section at least 50% frame width |
| Pit close-up | Garage top crop; pit and pump in soil; leader label above | Pit height 25–40% of frame height; pump occupies 25–40% of pit height |
| Sidewalk view | Repeated trees/house fronts behind a horizontal sidewalk; soil beneath | One long horizontal edge and 3–5 repeated modules, avoiding a featureless zoom crop |
| Payoff | Return to familiar overall property; final mechanism still visible | Resolve on the same spatial anchors, with a small camera settle and a clean last caption |

The percentages are broad framing targets derived by visual review, not automatic object segmentation. Check each composition in the supplied frames. ref01 f140 is a close three-quarter, f800 an overhead, f970 a sidewalk section; ref02 f30 establishes the slope and f500 isolates the underground pit.

## Scene coordinates and starter scale

Use metres as a convenient new-scene convention, Y up. Put the house toward −Z and the street toward +Z. Establish a ground datum at Y=0. Save object IDs and dimensions in a scene registry; never resize the same object to fit a later shot.

| Object | T dimensions/ratios |
|---|---|
| Plot | 14 m wide × 22 m deep; cut soil extends 6–8 m below datum or beyond the camera crop |
| House | 10.6 m wide × 7.2 m deep; main eaves 5.6 m, gable rise about 1.8 m |
| Garage | 5.3–6 m wide, door 2.65 m high, projecting 1–2 m from house front |
| Driveway | About 5.4 m wide × 12 m long; adjust to the original story, not building-code advice |
| Concrete | 0.10–0.18 m thick; a visible edge is essential |
| Granular base | 0.20–0.40 m in the visual model; make individual granules smaller than slab thickness |
| Sand bed | 0.025–0.06 m; pale tan strip, clearly thinner than base |
| Paver | Typical illustration block 0.20 × 0.10 × 0.06 m; use modular ratios, 0.003–0.006 m visible gaps |
| Footpath | About 1.2–1.8 m wide, .10–.15 m thick |
| Mature small tree | 3.5–5 m tall, crown roughly 2.2–3.2 m wide, trunk .25–.5 m diameter |
| Pit insert | Illustrative width .6–.9 m, depth 1.3–2 m; scale for readability, mark schematic |
| Pipe | Diameter .07–.14 m in context; enlarge slightly only in a diagram insert, and state exaggeration |
| Bevels | .005–.02 m on concrete/pavers; .01–.04 m on prominent architecture |

These are a new art-direction scale system. They are **not construction specifications**, and they are not asserted as the source videos' dimensions. Check real dimensions independently for factual technical content.

## House asset construction

The longer clip uses a recognizable suburban two-story gabled house: warm horizontal siding, white fascia/bargeboards, orange-red roof tiles, blue-gray windows with white mullions and dark shutters, a small sheltered entry, paneled pale garage, stone at the base, little flowers and an address plate. Model the large silhouette first, then layer narrow strips, panels and a few garden pieces. Keep glass reflections broad and diagonal. Use roof ridge/courses with shallow relief, not a smooth red box.

The shorter clip uses a flat-roof contemporary house: two offset plaster volumes, dark roof/floor trim, big rectangular blue windows, a dark paneled garage and sparse landscaping. The black trim belongs to the building; it is not a global contour shader. Do not force the gabled asset into every short.

Create 2–3 distinct architectural silhouettes if a longer story changes locations. For unrelated topics, translate the same hierarchy to the relevant object: large clean primary masses, readable secondary assemblies and small textured details only where the camera gets close.

## Terrain, foliage and background

Use a watertight terrain block or clipped earth volume. The top and cut faces must share an edge with no light leak. Put broad alternating lawn stripes on the top. Add small grass tufts at lawn/sidewalk and cut edges; roots hang from the thin topsoil boundary. Scatter stones in the section with varied scale/rotation and low contrast. A regular dot grid is visibly wrong.

Build a tree from a tapered 6–10-sided trunk and several interpenetrating faceted crown clusters. Start with an icosphere subdivision 1–2 and flat shading. Use 3–5 related greens and small per-cluster hue shifts. Match the reference crown silhouette; do not replace it with a smooth sphere or a photo billboard. Repeat trees with different seeds and scale rather than perfect copies.

Place a few broad pale green/beige faceted hills beyond the lot and a blue sky. Keep them behind the house and visually quieter than the mechanism. Avoid large sharp triangles filling the entire frame or an empty studio background below a floating model.

## Mechanism geometry contracts

- Give every removable layer an independent mesh and a stable original transform.
- Make a root a tapered curve/chain connected to its tree. Grow it along a fixed path.
- Split a slab into meshes before breaking it. Use a hinge/pivot at the retained edge to lift a panel. Do not nonuniformly scale a slab into a wedge.
- Reveal rebar by removing/fading the covering concrete, while preserving spatial alignment. Use parallel cylinders with cross bars and muted oxidized steel; no glowing neon lattice.
- Keep every paver's grid cell identity. A remove-and-replace sequence returns the **same** block to the same place.
- Model a pit as an open section with wall thickness and a bottom. Keep its pump/float/pipe attached to their defined mounting points.
- Use actual opaque occluders and a section opening for an underground view. A pipe painted on the soil can be a clearly marked diagram, but should not be presented as a hidden physical pipe visible through opaque ground.

## Starter limitations to improve for a final film

The runnable demo supplies primitive architecture, seeded stones, lawn bands, faceted crowns, a rigid slab reveal, illustrative pipe route and particle flow. It does not contain the original asset files, simulation, photo-matched UVs, engineering geometry, true fluid dynamics or a finished scene for arbitrary topics. Add bevels, richer texture, correctly anchored leaders and any topic-specific mechanism before claiming a final style match.
