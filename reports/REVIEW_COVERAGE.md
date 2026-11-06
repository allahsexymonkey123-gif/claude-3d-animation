# Review coverage and measurement ledger

All frame indices are zero-based. Ranges have exclusive ends.

| Reference | Video frames | Sequential 60-frame sheets | Original video bytes | Native cadence |
|---|---:|---:|---:|---|
| ref01 | 2049 | 35 | 41,700,720 | 30 fps, source PTS checked |
| ref02 | 1245 | 21 | 25,181,959 | 30 fps, source PTS checked |

## What every frame has

- An original native timestamp in `native_timestamps.csv`.
- A full-size 512×910 study JPEG and a sequential contact-sheet position.
- Display Y′ and saturation statistics, sharpness, image difference, histogram distance, optical-flow diagnostics and decoded-RGB SHA-256 in `per_frame.csv`.
- A manually reviewed semantic-beat association and available automatic transcript/word overlap in `frame_review_index.csv`.

## What was visually inspected

All 56 sequential contact sheets were inspected, covering every consecutive frame. Representative frames additionally opened at native size include ref01 f140/f800 and ref02 f30/f500. The review did not inspect every frame separately at native size. Pixel-level defects smaller than the contact-sheet thumbnails may remain unobserved. The original MP4s and full frame set are included so further checks can be made.

## What the sound analysis establishes

Automatic transcripts and timing, mixed-track periodicity candidates and objective loudness. It does not establish exact voice identity/provider, isolated stems or a perceptual timbre match. Direct listening to subjective voice timbre was not verified in the analysis environment.

## Reproduction

Run `templates/scripts/analyze_reference.py` against the included MP4s, preserving IDs. The supplied analyzer does not regenerate ASR; that optional step needs a speech model. After transcripts and native timestamp CSVs exist, `build_reference_index.py` regenerates the semantic index from its explicit manual beat table. Run `validate_repo.py` to check completeness.

## Sources of uncertainty

Compression, thumbnail review, caption interference in optical flow, changing subject coverage, ASR tokenization/timestamp error, and the non-uniqueness of reconstructing 3D from a rendered video. Physical units, source camera intrinsics, materials, easing curves and voice settings are reconstruction targets or unknowns.
