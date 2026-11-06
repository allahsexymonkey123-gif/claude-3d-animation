# Release validation

Completed 2026-11-06.

| Check actually performed | Result |
|---|---|
| Reference source integrity | Both included MP4 SHA-256 values match the user-supplied originals |
| Native frame coverage | 2,049 + 1,245 = 3,294 study frames, contiguous names and CSV rows |
| Native timestamps | Every consecutive source presentation timestamp follows 1/30 s, within microsecond rounding |
| Visual reference review | All 56 sequential sheets inspected, plus selected native-size stills; not an individual full-size inspection of every frame |
| Audio reference analysis | ASR word timing, windowed mixed-track measurements and EBU R128 loudness completed; no verified direct-listening timbre match |
| TypeScript | npm run typecheck passed |
| JSON and Python helpers | JSON parsed; all Python sources compile; helper scripts exercised |
| Portable resources | Core/reference Markdown links, font and license, frame/source files present |
| Executable reference analyzer | Ran against both original clips and produced the complete frame/sheet/measurement set |
| Still renderer | Multiple half-scale PNG stills successfully rendered |
| Deterministic posing | f0 and f270 rendered in 270,0 then 0,270 order; each PNG SHA-256 identical between orders |
| Full motion study | 360 frames rendered, native 30 fps at 540×960; included example trimmed to 12.000 s |
| Every-frame demo QA | All 360 frames decoded; no black, unplanned overwhite or identical neighboring frames flagged; all six sequential demo sheets visually reviewed |
| QA on an original reference | All 1,245 ref02 frames decoded successfully by video_qa.py |
| Side-by-side utility | Ran and produced comparison image |
| Audio mixer | Tested voice-only and voice-plus-bed branches with synthetic tones; voice-only output measured −14.3 LUFS, 48 kHz stereo PCM |
| GitHub publishing helper | JavaScript syntax and dry-run command plan passed; no public repository created or push performed |
| Independent instruction trial | A fresh agent used the repository to produce a different-topic luggage-sorter plan: 98 narration words, 8 contiguous shots, 720 frames, pending real voice honestly recorded |

## Scope and remaining limits

The included film is a simplified silent smoke render, not a finished reference-quality narrated short. Its code, camera and events are deterministic, but its surfaces, labels and mechanisms still need topic-specific production refinement. The default 1080×1920 composition was typechecked; the complete test video was rendered at half scale, not at full final resolution.

The original source meshes, physical measurements, render/animation settings and voice identity were not recovered. New scene dimensions/shader/camera/voice settings are explicit targets, not claimed ground truth. Perceptual voice matching and a complete narrated final output were not verified.

A local test-only Node compatibility shim was needed because the execution container could not enumerate network interfaces. It was not added to production source. Rendering was slow with this environment's software graphics; GPU performance on a user's computer was not benchmarked.

The public GitHub creation capability was unavailable in the connected tools. The downloadable repository includes a publishing helper for the user's authenticated GitHub CLI session. It does not contain an invented public repository URL.
