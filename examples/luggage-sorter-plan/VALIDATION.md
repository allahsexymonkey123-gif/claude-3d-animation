# Planning validation

Completed on 6 November 2026.

| Check | Result |
|---|---|
| Repository instructions and style reports | Read; inspected images are listed in SOURCES.md. |
| Original narration | 98 spoken words; SCRIPT.md and story.json match exactly. |
| Duration | 720 frames / 30 fps = 24.000 seconds. |
| Shot coverage | Eight ordered positive-length ranges cover [0,720) without gaps or overlaps. |
| Ending | Target voice ends at f690; 30-frame / 1-second final hold. |
| JSON shape | Checked field types, required fields, constants, enums, minima and array limits against templates/story.schema.json using a local Python checker for the schema keywords present. No external JSON Schema validator was installed or run. |
| Reference paths | All eight story.json reference-frame paths exist. |
| Missing-media honesty | voice_file and words_file are null; voice_status is pending. No invented provider, recording, word timings, model assets or completed movie. |
| Technical claims | Checked against primary IATA, equipment-maker and airline sources; boundaries are explicit in SCRIPT.md and SOURCES.md. |
| Scope | Only plan documents and story.json were written in style-forward-test. No render, audio generation, paid service, external publishing or repository edit was performed. |

## Production still to do

Cast/record one original voice; obtain and check its real word timings; build the new airport geometry; fit captions and causal actions to that take; render proof stills and consecutive motion frames; inspect the complete movie and audio; measure final delivery metadata/loudness. Build, typecheck, render, perceptual style comparison and every-frame movie QA were not run because this request is for a production plan only.

The plan is usable for a fictional, simplified conventional conveyor-and-pusher sorter. It does not specify any named airport's exact installation, operational interface, processing time or mechanical dimensions. A real recording may require minor cue changes within the fixed 24-second duration. No unresolved creative choice blocks storyboarding or asset construction; the performer/provider remains a production selection.
