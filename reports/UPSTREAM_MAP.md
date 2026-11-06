# How this repository follows the original

Source inspected: [mromidev/claude-animated-shorts](https://github.com/mromidev/claude-animated-shorts), pinned study commit `e3b817b6afc6cd413466d43f11ba31209e034bbf`. Retrieved 2026-11-06. The original is an MIT software/documentation repository with separately described reference media. Its bridge film uses flat outlined characters in a 3D environment; these supplied samples are full 3D architectural/mechanism explainers.

## Preserved structure and roles

| Original location | Original role | New equivalent |
|---|---|---|
| `README.md` | Install, contents, usage | `README.md`, with direct Claude prompt and publishing helper |
| `SKILL.md` | Complete agent pipeline | `SKILL.md`, rewritten for the supplied 3D style |
| `references/STYLE_BIBLE.md` | General visual/story formula | Same path, entirely new evidence and targets |
| `references/reports/` | Domain-specific measured reports | Same directory, new composition/material/light/motion/editing/text/audio/QA reports |
| `references/frames/` | Representative study frames | Same directory, expanded to every native frame of both clips |
| `references/sheets/` | Consecutive contact sheets | Same directory, all 56 native-30-fps sheets |
| `templates/bridge/` | Rendering/example scene source | `templates/diorama/`, an original full-3D starter |
| `templates/audio/` | Voice/music/SFX/mixing | Same directory, original voice brief/profile and measured loudness mixer |
| `templates/scripts/` | Stills, comparison, rendering/QA | Same directory, portable analysis/stills/compare/QA/integrity/publish helpers |
| `templates/SCRIPT_example.md` | Proven original story example | Same path, new conveyor example showing style transfer |
| `LICENSE` | MIT software/docs license | MIT for new code/docs, separate media notices |

## Code architecture examined

The upstream scene is divided into `Bridge.tsx` (composition/post pipeline), `world.ts` (world assembly/per-frame pose), `story.ts` (shots/camera/time), `build.ts` (3D environment), `paint.ts` (procedural textures), `lights.ts`/`shade.ts` (lighting/material response), `toon.ts`/`cast.ts`/`cardshade.ts` (drawn characters/cards), and `ink.ts`/`lensblur.ts`/`grade.ts` (post).

The new scene uses `DioramaShort.tsx` (composition/overlays/audio), `World.tsx` (lights/per-frame pose), `story.ts` (absolute-frame event timing), `camera.ts` (camera), `geometry.ts` (3D assets/material assembly) and `style.ts` (new palette/dimensions). This retains the useful separation of responsibilities without carrying over the old character or post-processing system.

The original audio folder separates timeline, DSP, instruments, music, SFX generation and mixing. The new version keeps sound tied to picture/voice timings, but does not copy the bridge-specific march score, crowd noises or hardcoded story events. Its mixer works from actual user-supplied original voice/optional licensed bed.

The original scripts support stills, side-by-side sheets, shot-table export, sandbox merge and full-frame QA. The new tools keep stills/comparison/full-frame QA and add original-file hashes, complete frame indexing, native timestamp evidence and a safe explicit GitHub publishing command. Sandbox merge scripts with user-specific filesystem paths are not carried over.

## Rules deliberately replaced

| Upstream-specific choice | Choice for these references |
|---|---|
| Flat bean-head cast/billboards | Solid 3D objects; no default people |
| Plum character ink and thick world edge pass | Material seams/trim, clean 3D silhouettes, no global thick ink |
| Strong lens blur/bloom recipe | Mostly sharp diagrams and restrained post |
| Historical factual anecdote/bridge formula | General visible causal mechanism |
| Approx. 3.7 words/s | Measured approx. 4.2–4.4 words/s including pauses |
| Bridge-specific 55–70 s duration | Duration from new brief; defaults remain a choice |
| No-caption user rule from that project | Captions/labels supported because they appear in these supplied references |
| March score and synthesized crowd | Original clear narration and restrained story-relevant SFX |
| Opus-only verification/agent naming | Renderer-neutral actual-output checks; no requirement for a particular model |

The old project's local paths, private reference videos, unrelated frame sets and unpublished user instructions are not included as new-style assets. The repo layout and production approach are credited in the notices; the supplied clips are the visual evidence for this kit.
