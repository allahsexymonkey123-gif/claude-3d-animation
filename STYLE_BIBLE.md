# ZEN 3D cutaway explainer style bible

## Contents

1. Evidence and limits
2. Format and visual signature
3. Composition and geometry
4. Color, material and light
5. Motion and editing
6. Typography, voice and sound
7. Story transfer and acceptance

## 1. Evidence and limits

| Item | ref01 | ref02 |
|---|---:|---:|
| Subject | Concrete, control joints, roots and pavers | Driveway runoff, drains, pumps and backup |
| Original upload | `snapgram.io_jgum1fo1itz7(1).mp4` | `snapgram.io_c12wj0upkl63(1).mp4` |
| Native raster | 512×910 | 512×910 |
| Native frame rate | 30/1 | 30/1 |
| Decoded video frames | 2,049 | 1,245 |
| Video duration | 68.300 s | 41.500 s |
| Audio duration | 68.192 s | 41.350 s |
| Approx. ASR word count | 280 | 183 |
| Words/second through last ASR word | 4.218 | 4.429 |
| Integrated mixed loudness | −14.3 LUFS | −14.2 LUFS |
| Loudness range | 1.7 LU | 1.6 LU |
| Measured true peak | −0.2 dBFS | +0.6 dBFS |

All frames were decoded without a frame-rate conversion. Sequential 60-frame contact sheets cover the entire videos: 35 sheets for ref01 and 21 for ref02. All 56 sheets were visually reviewed, and representative frames were opened at native size. `per_frame.csv` describes each decoded frame; `frame_review_index.csv` associates every frame with its sheet, semantic beat and nearest automatic transcript segment. Frame metadata and SHA-256 hashes permit coverage checks.

**M = measured**, **O = visually observed**, **T = reconstruction target**. Pixel coordinates, frame counts, loudness, sampled colors and optical flow are measured. Material roughness, actual scene dimensions, camera focal lengths, easing curves, polygon counts, original renderer and voice identity are **not recoverable exactly from these compressed videos**. Numeric settings below are explicit reconstruction targets unless marked M. Do not convert a guessed Blender/Three.js value into a statement about how the source was made.

Audio evidence consists of ASR and signal analysis, not verified direct listening to vocal timbre in this environment. The casting brief is a suggested original voice direction. Do not call it an exact reference voice.

## 2. Format and visual signature

**O:** A bright, miniature, full-3D educational model. Architecture is more detailed than an abstract block diagram but simplified enough to read immediately. Trees show flat polygon facets. Hardscape shows grain, seams, panels and edge thickness. Windows have restrained blue reflections. A cross-section through the lot exposes warm soil, stones, roots, gravel, pipes or a pit. Real contact shadows make all of these surfaces belong to one world.

The shots function as **a moving physical diagram**. The world stays recognizable. The camera travels from the overall situation to a plan/section/insert. A surface is removed, tinted, split, raised or replaced to explain the current sentence. The viewer always knows what changed and why.

**T:** 1080×1920, 30 fps, full frame, no letterboxing. Match the reference's portrait composition rather than rendering a wide scene and cropping its sides. Keep the important mechanism away from the app UI edges and the bottom 12–15% when possible. Do not mechanically rescale native coordinates without accounting for the 512×910 raster's tiny aspect-ratio difference from exact 9:16.

There is no character performance, lip sync, handheld live-action camera or painterly 2D cast in these samples. If a new topic requires people, their animation must be newly designed, not falsely inferred from these references.

## 3. Composition and geometry

Use the [geometry/composition report](reports/geometry-composition.md) for dimensions and construction recipes.

- **O:** Establishing views look down from a three-quarter angle. The house occupies much of the upper half, the active driveway/yard occupies the middle, and the exposed soil face can fill the lower third or more.
- **O:** The longer reference alternates between three-quarter house views, overhead driveway diagrams and a low side view of a sidewalk. The shorter reference mainly preserves a front/side cutaway and pushes close to the pump pit.
- **O:** The frame is filled by the setting. The earth section continues below the crop; it rarely reads as a small floating toy island in empty space.
- **T:** Use a long-enough perspective lens to keep distortion modest. Start at a vertical FOV of 30–40°, camera elevation 28–50° for establishing shots, 70–88° for plans and 10–25° for section inserts. These are camera-fit targets, not measured source camera data. Orthographic projection can work for isolated plans, but do not call the whole reference orthographic.
- **T:** Use real mesh thickness on slabs, paving blocks, curbs and cut faces. Preserve neighboring edge alignment while an individual piece moves. Keep material boundaries consistent through camera moves.
- **O:** Roof trim, garage panels, window mullions, siding courses, foundation stone, little plants, grass tufts and driveway edging provide detail. The active mechanism gets more resolution than distant scenery.

## 4. Color, material and light

Use the [material/color](reports/materials-color.md) and [lighting/render](reports/lighting-render.md) reports. The palette samples are **displayed, lit pixels**, not original base color textures.

| M: sampled region | Displayed median sRGB | Evidence |
|---|---|---|
| Lit concrete | `#B4B0A4` | ref01 f140 |
| Lawn | `#54A332` | ref01 f140 |
| Terracotta roof | `#B24718` | ref01 f140 |
| Warm siding | `#C8B79E` | ref01 f140 |
| Soil | `#684111` | ref01 f140 |
| Blue car | `#0D54A2` | ref01 f140 |
| Sky | `#90CBEE` | ref02 f30 |
| Plaster wall | `#BEB5A6` | ref02 f30 |
| Dark garage | `#1D2025` | ref02 f30 |
| Window glass | `#7C8D9E` | ref02 f30 |
| Pump body | `#0A5A95` | ref02 f500 |

