# Visual and voice production directions

## Visual target and transfer

Build a real 3D miniature terminal, with the baggage mechanism inside the same continuous architecture. The airport setting replaces the source driveway; the borrowed grammar is a familiar exterior, a physical cutaway, a useful overhead, a lower mechanism insert and a resolved wide. Do not turn the plan into flat arrows on a house, a character skit or a montage of disconnected machine images.

Warm off-white plaster and lightly mottled concrete carry the architecture. Use blue-gray terminal glazing with broad reflection strips, a few muted terracotta service panels and dark charcoal rubber belts. Put saturated faceted green shrubs and one small tree outside the terminal edge. Expose a brown soil cut face below the concrete base with sparse embedded stones; it continues below the picture crop, rather than making a little floating island. These exterior accents anchor the repository's color hierarchy without pretending airport machinery is landscaping.

The blue hero bag is the focal object, drawing on the reference's saturated blue vehicle. Keep other luggage tan/brown and the surrounding structure subdued. Use temporary green accents for a named part, a resolved route or an ID association. A thin green line is a diagram overlay, not a physical light cable or a force that carries luggage.

The source's exact meshes, shaders, camera settings and voice were not recovered. All dimensions, materials, light values and camera angles below are reconstruction choices for this original scene.

## World and asset registry

Use scene metres, Y up. Main belt travel is toward decreasing Z; the Flight 24 branch travels toward increasing X. Overhead composition maps upstream to the bottom of the frame, Flight 17 to the top and Flight 24 to the right. Keep this map through every reframe.

| Object ID | Proposed dimensions / placement | Parent, attachment and pivot | Material / fixed identity | Initial → final state |
|---|---|---|---|---|
| `terminal` | Approx. 14 m wide × 16 m deep, roof at Y=4.2; ground slab top at Y=0 | World origin; doors, glazing and signs are fixed children | Rough warm off-white, blue-gray glass, rust service panel | Same architecture throughout |
| `base_section` | Slab 0.25 m thick; soil extends below Y=−4 and out of the lower crop | World; top and cut face share an edge | Concrete, brown soil, seeded stones | Remains fixed; never made transparent to fake depth |
| `roof_reveal` | Independent half-roof panel with real thickness | Local rest transform saved; rigid vertical lift by 3 m, no scaling | Same roof finish and shadow as terminal | Closed → raised outside active view by f84 |
| `near_wall_cutaway` | Clearly bounded near-wall panel | Separate mesh; reveal only this cut face | Matching plaster; section edge retained | Opaque → removed/faded as an illustrative cutaway, f58–84 |
| `main_belt` | Width 1.05 m, deck Y=0.9; X=0, Z=+6 to −6 | Fixed frame; rollers and motor fixed at defined axes | Matte charcoal rubber, dull gray frame | Runs toward −Z; local hold f458–529 during transfer |
| `flight24_branch` | Width 1.05 m, same deck height; X=+0.53 to +4.5 at Z=−1 | Fixed to main-belt junction; receiving roller gap visibly small | Same machinery family | Runs toward +X; hero stops at a physical end stop |
| `flight17_output` | Main belt continues to Z=−6 | Fixed; its sign is not a baggage-claim sign | Neutral plate `FLIGHT 17` | Tan bag continues along this path |
| `hero_bag` | 0.72 m long (Z) × 0.47 m wide (X) × 0.32 m high; laid on broad face | Rigid body root; handle, tag, seams and wheels stay attached | Saturated blue, approx. displayed target `#0D54A2`; white tag; ID alias `…0317` | Inlet → held for read recovery → tracked → right branch → Flight 24 collection |
| `comparison_bag` | 0.62 × 0.43 × 0.30 m; ahead of hero with visible spacing | Separate stable root and attached tag | Warm tan, ID alias `…0842`, FLIGHT 17 | Main belt → straight-through output |
| `hero_tag` | Approx. 0.16 × 0.05 m physical white strip, attached to handle | Fixed attachment; optional small, deterministic bend | Illustrative barcode and ID; never changes number | Barcode partially obscured, human-readable number available in captured image |
| `tag_reader` | Warm off-white portal, lenses above and beside inlet belt | Fixed portal at Z≈+4; label anchor on its casing | Rough body, dark lenses; no glowing scanner beam required | Scan attempt → no-read result |
| `operator_station` | Small screen and keyboard immediately beside scan zone | Fixed terminal-side mounting | Dark bezel, restrained blue-gray screen | Captured tag image → operator confirmation; no auto-resolving UI implied |
| `position_sensor` | Photocell pair at Z≈+0.8, above belt edge | Emitter/receiver fixed to opposite rails | Small blue-gray casing, green status dot only when active | Real bag crossing changes status |
| `encoder` | Small wheel at a visible drive roller | Fixed shaft axis; rotation derives from belt travel | Dull steel and black rubber | Rotation agrees with cumulative belt displacement and stops during hold |
| `diverter` | Approx. 0.9 m long × 0.30 m high plate, 0.10 m thick; stroke ≈1.4 m | Actuator fixed on −X side at Z=−1; plate translates along +X, preserves contact plane | Off-white casing, dark rubber contact face; mechanism exposed at one side | Fully retracted → contact and side push → fully retracted |
| `flight24_makeup` | Branch endpoint at X≈+4.5, deck Y=0.9; broad collection area | Fixed end stop and world-mounted `FLIGHT 24` sign | Same belt and neutral architecture | Empty → hero bag arrives and settles |
| `trolley` | Small baggage trolley parked next to collection area | Fixed during this story; real wheels and ground shadow | Muted gray, no airline branding | Parked; no self-loading or drive-away animation |

