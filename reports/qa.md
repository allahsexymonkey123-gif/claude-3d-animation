# Validation and acceptance rubric

## Reference-study coverage

Run `python3 templates/scripts/validate_repo.py` from the root. It checks original video hashes, all frame filenames, per-frame CSV coverage, sequential sheet count, Markdown links and Python syntax. A checksum/coverage pass validates the package, not artistic quality.

All 3,294 frames have numeric measurements and semantic-beat associations. The visual review used all 56 consecutive contact sheets, plus selected native-size frames. This is not a claim that every frame was individually inspected at native size. Voice timbre was not verified by listening in the analysis environment. Preserve those limits in any downstream description.

## Before a final full render

1. Typecheck/build the actual source.
2. Render a wide, overhead/section and close insert at actual output resolution.
3. Compare with relevant reference stills, not a random frame with a different shot type.
4. Confirm geometry continuity, clear mechanism, material color hierarchy, ground contact and text readability.
5. Render consecutive frames for a fast camera move, a reveal and a small-object action. A good isolated still does not prove smooth animation.
6. Render several frame numbers out of order and compare to normal-order results. Fix any stateful simulation/randomness.

## QA scorecard

Score each dimension 0–5 and list the actual frame(s) checked. A final film should have no dimension below 3, aim for 4+ overall, and have no critical mechanism/audio/continuity failure. These are production acceptance targets, not measured scores of the starter.

| Dimension | A score of 5 means | Typical failure |
|---|---|---|
| Composition | Frame-filling world, clear primary mechanism at phone size | Tiny floating island, giant empty sky, hidden mechanism |
| Geometry | Consistent solid objects, thickness, depth and occlusion | Billboard substitutes, morphing house, paper-thin slab |
| Materials | Warm subdued architecture, lively foliage, readable layers and fine texture | Glossy plastic, generic noise, wrong relative scale |
| Light | Readable facets, connected shadows, stable exposure | Crushed black sides, floating parts, shadow crawl |
| Camera | Motivated smooth reframes and stable read holds | Constant orbit, sudden speed jumps, shake |
| Object motion | Coherent attachment, pivots, paths and trajectories | Popping, melting pieces, teleporting liquid |
| Mechanism | Causal action makes sense without needing every caption | Water flows uphill without a pump, misaligned part |
| Typography | Crisp, well timed, legible and positioned around action | Clipped outline, paragraph caption, broken leader |
| Voice | Actual original voice, consistent identity, natural checked take | Silent track, robotic splice, abrupt identity changes |
| Sound/timing | Mix clear, near target loudness, picture events synchronized | Bed masks speech, last word cut off, clipping |

## Every-frame checks

Run `video_qa.py` on the final encoded MP4, not just an intermediate. It decodes every frame and flags black, overwhite and identical-frame events. It does not prove absence of every visual artifact. Review the flags and declare intentional holds/flashes in the expected-events JSON. The supplied references contain long low-motion holds, so low flow alone is not a failure.

Check cadence from native timestamps; do not accept a 15 fps animation duplicated into a 30 fps container. Check dimensions, frame count and duration agree with the planned composition. Verify no missing final frames, texture pops, random-seed changes, aliasing, Z-fighting, alpha sorting defects or camera collisions.

For detailed QA sheets, reuse `analyze_reference.py` on a rendered film with a new ID/root. This is more storage intensive but saves each frame and its metrics. Keep generated QA outputs under `out/`, not inside the reference evidence folders.

## Audio checks

Listen to the complete final export at normal speed. Verify pronunciation, voice continuity, breaths, narration onset and final word. Check LUFS/true peak from the encoded output. Use about −14.3 LUFS and a maximum around −1 dBTP as a starting delivery target. The reference's measured peak overshoots are not a target.

If no narrator tool was available, label the film silent and deliver the ready script/timings with that limitation. Do not call it a finished narrated story. A transcript, generated waveform or provider setting alone is not evidence of the intended voice sound.

## Source/editability checks

Keep editable geometry, `story.json`, script, actual voice identity/settings, words, captions, SFX cues and a concise `VALIDATION.md` with the final outputs. Do not put API keys in source control. Preserve separate notices for any assets with licenses beyond the new code's MIT license.
