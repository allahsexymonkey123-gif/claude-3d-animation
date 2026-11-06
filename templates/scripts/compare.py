#!/usr/bin/env python3
"""Create honest side-by-side still comparisons; never warp a render to fit the reference."""
import argparse,pathlib
from PIL import Image,ImageOps,ImageDraw
ap=argparse.ArgumentParser();ap.add_argument('ours');ap.add_argument('reference');ap.add_argument('output');a=ap.parse_args()
canvas=Image.new('RGB',(1024,950),'#16161B');d=ImageDraw.Draw(canvas)
for x,p,label in [(0,a.reference,'REFERENCE'),(512,a.ours,'RECONSTRUCTION')]:
    im=Image.open(p).convert('RGB');im=ImageOps.contain(im,(512,910));canvas.paste(im,(x+(512-im.width)//2,40))
    d.text((x+12,12),label,fill='white')
pathlib.Path(a.output).parent.mkdir(parents=True,exist_ok=True);canvas.save(a.output)
