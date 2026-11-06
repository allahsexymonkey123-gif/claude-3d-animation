#!/usr/bin/env python3
"""Scan EVERY decoded frame for corruption, unintended freezes and gross exposure failures.

python templates/scripts/video_qa.py out/final.mp4 out/qa [expected_events.json]
Expected JSON: {"allowed_holds":[[0,60]],"allowed_flashes":[[120,125]]}.
All bounds zero-based/end-exclusive. Low motion is a diagnostic, not an automatic failure.
"""
import argparse,json,pathlib,subprocess
import cv2,numpy as np

def main():
    ap=argparse.ArgumentParser();ap.add_argument('video');ap.add_argument('out');ap.add_argument('events',nargs='?');a=ap.parse_args()
    out=pathlib.Path(a.out);out.mkdir(parents=True,exist_ok=True)
    meta=json.loads(subprocess.check_output(['ffprobe','-v','error','-show_streams','-show_format','-of','json',a.video]))
    v=next(s for s in meta['streams'] if s['codec_type']=='video');num,den=map(int,v['avg_frame_rate'].split('/'))
    cap=cv2.VideoCapture(a.video);prev=None;rows=[];black=[];white=[];exact=[]
    plan=json.loads(pathlib.Path(a.events).read_text()) if a.events else {}
    allowed=lambda f,key:any(lo<=f<hi for lo,hi in plan.get(key,[]))
    while True:
        ok,bgr=cap.read()
        if not ok:break
        f=len(rows);im=cv2.resize(bgr,(180,320),interpolation=cv2.INTER_AREA);gray=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
        mean=float(gray.mean()/255);diff=float(np.mean(np.abs(im.astype(float)-prev.astype(float)))) if prev is not None else None
        rows.append(dict(frame=f,mean_gray=mean,mean_difference=diff))
        if mean<.025:black.append(f)
        if mean>.95 and not allowed(f,'allowed_flashes'):white.append(f)
        if diff==0 and not allowed(f,'allowed_holds'):exact.append(f)
        prev=im
    cap.release()
    expected=int(v.get('nb_frames',len(rows)))
    r=dict(width=v['width'],height=v['height'],fps=num/den,decoded_frames=len(rows),metadata_frames=expected,
        black_frames=black,unplanned_white_frames=white,identical_frame_indices=exact,
        note='Identical/near-still frames can be intentional. Inspect them before changing motion.',
        format_ok=(num/den==30 and len(rows)==expected),per_frame=rows)
    if any(s['codec_type']=='audio' for s in meta['streams']):
        log=subprocess.run(['ffmpeg','-hide_banner','-i',a.video,'-af','ebur128=peak=true','-f','null','-'],capture_output=True,text=True,check=True).stderr
        (out/'loudness.txt').write_text(log[log.rfind('Summary:'):])
    (out/'qa.json').write_text(json.dumps(r,indent=2));print(json.dumps({k:x for k,x in r.items() if k!='per_frame'},indent=2))
    if not r['format_ok'] or black or white:raise SystemExit(1)

if __name__=='__main__':main()
