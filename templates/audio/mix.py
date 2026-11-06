#!/usr/bin/env python3
"""Mix an original voice with optional licensed bed; two-pass measured loudness normalization.

python templates/audio/mix.py voice.wav out/mix.wav [--bed licensed-bed.wav]
This does not call a paid TTS service or reuse the reference soundtrack.
"""
import argparse,json,pathlib,re,subprocess,tempfile
ap=argparse.ArgumentParser();ap.add_argument('voice');ap.add_argument('output');ap.add_argument('--bed');a=ap.parse_args()
pathlib.Path(a.output).parent.mkdir(parents=True,exist_ok=True)
with tempfile.TemporaryDirectory() as tmp:
    raw=pathlib.Path(tmp)/'premix.wav';cmd=['ffmpeg','-v','error','-y','-i',a.voice]
    if a.bed:
        cmd+=['-stream_loop','-1','-i',a.bed,'-filter_complex',
          '[0:a]aresample=48000,asplit=2[v][side];[1:a]aresample=48000,volume=0.12[m];[m][side]sidechaincompress=threshold=0.025:ratio=5:attack=20:release=250[duck];[v][duck]amix=inputs=2:duration=first:normalize=0[out]',
          '-map','[out]']
    else:cmd+=['-af','aresample=48000']
    cmd+=['-ac','2','-c:a','pcm_s24le',str(raw)];subprocess.run(cmd,check=True)
    target='loudnorm=I=-14.3:TP=-1.0:LRA=3'
    log=subprocess.run(['ffmpeg','-hide_banner','-i',str(raw),'-af',target+':print_format=json','-f','null','-'],capture_output=True,text=True,check=True).stderr
    match=re.findall(r'\{\s*"input_i".*?\}',log,re.S)
    if not match:raise RuntimeError('loudnorm did not return measurements')
    m=json.loads(match[-1]);fields={'measured_I':'input_i','measured_LRA':'input_lra','measured_TP':'input_tp','measured_thresh':'input_thresh','offset':'target_offset'}
    params=':'.join(f'{k}={m[v]}' for k,v in fields.items())
    subprocess.run(['ffmpeg','-v','error','-y','-i',str(raw),'-af',target+':'+params+':linear=true','-ar','48000','-c:a','pcm_s24le',a.output],check=True)
print(a.output)