These dimensions exaggerate sensor visibility and simplify travel distances. Enlarge the **screen insert**, not the physical tag, for readability. Show the number alias `…0317` linked to Flight 24 and `…0842` to Flight 17, so nobody infers that the ID's last digits encode the flight. Barcode art is schematic, not a supplied machine-readable asset. The operator monitor is an in-scene diagram of a real human check; it is not a claim about a particular airport's interface.

## Geometry, materials and light

Model primary shapes first, then useful seams, handles, rollers and mounting brackets. Keep the hero bag's silhouette, proportions, tag attachment and seam pattern identical through all views. Give the terminal slabs, roof and belt rails actual thickness. Belt rollers must contact the belt; every moved bag stays on a supporting surface. The pusher's actuator remains attached to its fixed housing through its full stroke.

Start roughness around .8–.95 for plaster/concrete, .65–.85 for bag fabric, .75 for rubber and .25–.4 for glass. Treat these as shader starting values and tune rendered pixels, rather than treating displayed reference hex colors as recovered base colors. Use subtle seeded fine texture; avoid crawling noise, polished plastic luggage and chrome machinery. Do not add a global black world-outline pass.

Use a broad daylight key from above/front-left and soft neutral/pale-blue fill. Keep dark belt forms legible against the machinery while pale architecture retains detail. Contact shadows seat bags on belts and show the pusher touching the suitcase. Moderate contact AO, crisp antialiasing, no film grain, no global bloom, no strong depth of field. One color-management and exposure setup serves every view. A bright industrial interior can be achieved with ambient fill; avoid a nighttime lighting change in this short runtime.

## Motion and camera execution

Keep all geometry, camera poses, belt offsets, sensor states, UI transitions and bag positions a pure function of absolute frame number. Seed any texture or stone variation once. No integrated state that depends on previously rendered frames, random movement per frame or 12 fps stepped motion.

Use the named camera states and frame windows in [SHOT_PLAN.md](SHOT_PLAN.md). At each handoff the new camera starts from the previous pose, with zero roll and a smooth ease that settles. A quintic smootherstep is a suitable implementation choice, not an assertion about the reference renderer. Adjacent moves take 8–18 frames here; larger plan/section moves take 24. Preserve orientation, material boundaries and architectural anchors. Don't orbit while the pusher transfer is being explained.

