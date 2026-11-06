# Motion and camera

## Measurement method

Every native frame was decoded. Dense Farnebäck flow was calculated between consecutive RGB frames after area downsampling to 128×228; magnitudes were multiplied by 512/128 to express an approximate source-pixel displacement. The images are compressed, heavily textured, occluding and captioned. This is a diagnostic of visible image motion, not an exact estimate of camera movement. The tiny aspect scaling is approximate and is documented in the analyzer.

| M statistic | ref01 | ref02 |
|---|---:|---:|
| Median of per-frame median flow | .1415 px | .1320 px |
| 95th percentile of per-frame median flow | 15.0911 px | 2.3972 px |
| Median of per-frame 95th-percentile flow | .5761 px | 4.1211 px |
| Median mean RGB frame difference, 0–255 scale | .7950 | 2.3769 |
| Bit-identical neighboring decoded frames | 0 | 0 |

ref02 has more local water/rain movement, so its high-pixel-percentile flow can be larger while its median scene motion remains low. Never treat a caption change or lightning flash as a camera cut automatically. The supplied histogram-based cut candidates are **unverified candidates**, not the edit list.

## Visually reviewed move examples

These approximate windows bracket observed motion, not exact recovered animation keys. Open the full sequential sheets around each window.

| Reference frames | Observed move/action | Transferable rule |
|---|---|---|
| ref01 90–110 | Opening title fades; view moves closer; car enters | One decisive reframe on the change in explanation |
| ref01 224–245 | Rapid move to low section; car leaves view; base becomes visible | Reveal depth by changing viewpoint, while keeping the house as an anchor |
| ref01 350–380 | Glide to overhead driveway | Plan view makes crack/control-joint pattern immediately legible |
| ref01 475–505 | Return toward oblique; crack/rebar state transitions | State change and camera change share a causal beat |
| ref01 585–610 | Reframe overhead again | Reuse a familiar angle so the viewer can compare before/after |
| ref01 930–960 | Sweep from driveway across tree/sidewalk context to low side view | Continuous spatial move bridges nearby demonstrations |
| ref01 1048–1070 | Return from sidewalk toward driveway | Preserve left/right orientation |
| ref01 1120–1140 | Lower oblique view for root lift | Show the new vertical offset in profile |
| ref01 1240–1260 | Push to raised edge | Make the consequence occupy enough pixels to read |
| ref01 1395–1410 | Return to overhead grid | Give the next abstraction a clean plan |
| ref01 1540–1560 | Move to paver/sand section | Keep layer thickness and top alignment continuous |
| ref01 1860–1880 | Closer payoff view around car and pavers | A final restrained push supports the conclusion |
| ref02 437–452 | Fast push into underground pit area | Close-up is motivated by a hidden component |
| ref02 525–540 | Pull back to see whole route | Show the entire mechanism after naming parts |
| ref02 665–680 | Return to wider situation | Reset the viewer before a new failure |
| ref02 750–760 | Brief storm flash over same scene | Do not misclassify a flash as a hard scene cut |
| ref02 765–780 | Closer drain view for leaves | Local action gets a closer view, world remains the same |
| ref02 976–997 | Repeated short light flashes | Keep geometry fixed through the exposure event |
| ref02 1125–1140 | Move to curb outlet | Follow the physical route to its endpoint |
| ref02 1185–1244 | Evening transition and final settle | End on a stable readable result |

## Timing targets for new animations (T)

- Hold a useful composition about 30–90 frames while the voice explains it. Add small drift only if it helps; do not create constant unnecessary orbiting.
- Use 8–24 frames for an adjacent reframe, 18–36 for a large plan-to-section change. Begin and settle smoothly. Check the actual source window before choosing a move length.
- Use very small slow pushes, around 1–3% framing change over 2–3 seconds, as an initial hold treatment. This is a recommendation, not a calibrated source measurement.
- Use zero or very small roll by default. The original upstream 4–5° dramatic rolls and impact shakes do not define these references.
- For reveals, keep the explanatory action about 0–3 frames from its spoken keyword. Use the recorded take's timing; a transcript is not a sample-accurate cue sheet until checked.

Use a quintic smootherstep for a move that starts/stops at rest:

```ts
const clamp = (x: number) => Math.max(0, Math.min(1, x));
const smooth = (x: number) => { x = clamp(x); return x*x*x*(x*(x*6-15)+10); };
const u = smooth((frame-start)/(end-start));
position.copy(startPosition).lerp(endPosition,u);
target.copy(startTarget).lerp(endTarget,u);
camera.lookAt(target);
```

This curve is **a reproducible choice**, not a recovered source curve. An ease-out may better fit a particular source move. Avoid resetting the camera to its shot start every render and then integrating velocity; set the complete pose from the absolute frame instead.

## Object animation recipes (T)

| Mechanism | Construction and curve | Failure to avoid |
|---|---|---|
| Crack propagation | Fixed spline/path with a progress parameter; branch starts are timed offsets | A different random crack every frame |
| Root growth | Reveal a tapered fixed curve from tree to slab | Disconnected root teleporting across lawn |
| Slab lift | Pivot an existing mesh about the retained edge; show underside and shadow | Scaling a rectangle into a wedge or losing thickness |
| Jackhammer | Small 1–3 frame tool vibration while fragments separate on fixed trajectories | Shaking the entire world |
| Debris | Rigid pieces, seeded trajectories, settling rotation | Melting/warping concrete |
| Paver replacement | Stable cell ID and start transform; rise, move aside, return, seat | New random block layout after repair |
| Rain | Seeded particles with absolute-time modulo fall phase | Resampling every streak on each frame |
| Surface water | Flow texture/advection along slope; calm long ripples and edge foam | Texture scrolling uphill or ocean waves |
| Pipe flow | Constant-speed parameter along a connected path, confined to the pipe | Liquid jumping between pipe segments |
| Pump cycle | Fill → float threshold → pump on → discharge → water level falls | Uphill flow without showing a pressure source |

Use a curve arc-length parameter for constant-speed travel around bends. `curve.getPointAt(u)` is preferable to `getPoint(u)` when the segments have different lengths. For rigid parts, preserve parent transforms and attach points.

## Determinism and smoothness check

Render a motion span at each consecutive frame. Also render selected frames in shuffled order (e.g. 270,0,135,359) and compare hashes to their sequential renders. A result that depends on the previously rendered frame is invalid for batch rendering. Resolve strobing shadows/textures before using frame interpolation; interpolation cannot fix geometry discontinuities or wrong physical motion.
