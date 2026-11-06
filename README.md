# ZEN 3D Explainer Shorts

A downloadable Claude Code production kit for **smooth, fully 3D, low-poly cutaway explainers**: miniature environments, readable materials, exposed mechanisms, restrained camera moves, fast narration, white outlined captions and selective green emphasis.

Built from a frame-complete study of the two videos supplied for this project. The package contains **3,294 full-size study frames, 56 consecutive 30 fps contact sheets, both unmodified MP4s, per-frame measurements, word-timed automatic transcripts and detailed production reports**.

The repository structure follows [mromidev/claude-animated-shorts](https://github.com/mromidev/claude-animated-shorts), but its visual system is replaced. These references contain full 3D objects and architectural diagrams, rather than the upstream flat cartoon cast. See the [upstream mapping](references/reports/UPSTREAM_MAP.md).

## Give this to Claude

Download/unzip this complete repository, open it in Claude Code, and say:

> Read CLAUDE.md and SKILL.md. Use the ZEN 3D explainer style in this repository to create an original story about [YOUR TOPIC]. Keep the 3D render style, mechanism reveals, 30 fps motion, narration pacing and caption treatment consistent with the two supplied reference videos. Inspect the relevant reference frames before designing the shots. Follow the full workflow through rendering and QA.

Claude Code can also use the included `/create-story [your topic]` project command. After Claude has loaded it, the short version is:

> Create a story using the animation style you downloaded about [YOUR TOPIC].

This is a **production kit, not a trained video model**. Claude still needs a rendering environment and an available narrator/voice tool to produce a finished narrated video. A written prompt alone cannot guarantee identical rendering quality or recover the references' original assets/voice. The included working 12-second motion study is a starting scene, not a finished replica of either reference.

## What's inside

| Path | Purpose |
|---|---|
| [SKILL.md](SKILL.md) | Agent workflow and hard style rules |
| [CLAUDE.md](CLAUDE.md) | Automatically discovered project instructions for Claude Code |
| [references/STYLE_BIBLE.md](references/STYLE_BIBLE.md) | Complete visual, story and production specification |
| [references/reports](references/reports) | Composition, geometry, materials, light, motion, captions, audio, editing and QA |
| [references/videos](references/videos) | Two unmodified user-supplied MP4 references |
| [references/frames](references/frames) | All 3,294 decoded frames, at 512×910 |
| [references/sheets](references/sheets) | 56 sequential sheets, 60 frames per complete sheet |
| [references/measurements](references/measurements) | CSVs, hashes, metadata, transcripts, palette samples and frame review index |
| [templates/diorama](templates/diorama) | Runnable Three.js + Remotion 3D scene, animation, camera and overlays |
| [templates/audio](templates/audio) | Original narrator brief, voice settings template and loudness mixer |
| [templates/scripts](templates/scripts) | Reference analysis, still rendering, comparisons, QA and public GitHub publishing |
| [templates/STORY_TEMPLATE.md](templates/STORY_TEMPLATE.md) | A new story's required planning outputs |
| [templates/SCRIPT_example.md](templates/SCRIPT_example.md) | Original example showing how to transfer the visual grammar |
| [references/manifest.json](references/manifest.json) | Source provenance, coverage and measurement limits |
| [examples](examples) | Silent rendered motion study and a complete different-topic story plan |
| [VALIDATION.md](VALIDATION.md) | Checks actually completed and production limits |

## Run the starter

Install Node.js 20+, npm, Python 3.10+ and ffmpeg/ffprobe. From this folder:

```bash
npm ci
npm run typecheck
npm run studio
npm run stills
npm run render
```

The composition is `DioramaShort`, 1080×1920, 30 fps, 360 frames. The demo is intentionally silent. To use your own voice, put `voice.wav` in `public/` and render with:

```bash
npx remotion render src/index.ts DioramaShort out/narrated.mp4 --props='{"captions":true,"labels":true,"title":"WATER NEEDS A PATH","voice":"voice.wav"}' --codec h264 --crf 17 --gl angle --concurrency 1
```

Replace the demo caption/beat times with the actual narration timings first. The narrator's audio and the composition must have matching duration. To make a different length, change `TOTAL`, the beat/camera ranges and the cues together. Do not append a new script to the unchanged twelve-second demo.

Optional reference-analysis dependencies and integrity check:

```bash
python3 -m pip install -r requirements-analysis.txt
python3 templates/scripts/validate_repo.py
python3 templates/scripts/video_qa.py out/demo.mp4 out/qa
```

Remotion may download its headless browser on first use. This package does not include Node modules or browser binaries. Refer to [Remotion's license](https://www.remotion.dev/license) for its own usage terms; this repository's MIT license does not replace dependency licenses.

## Publish a new public GitHub repository

This archive is ready to publish; a public repository was **not** created by the packaging process. Install [GitHub CLI](https://cli.github.com/), sign in once, then run inside the unzipped folder:

```bash
gh auth login
npm run publish:github
```

That explicit command creates a new public repository named `zen-3d-explainer-shorts` in the authenticated GitHub account and pushes this folder. To choose another name:

```bash
npm run publish:github -- my-3d-animation-style
```

It will refuse to overwrite existing Git history/remotes. If the name already exists, choose another name. It never asks you to paste a token into the repository. A text-only GitHub editor is unsuitable for uploading the complete 3,294-frame set; use Git or the helper above.

Once published, send Claude the actual repository URL and ask it to download the repository and read `CLAUDE.md` / `SKILL.md`. Until then, give Claude this ZIP directly.

## Measurement honesty

All native frames were decoded and measured. All 56 sequential contact sheets were visually inspected; selected frames were additionally inspected full-size. The study did not recover original meshes, animation curves, render settings or a trained voice. Exact source camera focal lengths, real-world construction dimensions, shader parameters and voice identity are unknown. Screen-space observations and reconstruction targets are labeled separately throughout.

The audio study uses automatic transcription and signal measurements. Subjective vocal timbre was not verified by direct listening in the analysis environment. The voice brief is an original casting target, not an identified/cloned reference voice.

## Licensing

New code and documentation: [MIT](LICENSE). Supplied videos and all derived frame/contact-sheet media: **reference material only, not covered by MIT**; their original rights remain with their respective owners. The included references display third-party branding; no affiliation is asserted. Generate original stories, branding, narration and output assets. See [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md) and [references/LICENSE-MEDIA.md](references/LICENSE-MEDIA.md).
