#!/usr/bin/env python3
"""Decode every native frame; save full frames, sequential sheets and auditable metrics.

python templates/scripts/analyze_reference.py VIDEO --id ref01 --root references
Requires ffmpeg, ffprobe, numpy, Pillow, opencv-python-headless, scipy.
All time/frame ranges are zero based, end exclusive. Measurements precede JPEG encoding.
"""
import argparse, csv, hashlib, json, math, pathlib, re, subprocess
import cv2
import numpy as np
from PIL import Image, ImageDraw
from scipy import signal

def run(args):
    return subprocess.run(args, check=True, capture_output=True)

def analyze(video, ident, root):
    video, root = pathlib.Path(video), pathlib.Path(root)
    frames, sheets, data = [root / d / ident for d in ('frames','sheets','measurements')]
    for p in (frames, sheets, data): p.mkdir(parents=True, exist_ok=True)
    meta = json.loads(run(['ffprobe','-v','error','-show_format','-show_streams','-of','json',str(video)]).stdout)
    stream = next(s for s in meta['streams'] if s['codec_type']=='video')
    w, h = stream['width'], stream['height']
    num, den = map(int, stream['avg_frame_rate'].split('/')); fps = num / den
    # No fps filter: every decoded native frame is retained. Reject VFR in the final validation.
    cmd = ['ffmpeg','-v','error','-i',str(video),'-map','0:v:0','-fps_mode','passthrough','-f','rawvideo','-pix_fmt','rgb24','-']
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE)
    rows, prev, prev_hist, prev_sha, thumbs, frame = [], None, None, None, [], 0
    candidates = []
    def save_sheet(start, imgs):
        cw,ch,label = 104,185,16
        sheet = Image.new('RGB',(cw*10,(ch+label)*6),'#141419'); d=ImageDraw.Draw(sheet)
        for j,im in enumerate(imgs):
            x,y=(j%10)*cw,(j//10)*(ch+label)
            sheet.paste(im.resize((cw,ch),Image.Resampling.LANCZOS),(x,y))
            d.text((x+2,y+ch+1),f'{start+j:04d} {(start+j)/fps:.2f}s',fill='#f5eb80')
        sheet.save(sheets/f'sheet_{start:06d}.jpg',quality=88)
    while True:
        raw = p.stdout.read(w*h*3)
        if not raw: break
        if len(raw)!=w*h*3: raise RuntimeError('Truncated raw frame')
        rgb=np.frombuffer(raw,np.uint8).reshape(h,w,3)
        im=Image.fromarray(rgb); im.save(frames/f'f{frame:06d}.jpg',quality=88,subsampling=0)
        small=cv2.resize(rgb,(128,228),interpolation=cv2.INTER_AREA)
        gray=cv2.cvtColor(small,cv2.COLOR_RGB2GRAY)
        hsv=cv2.cvtColor(small,cv2.COLOR_RGB2HSV)
        # Y' approximation in display encoded BT.709, NOT physical scene luminance.
        luma=small.astype(np.float32)@np.array([.2126,.7152,.0722],np.float32)/255
        hist=cv2.calcHist([hsv],[0,1],None,[24,16],[0,180,0,256]);cv2.normalize(hist,hist)
        sha=hashlib.sha256(raw).hexdigest()
        diff=histdist=flowmed=flow95=flowx=flowy=0.
        if prev is not None:
            diff=float(np.abs(small.astype(float)-prev.astype(float)).mean())
            histdist=float(cv2.compareHist(prev_hist,hist,cv2.HISTCMP_BHATTACHARYYA))
            flow=cv2.calcOpticalFlowFarneback(cv2.cvtColor(prev,cv2.COLOR_RGB2GRAY),gray,None,.5,3,15,3,5,1.2,0)
            mag=np.linalg.norm(flow,axis=-1)*(w/128)
            flowmed,flow95=map(float,np.percentile(mag,[50,95]))
            flowx,flowy=map(float,np.median(flow,axis=(0,1))*(w/128))
            if histdist>.22 and diff>12: candidates.append(frame)
        masked=luma[int(228*.20):int(228*.60)]
        rows.append(dict(frame=frame,time_s=round(frame/fps,6),raw_rgb_sha256=sha,
            mean_yprime=round(float(luma.mean()),6),p05_yprime=round(float(np.percentile(luma,5)),6),
            p95_yprime=round(float(np.percentile(luma,95)),6),mean_saturation=round(float(hsv[:,:,1].mean()/255),6),
            interior_yprime=round(float(masked.mean()),6),sharpness_laplacian=round(float(cv2.Laplacian(gray,cv2.CV_64F).var()),4),
            mean_rgb_difference=round(diff,5),histogram_distance=round(histdist,5),
            flow_median_source_px=round(flowmed,5),flow_p95_source_px=round(flow95,5),
            flow_x_median_source_px=round(flowx,5),flow_y_median_source_px=round(flowy,5),identical_to_previous=int(sha==prev_sha)))
        prev,prev_hist,prev_sha=small.copy(),hist,sha
        thumbs.append(im.resize((104,185)))
        if len(thumbs)==60: save_sheet(frame-59,thumbs);thumbs=[]
        frame+=1
    if thumbs: save_sheet(frame-len(thumbs),thumbs)
    if p.wait()!=0: raise RuntimeError('ffmpeg decode failed')
    with (data/'per_frame.csv').open('w',newline='') as f:
        writer=csv.DictWriter(f,fieldnames=rows[0].keys());writer.writeheader();writer.writerows(rows)
    fields=['mean_yprime','mean_saturation','mean_rgb_difference','flow_median_source_px','flow_p95_source_px','histogram_distance']
    summary=dict(id=ident,original_filename=video.name,sha256=hashlib.sha256(video.read_bytes()).hexdigest(),
        file_bytes=video.stat().st_size,width=w,height=h,fps=fps,frames=frame,duration_s=frame/fps,
        exact_duplicate_adjacent_frames=sum(r['identical_to_previous'] for r in rows),
        cut_candidates=candidates,cut_candidates_are_not_verified_edits=True,
        statistics={key:{f'p{pct:02d}':round(float(np.percentile([r[key] for r in rows[1:]],pct)),6) for pct in [5,25,50,75,95]} for key in fields})
    (data/'ffprobe.json').write_text(json.dumps(meta,indent=2))
    # Audio is a mixed track. Pitch candidates are not isolated speaker/voice-clone data.
    audio=run(['ffmpeg','-v','error','-i',str(video),'-map','0:a:0','-ac','1','-ar','16000','-f','f32le','-']).stdout
    x=np.frombuffer(audio,np.float32);hop,n=320,800; audio_rows=[]
    for start in range(0,len(x)-n,hop):
        a=x[start:start+n].astype(float);rms=float(np.sqrt(np.mean(a*a))); a-=a.mean()
        ac=signal.fftconvolve(a,a[::-1],mode='full')[n-1:]; ac/=max(ac[0],1e-12)
        low,high=40,228
        peaks=signal.find_peaks(ac[low:high])[0]+low
        lag=int(peaks[np.argmax(ac[peaks])]) if len(peaks) else 0
        periodicity=float(ac[lag]) if lag else 0
        candidate=16000/lag if lag and periodicity>.5 and rms>.01 else 0
        audio_rows.append(dict(time_s=round(start/16000,4),rms_dbfs=round(20*math.log10(max(rms,1e-9)),3),
            mixed_track_f0_candidate_hz=round(candidate,3),periodicity=round(periodicity,4)))
    with (data/'audio_windows.csv').open('w',newline='') as f:
        writer=csv.DictWriter(f,fieldnames=audio_rows[0]);writer.writeheader();writer.writerows(audio_rows)
    measured=subprocess.run(['ffmpeg','-hide_banner','-i',str(video),'-map','0:a:0','-af','ebur128=peak=true','-f','null','-'],capture_output=True,text=True,check=True).stderr
    (data/'audio_loudness.txt').write_text(measured[measured.rfind('Summary:'):])
    summary['audio']=dict(sample_rate_analysis=16000,source_sample_rate=next(s['sample_rate'] for s in meta['streams'] if s['codec_type']=='audio'),
        mixed_track_pitch_caveat='Autocorrelation candidates from mixed speech/music/SFX; not a verified speaker fundamental or a voice identity.')
    (data/'summary.json').write_text(json.dumps(summary,indent=2))
    print(json.dumps(summary,indent=2),flush=True)

if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('video');ap.add_argument('--id',required=True);ap.add_argument('--root',default='references')
    a=ap.parse_args();analyze(a.video,a.id,a.root)
