# Sources and style evidence

Technical sources were consulted on **6 November 2026**. They support the mechanism; the scene, wording, timings, layout and interface graphics are original planning choices. No source media is reused in a deliverable.

## Verified technical claims

| Claim used in the plan | Primary source | Scope and treatment |
|---|---|---|
| Bag tags provide machine-readable identification; optical tag scanning needs a readable line of sight. | [IATA — Baggage Tracking, Resolution 753 implementation guide, issue 4 (2023), §§6.5.1–6.5.3](https://www.iata.org/contentassets/5c4aa8b8b3b1432697d2bf3301450684/reso753-implementation-guide---2023_issue-4.0.pdf) | Supports identification and the readability problem. The plan chooses barcode scanning; it does not present RFID as mandatory. |
| A controller can determine a bag's sorting destination using baggage-source data and flight allocation. | [BEUMER Group — Routing & Sorting](https://www.beumergroup.com/products-systems/baggage-handling-technology/airport-software-suite/routing-sorting-ensuring-an-efficient-execution/) | Supports the number-to-record-to-flight association. The compact `ID → FLIGHT → BELT` display is an explanatory graphic, not a copied operational interface. |
| Failed reads can receive human attention using captured tag images and an operator-entered number or flight information. | [BEUMER Group — Video Coding](https://www.beumergroup.com/video-coding-airport/) | Supports an operator checking the captured image while a bag remains in the system. The precise waiting position and short duration are illustrative. Not every failed read is recoverable this way. |
| Photocells/light curtains provide tracking and position information; encoders measure conveyor speed. | [Datalogic — Baggage Handling Systems (Sorting), “Tracking and Control”](https://www.datalogic.com/eng/industries-applications/transportation-logistics/airports/baggage-handling-systems-(sorting)-ia-65.html) | Supports the tracking insert. The visible green status dot and ID marker are teaching overlays. |
| Conventional conveyor systems can use computer-controlled junctions/pushers to leave a bag on the main path or transfer it to another belt. Other airport architectures also exist. | [BEUMER Group — How did the baggage handling system develop and which systems are used in airports today?, “Conveyor technology”](https://www.beumergroup.com/knowledge/airport/how-did-the-baggage-handling-system-develop-and-which-systems-are-used-in-airports-today/) | Supports the chosen routing device. The plan's stop-and-push mechanism is simplified staging, not an installation design or throughput claim. |
| Sorting/make-up precedes transport and loading into the aircraft, with additional checks by handling staff. | [Virgin Atlantic — Loaded: Behind the scenes with baggage, “The laterals” and “At the aircraft side”](https://flywith.virginatlantic.com/gb/en/stories/loaded-behind-the-scenes-with-baggage.html) | A primary airline account of one airport's process. Supports ending at the flight's collection point with loading still ahead; no universal physical layout is asserted. |

No numerical capacity, sorting accuracy, airport-wide journey time, universal security sequence or “never loses a bag” claim is made. The miniature measures and motion windows are art direction, not engineering facts.

## Repository instructions read

`README.md`, `CLAUDE.md`, `SKILL.md`, `references/STYLE_BIBLE.md`, all eight linked reports on geometry, materials, lighting, motion, editing, captions, audio and QA; `templates/STORY_TEMPLATE.md`, `templates/SCRIPT_example.md`, `templates/story.schema.json`; `templates/audio/voice-direction.txt` and `voice-profile.json`; and `references/measurements/beat_timeline.json`.

## Reference images actually inspected

All paths below are relative to the root of this repository. The study images are included under `references/` and retain the separate reference-media notice.

| Inspected evidence | What was transferred |
|---|---|
| `references/frames/ref01/f000140.jpg` | Warm detailed architecture, blue focal object, contact shadows, textured ground depth and white outlined caption. |
| `references/frames/ref01/f000800.jpg` | Overhead layout that fills the portrait frame; temporary green emphasis attached to real geometry. |
| `references/frames/ref01/f000970.jpg` | Low section with a continuous top surface, depth and clear adjacent context. |
| `references/frames/ref02/f000030.jpg` | Opening two-line white/green hook over a complete miniature environment. |
| `references/frames/ref02/f000500.jpg` | Component scale, cutaway depth, compact part label, thin leader and green endpoint. |
| `references/sheets/ref01/sheet_000300.jpg`, `sheet_000360.jpg` | Consecutive depth-to-plan transition and stable read holds; geometry persists through the move. |
| `references/sheets/ref02/sheet_000420.jpg` | Consecutive failure-to-component reveal with recognizable architecture. |
| `references/sheets/ref02/sheet_000540.jpg` | Consecutive whole-route view after a mechanism reveal, with restrained camera motion. |

Other reference windows mentioned as principles in the shot plan, such as the final settle in ref02 f1185–1244, were read in the repository's reports and beat map, not directly inspected here. No original audio was listened to in this planning pass; the narrator brief is an original casting choice.