Grass is bright but architecture is warm and subdued. Soil is brown/ochre, not gray. Pavers use related terracotta/tan/brown families. Water is translucent blue/teal with light flow streaks. Window frames are true dark/white construction elements, **not** a black ink outline around every object.

**T:** Roughness around .75–.95 for concrete/soil/plaster, .6–.9 for foliage/wood, .2–.4 for stylized glass, .15–.3 for water. Keep metallic behavior off ordinary surfaces. These are shader starting points. Tune output pixels against the sampled reference instead of copying display hex values directly into a physically lit material and expecting the same result.

**O:** Daylight produces readable directional shadows with soft ambient fill. Leaf facets remain readable without deep black crushing. The second video gradually turns to warmer evening windows and a darker blue/purple sky at its end. Storm flashes are brief and purposeful.

**T:** Key light above/front-left with ambient/hemisphere fill. Add subtle contact AO where supported, not a dark halo around every edge. Use anti-aliasing and consistent color management. Keep film grain, global outlines and strong bloom off. Preserve fine aggregate; avoid dense photographic noise that crawls at phone resolution.

## 5. Motion and editing

Use [motion/camera](reports/motion-camera.md) for frame examples and [editing/story](reports/editing-story.md) for the complete beat map.

**M:** The decoded videos contain no bit-identical adjacent frames. This does not prove every held shot has visible animation; compression and extremely subtle drift can change pixels too.

**M:** Median dense optical-flow magnitude per frame, measured at 128×228 and expressed in native-source pixels, is approximately **0.141 px for ref01** and **0.132 px for ref02**. At the 95th percentile of those per-frame medians, values rise to **15.09 px** and **2.40 px**. These are optical-flow diagnostics over all image content, not calibrated world camera velocities; captions, flowing water, occlusion and large perspective changes can contaminate the estimate.

**O:** Most explanation beats hold a stable composition. Changes in viewpoint come in short smooth bursts, usually when the current mechanism changes. Some fast material/state transitions and intentional flashes exist. Do not impose the upstream's constant strong camera creep, 4–5° roll, impact kicks or march cadence.

**T:** Reconstruct a small drift during a 1–3 second read hold, with 8–24 frame eased reframes for adjacent views and 18–36 frame moves for large orbit/plan changes. Use a visual guide first; do not require every move to use one duration. Keep the motion smooth at **every** 1/30-second step. Avoid 12 fps stepped poses, ping-pong easing, elastic springs, speed jumps, per-frame random movement and temporal texture flicker.

**O:** Cracks propagate along fixed branching paths. Roots grow from fixed locations. Slab edges lift while preserving thickness and neighboring alignment. Debris separates into rigid pieces. Small pavers rise and return to their original cells. Rain falls in thin streaks while water follows a readable surface or pipe route. House/road geometry does not morph between these events.

## 6. Typography, voice and sound

Read [captions/labels](reports/captions-labels.md) and [audio/voice](reports/audio-voice.md).

**O:** A two-line all-caps hook sits near the top for roughly the opening three seconds, using white and green emphasis. Spoken captions use a short phrase or sometimes one word, white heavy geometric sans, a thick charcoal outline and a little shadow. Emphasized words turn green. Small part labels are uppercase white on black, frequently with a thin leader to a green circled dot. Red/white tilted status stamps mark failures. Only the opening hook is a headline; the rest should remain uncluttered.

The clips use different caption positions. **T:** For the longer plan-to-section treatment, begin around 62–66% of frame height. For the shorter front-section treatment, begin around 73–77%. Move slightly to protect the mechanism rather than centering every caption blindly. Default new scenes to the closer composition, then check readability. The starter uses the lower/front-section treatment.

**T:** Montserrat ExtraBold/Black is a bundled, redistributable approximation, not an identified source font. Use roughly 70–88 px at 1080 width, font weight 800–900, 6–10 px outline, one or two lines, 1.0–1.1 line height and 80–90% max text width. The demo starts at 76 px.

**M:** ASR gives about 253 and 266 words/minute. The visible demonstrations follow the narration's causal phrases. **T:** Use one original continuous narrator at 4.2–4.4 words/second, clear and conversational, with short breath pauses and slightly stronger stress on the new mechanism. Do not claim an identified actor/provider/voice preset. Sound beds should support rather than obscure the explanation. Exact music/SFX stem levels cannot be extracted from a mixed track.

## 7. Story transfer and acceptance

Transfer the **grammar**, not the driveway topic: show a familiar thing, reveal the hidden problem, attempt a fix, expose its limitation, introduce the better mechanism, test it and resolve the opening question. Machines, biology, logistics, products and ordinary stories can use the same visible causal staging. If the user wants character drama, create a separate cast/performance specification; these two clips do not establish one.

Do not simply animate the same house for every brief. Preserve the colors, mesh readability, physical reveal logic, camera restraint, captions and narration pacing while designing a new setting and story.

A finished short needs: visible spatial continuity, a clear cause-and-effect action in each beat, smooth native 30 fps motion, reference-like composition/material hierarchy, accurate caption/audio synchronization, readable small-screen labels and an honest completed render. See the [QA rubric](reports/qa.md).
