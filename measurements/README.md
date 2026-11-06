# Measurement files

`ref01` is the 68.3-second paver/concrete reference. `ref02` is the 41.5-second drainage reference.

- `per_frame.csv`: every decoded frame, raw-RGB hash, display Y′/saturation/sharpness/difference/histogram/flow diagnostics.
- `native_timestamps.csv`: actual source presentation timestamps. Both sequences were checked for consecutive 1/30-second intervals.
- `summary.json` / `ffprobe.json`: measured format, original-file SHA-256 and stream metadata.
- `audio_windows.csv`: 50 ms mixed-track RMS/periodicity windows every 20 ms; pitch candidates are not isolated speaker measurements.
- `audio_loudness.txt`: FFmpeg EBU R128 summary from the original mixed soundtrack.
- `transcript.auto.json`: automatic English transcription and word times, not manually certified word-perfect text.
- `beat_timeline.json`: explicit manual semantic intervals; a boundary is not automatically a hard camera cut.
- `frame_review_index.csv`: all 3,294 frames joined to sheet/beat/automatic voice timing.
- `palette_samples.json`: ROI boxes and sampled displayed median colors.
- `caption_samples.json`: bright white caption-fill bounding boxes in isolated ROIs.

All frame indices are zero-based. Time is seconds. Ranges are end-exclusive. See the analyzer source and review-coverage report for thresholds, resolution, methods and limits. Do not infer original shaders, camera intrinsics, exact physical dimensions or a voice identity from these measurements.
