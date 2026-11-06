---
name: zen-3d-explainer-shorts
description: Create original vertical 30 fps low-poly 3D cutaway explainer stories using this repository's two supplied video references, detailed style bible, per-frame measurements and runnable Three.js/Remotion template. Use for requests to create a story using the downloaded ZEN animation style, miniature architectural or mechanical explainers, exposed layered mechanisms, smooth camera reframes, fast narration and white outlined captions with green emphasis.
---

# Make a ZEN 3D explainer short

## Load the reference system

1. Read [STYLE_BIBLE.md](references/STYLE_BIBLE.md).
2. Read the reports on [geometry/composition](references/reports/geometry-composition.md), [materials](references/reports/materials-color.md), [lighting](references/reports/lighting-render.md), [motion](references/reports/motion-camera.md), [editing/story](references/reports/editing-story.md), [captions](references/reports/captions-labels.md), [audio](references/reports/audio-voice.md) and [QA](references/reports/qa.md).
3. Inspect `references/sheets/ref01/` and `ref02/` for the required mechanism/move. Open corresponding full-size frames in `references/frames/` for fine details. Use `references/measurements/beat_timeline.json` to locate events.
4. Treat measured pixel values as evidence and scene-unit/material/voice settings as reconstruction choices. Never present suggested parameters as recovered source settings.

## Lock the visual identity

- Build actual 3D assets. Keep visible depth, continuous occlusion and consistent object dimensions across views.
- Stage one miniature world around a concrete cause and effect. Keep the main setting recognizable while revealing its hidden mechanism.
- Use a high three-quarter establishing view, an overhead plan when layout matters, and a lower section view when layers/paths matter. Make the active mechanism large enough to read on a phone.
- Use rough earthy surfaces, warm off-white architecture, blue-gray glass, rusty/orange roof or paver accents, saturated faceted green foliage and exposed brown soil with sparse stones/roots.
- Render clean edges with real material seams and contact shadows. Do not add a global thick black cartoon-outline pass.
- Keep backgrounds simple and quiet. Avoid heavy lens blur, film grain, glossy plastic, excessive bloom, constant orbiting, random camera shake and rapid unrelated cuts.
- Keep prose captions short, white and heavily outlined in charcoal. Highlight a meaningful noun/verb in green. Add small black mechanism labels with thin white leaders and green endpoint dots as needed.
- Do not add people or dialogue scenes simply because the upstream repository has characters. If the new story needs people, design original low-poly 3D figures as supporting props; the supplied clips do not define a human acting or lip-sync system.

## Produce the story

1. Turn the brief into one visible mechanism and a causal chain: familiar setup → failure → attempted fix → remaining failure → better mechanism → test → payoff. Do not force construction content onto unrelated topics.
2. Write `out/<slug>/SCRIPT.md` using [STORY_TEMPLATE.md](templates/STORY_TEMPLATE.md). Pick a duration from the brief; default 45–65 seconds. Use about 4.2–4.4 words/second, including pauses. Budget 0.5–1 second at the end to let the last idea register.
3. Verify claims for factual stories. Use screen action to demonstrate the cause, not merely decorate the narration. Do not repeat questionable numerical claims from the reference transcript as universal truths.
4. Record/generate an original continuous voice take using [voice-direction.txt](templates/audio/voice-direction.txt). Reuse one selected identity and recording setup for subsequent stories. Obtain actual word timings; inspect and correct them. Lock voice before final animation timing.
5. Write `story.json`: frame ranges, narration phrase, camera start/end, new object/state, mechanism, caption, label, SFX and reference frame. Use `templates/story.schema.json`. All audio/image paths must point to actual assets.
6. Build the world from [templates/diorama](templates/diorama). Replace the demo topic/geometry rather than renaming the same house shot. Keep constants in `style.ts` and event timings in `story.ts`.
7. Pose every property as a pure function of absolute frame number. Use seeded randomness created once, not new per-frame random samples. Make camera moves continuous within a shot. Keep contact/attachment points stable. Progress cracks along fixed paths; pivot slabs about a physical edge; move rigid pieces as rigid pieces; show flow along a coherent route.
8. Synchronize mechanism events within roughly 0–3 frames of the causal word, after checking actual narration. Use small labels to name parts, not paragraph overlays.

## Render, compare and deliver

1. Run `npm ci` and `npm run typecheck`.
2. Render a wide, a close section, a material reveal and an end frame. Use `npm run stills` for the starter; adapt frame limits for a longer project. Compare to relevant reference stills with `templates/scripts/compare.py`.
3. Correct silhouette, object scale, camera framing and value hierarchy before surface decoration. A centered scene on a tiny floating island does not match the references' frame-filling cutaways.
4. Render the full piece at 1080×1920, **native 30 fps**, H.264 yuv420p, CRF 16–18. Optional high-resolution delivery: 1440×2560 at the same frame rate. Upscaling is not extra source detail.
5. Mix original narration, optional licensed music and restrained mechanism SFX. Normalize using `templates/audio/mix.py`; target around −14.3 LUFS and a safer −1 dBTP ceiling. Do not reproduce the reference's measured overshoots.
6. If muxing externally, map the intended streams explicitly: `-map 0:v:0 -map 1:a:0`. Verify the result contains the actual mix rather than a silent track.
7. Run `python3 templates/scripts/video_qa.py out/<slug>/final.mp4 out/<slug>/qa`. Inspect every flagged frame and relevant consecutive sheets. Planned still holds/flashes must be declared; the reference's low motion does not mean every hold needs exaggerated drift.
8. Check randomized frame-order renders, visible flow direction, labels, captions, end timing, missing assets, black frames, clipping and audio presence. Use the [QA scorecard](references/reports/qa.md).
9. Save `VALIDATION.md` with what ran and any limitations. Deliver `final.mp4`, script, timings and editable source. Never call a silent mockup a finished narrated story or assert exact style identity from automated measurements alone.

## Capability boundary

The repository teaches a workflow and includes executable source; it does not install a pretrained video generator or reproduce an unavailable voice. Use available authorized tools. When a requested renderer/voice service is missing, finish all independent work and clearly identify the missing dependency. Keep code, visual references and media licensing distinct.
