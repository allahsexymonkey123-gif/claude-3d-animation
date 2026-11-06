# Captions, headlines, labels and status graphics

## Measured samples

`../measurements/caption_samples.json` contains manually isolated caption ROIs, then exact bounding boxes of bright neutral text fill pixels (`min(R,G,B)>235`, channel spread <15). These boxes exclude the black stroke, shadow, green words and anti-aliased darker edges. They measure glyph ink, **not** CSS font size or the entire line box.

| M sample | White-fill bounding box, native pixels, x0/y0/x1/y1 | Fill size | Vertical region |
|---|---|---|---|
| ref01 f140, “and after a” | 123 / 573 / 351 / 602 | 228×29 | About 63.0–66.2% of H |
| ref02 f30, “down the hill” | 99 / 669 / 375 / 701 | 276×32 | About 73.5–77.0% of H |
| ref02 f500, “ground with a” | 88 / 669 / 385 / 709 | 297×40 | About 73.5–77.9% of H |

This is why one fixed caption baseline does not match both clips. The first clip's plan/sidewalk framing uses a higher caption band; the second clip leaves more lower soil space for speech captions. A word with a descender changes the fill height without implying a different font size.

## Caption rendering targets (T)

| Property | At 1080×1920 | At native 512-wide study scale |
|---|---:|---:|
| Font | Montserrat weight 800–900, approximation | Source font unknown |
| Font size | 70–88 px, start 76 | Roughly 33–42 px equivalent |
| Fill | `#FFFFFF` | White |
| Outline | 6–10 px charcoal `#111415` | Roughly 3–5 px |
| Shadow | Short, 2–4 px down, low blur/opacity | Small dark separation |
| Max width | 880–960 px | About 417–455 px |
| Alignment | Center | Center |
| Line height | 1.0–1.1 | Tight 1–2 line captions |
| Weight emphasis | Keep same font; use green | Do not enlarge every keyword |
| Positive/active accent | Start `#60DF79`, tune to frame | Source green varies with compression |

Use `paint-order: stroke fill` / WebKit text stroke or render a proper outlined text mask. Stroke should sit outside the white fill, not eat into it. Do not fake the outline with a huge blur glow. Prefer an open licensed font bundled in the project so rendering is repeatable. The included Montserrat font has its own OFL license.

The observed captions are **short phrases**, often 1–4 words, sometimes 5, rather than a compulsory one-word karaoke system. Highlight a concept such as “base,” “rebar,” “control,” “pavers,” “400 gallons,” “trench drain,” “overflows,” “pump,” “leaves,” “basket,” “power,” “battery” or the final resolution. These are examples of the role, not a vocabulary list for every story.

## Timing

Match caption start/end to checked voice word timings. Some reference swaps use a short opacity blend, visible over a few native frames; others read as direct changes. Use 2–5 frames of fade at most if matching that local example. Keep position and scale steady while a phrase is being read. Avoid constant spring/bounce/rotation, long fade-ins, moving words or an entire paragraph covering the mechanism.

Open ref01 sheets around f0–60 and f300–360 for phrase changes. Do not treat ASR segment boundaries as exact caption timing; the source phrase breaks do not always match the transcription's sentence segmentation.

## Opening hook

The headline occupies the upper central zone, typically a two-line uppercase phrase. White establishes the subject and green emphasizes the problem/result. Thick dark outlines keep it readable over the roof/hills. It is present for approximately the first three seconds and then leaves, making more room for the mechanism.

T starting layout: top 9–13% H, maximum 80–90% W, font about 72–86 px at 1080, weight 900, 0–1 px tracking, 1.0 line height. The exact source font/size is unknown. Write a new hook; do not copy the reference's headline or branded sign.

## Mechanism labels

Small labels name **parts**, and remain separate from the spoken captions. Observed design: black/dark rectangular or softly rounded plate, small bold uppercase white text, occasional thin green underline, white leader, green dot with pale rim at the endpoint. Examples include BASE, REBAR, CONTROL JOINTS, PIT, TRENCH DRAIN, LEAF BASKET, BATTERY BACKUP and CURB OUTLET.

T at 1080: 22–30 px type, 8–14 px horizontal padding, 5–9 px vertical padding, 2–4 px corner radius, 2–3 px leader, 8–12 px endpoint dot. Keep text horizontal to the screen even while anchored to a world point. Project the attachment point through the actual camera every frame. Let it fade or disappear if occluded/outside the frame; do not draw leaders through unrelated surfaces. Keep labels readable for at least 20–30 frames when they carry a new technical term.

The starter includes one simplified fixed label. Add a projected leader/endpoint and occlusion behavior to a final topic-specific scene; do not treat its fixed box as the completed labeling system.

## Failure/status stamps

ref02 uses red/white tilted stamps for failures such as FLOODED, NO PUMP and JAMMED, plus compact black status labels. Transfer that visual role with new wording appropriate to the story. Start a red stamp with a restrained 6–10 frame scale/opacity entrance, settle without ongoing vibration, hold briefly, then remove it. Avoid simultaneously covering the screen with a hook, a big stamp, three part labels and a caption.

## Accessibility and QA

Check at 512-wide playback. Caption outlines must remain separated from dark garage edges. Keep critical captions out of the bottom platform UI. Do not let a green word disappear into green grass: keep the charcoal outline. Check spelling, line wraps, descending letters, numerals, timing and any brand/domain text by reading actual rendered frames.