Conveyor travel uses a stable path parameter measured by arc length. Acceleration at a hold/release is eased over a few frames. Drive roller rotation and belt texture offsets derive from the same travel function. The blue bag's ID marker follows its rigid-body position, while the underlying belt pattern continues independently. The tan bag is clear of the junction before the hero's transfer; keep other incoming bags outside the short accumulation area so the staged pause creates no collisions.

For the side transfer, the local main belt stops with the blue bag centered at Z=−1. The paddle approaches the bag's −X face, makes visible contact, then translates it onto the branch without crossing through the bag or floor. Keep the receiving surface coplanar. After transfer, the paddle retracts before the main belt resumes. The branch carries the bag away from the junction; it decelerates into the collection area's end stop without bouncing. This stop-and-push staging is illustrative, not a recovered specification for an installed sorter.

The shot plan's contact at about f485 is provisional. Once a voice is recorded, move it close to the checked word “pushes”; do the same for ID confirmation, match, sensor crossing and arrival. Preserve cause before consequence. If the 98-word take cannot fit naturally, shorten wording within the same meaning before stretching the recording; maintain 720 total frames and at least 15 final silent frames, with 30 preferred.

## Typography and overlays

Use the repository's bundled Montserrat ExtraBold/Black as an approximation. At 1080 width, start spoken captions at 76 px, weight 800–900, 8 px outside charcoal outline `#111415`, white fill and a subtle 3 px downward shadow. Keep max width about 900 px, one or two lines, tight 1.05 line height. Green starts at `#60DF79` and keeps the same outline. Test at 512-wide playback; resize/rewrap a long chunk rather than reducing it until unreadable.

Part labels start at 28 px uppercase white on a compact charcoal plate with a 2–3 px white leader and 10 px green endpoint dot. Project endpoints from actual world coordinates each frame. If a component is offscreen or occluded, hide its leader. Keep new labels visible for at least 30 frames. Use a restrained 6-frame entrance for the red/white `NO READ` stamp and remove it before confirmation. No reference logos, brand signs, copied narration or copied source media belong in the original output.

## Narrator and recording direction

Use one original adult narrator with clear General American English and a steady mid-register. Deliver quickly, plainly and with curiosity. Start immediately, keep clean consonants and brief breaths, and preserve natural stress rather than fitting every syllable to a metronome. “Correct flight,” “unique number,” “operator,” “matches,” “track,” “timed diverter” and “identity” are useful stresses. Give the final sentence a small downward cadence.

The target is about 4.26 spoken words/second over 23 seconds, **including** its short internal pauses. Avoid a sales pitch, trailer voice, shouted reveal, multiple characters or an imitation/clone of the reference speaker. The source speaker and provider are unknown; the voice identity in this plan is a new casting direction. Record a single continuous dry take where possible. Actual provider, voice ID, settings and performer license must be recorded only after selection, not invented here.

Before locking picture, listen to the complete take and correct pronunciation, breaths and stress. Obtain actual word timings from that waveform and manually correct key causal words. Save the real dry voice and checked timings during production; do not manufacture a `words.json` from this written frame budget.

## Sound and final production targets

Use a restrained conveyor hum, one scan tick, a couple of operator key taps, a soft confirmation latch, a quiet sensor cue and the physical pusher slide/contact. Avoid noisy airport announcements or voices that compete with the narrator. Music is optional; the default plan needs no score. If added, choose an original/licensed unobtrusive bed and begin about 18–24 dB under voice. Start SFX about 10–18 dB below speech and judge by listening.

Produce 48 kHz WAV stems. Target the eventual encoded mix around −14.3 LUFS integrated, with a −1 dBTP ceiling; do not reproduce the source's peak overshoots. The last spoken word finishes by f690 and the bed tails down through the final hold. Only make claims about actual loudness after measuring the export.

Future render target: 1080 × 1920, native 30 fps, exactly 720 frames/24 seconds, SDR Rec.709/sRGB, H.264 yuv420p, CRF 16–18. Typography is composited after the 3D image. Before a full movie, inspect a wide, a plan, a scanner insert, a sensor section, pusher contact and the final frame. Check consecutive frames through each move and transfer, plus selected frames rendered in shuffled order. Those rendering and audio checks are future production work, not checks completed for this planning request.
