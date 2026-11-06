# Audio, narration and voice continuity

## What was and was not established

Both original videos include stereo HE-AAC audio at 44.1 kHz. Their soundtracks were decoded for ASR, 20 ms window measurements and FFmpeg EBU R128 loudness analysis. Automatic transcripts with word timestamps are included unchanged, explicitly marked `.auto.json`. The study did **not** verify subjective vocal timbre by direct listening in this analysis environment, identify a speaker/TTS provider, isolate music/SFX stems or recover a voice model. No exact actor, accent, synthesis settings or voice-clone asset is claimed.

The original tracks remain attached to the included MP4s so a capable production environment can listen directly before final casting. Keep that distinction clear when describing the package.

## Measured pacing and mix

| M metric | ref01 | ref02 |
|---|---:|---:|
| ASR words | 280 | 183 |
| Last ASR word ends | 66.38 s | 41.32 s |
| Words/s, from zero through last word | 4.218 | 4.429 |
| Equivalent words/min | 253.1 | 265.7 |
| Words/s using summed ASR word durations | 4.995 | 5.214 |
| Interword gaps >250 ms | 20 | 12 |
| 95th percentile ASR gap | .322 s | .359 s |
| Integrated mixed loudness | −14.3 LUFS | −14.2 LUFS |
| Loudness range | 1.7 LU | 1.6 LU |
| Mixed true peak | −.2 dBFS | +.6 dBFS |

Counts depend on the ASR tokenizer and can change after manual correction. The initial voice starts very near the beginning; the ASR start at 0.0 is not proof of a sample-exact onset. The summed-word-duration rate is not the target for writing a script, since it excludes pauses. Use the **4.2–4.4 words/s including pauses** range instead.

## Pitch and spectral limits

Autocorrelation candidates from the **mixed** mono track, with a .5 periodicity threshold and RMS gate, have approximate 10/50/90th percentiles of 120/160/258 Hz for ref01 and 126/167/267 Hz for ref02. The analyzer uses 50 ms windows every 20 ms. These values are affected by music, effects, octave errors and unvoiced speech. They cannot establish the actual speaker's identity, natural pitch range, emotional tone or gender. Do not directly use them as a voice-clone target.

## Original voice casting target (T)

Use one original narrator with clear conversational English and a steady mid-register delivery. A natural adult male read is a reasonable initial creative choice for a direct explanatory tone, but it is **a casting choice**, not an authenticated identification of the reference voice. Keep the same voice identity/accent/mic character between clips, unless the user asks for multiple speakers.

Read quickly but conversationally. Use ordinary contractions and simple causal sentences. Stress the newly introduced noun and the verb that explains what it does. Put short pauses at a failure→fix turn. Let the last phrase settle. Avoid a sales announcer, exaggerated animation voices, a musical cadence, whispering, shouted punchlines or robotic equal syllables.

Start with [voice-direction.txt](../../templates/audio/voice-direction.txt) and [voice-profile.json](../../templates/audio/voice-profile.json). Their values are new production defaults. Unknown reference provider/voice IDs remain `null`. Save the actual selected provider, voice ID, model version, rate and settings in the story's production manifest after a real voice has been chosen.

## Generation/recording workflow

1. Write the entire narration before rendering shots. Budget words from duration minus a small ending hold.
2. Generate or record one continuous take when possible. If separate sentences are needed, keep one voice configuration, leave short editing handles and normalize the joined take uniformly.
3. Listen to the actual take. Fix mispronunciation, rushed numbers, strange breaths or stressed wrong words before generating animation.
4. Transcribe the actual waveform to word-level timestamps and hand-correct important cues. Do not invent word durations from word count.
5. Export a dry `voice.wav` and checked `words.json`. Map shot/label/caption events to those words. Keep time in integer frames for picture and sample times for audio.
6. Keep the words intelligible. Shorten text or increase film duration before using strong time stretching.

No paid TTS call is made by this repository. Claude needs an available licensed voice tool or a user-provided recording to finish narration. It must report missing audio honestly rather than silently returning an unvoiced film.

## Sound design targets (T)

Use restrained physical cues: a light car roll/stop, a crack, granular fill, a short cut/jackhammer, paver clicks, rain, surface runoff, a pump hum and a quiet status accent. Use them only when supported by the new story. No default oompah/march score from the original repository.

Suggested initial balance: music 18–24 dB below voice and SFX 10–18 dB below voice during speech. These are original mix choices; actual source stem levels are unknown. Duck a continuous bed under narration, then raise it slightly only during meaningful gaps. Keep bass and tool noise from masking consonants.

Use 48 kHz WAV stems while producing. Target the final mix around −14.3 LUFS with a **−1 dBTP ceiling**. The reference's +.6 dBFS true peak is measured evidence, not a defect to reproduce. `mix.py` performs measured two-pass loudness normalization and optional sidechain ducking for a licensed bed. Check the final encoded file again for true-peak overshoot and audible artifacts.

## Delivery checks

Check actual audio presence, correct stream mapping, duration, first/last words, caption sync and end truncation. Listen to the complete final encoded film at normal speed. A waveform/loudness scan alone cannot assess vocal naturalness, exact pronunciation, music taste or perceptual voice matching.
