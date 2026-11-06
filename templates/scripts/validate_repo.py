#!/usr/bin/env python3
"""Validate the portable repository, complete frame coverage, source hashes and links."""
import csv,hashlib,json,pathlib,re,subprocess,sys
root=pathlib.Path(__file__).resolve().parents[2]
errors=[]
for ident,n in [('ref01',2049),('ref02',1245)]:
    summary=json.loads((root/f'references/measurements/{ident}/summary.json').read_text())
    frames=sorted((root/f'references/frames/{ident}').glob('f*.jpg'))
    if len(frames)!=n:errors.append(f'{ident}: expected {n} frames, got {len(frames)}')
    if [p.name for p in frames]!=[f'f{i:06d}.jpg' for i in range(n)]:errors.append(f'{ident}: frame sequence has gaps')
    rows=list(csv.DictReader((root/f'references/measurements/{ident}/per_frame.csv').open()))
    if len(rows)!=n or [int(r['frame']) for r in rows]!=list(range(n)):errors.append(f'{ident}: CSV frame coverage')
    media=root/f'references/videos/{ident}.mp4'
    if not media.exists() or hashlib.sha256(media.read_bytes()).hexdigest()!=summary['sha256']:errors.append(f'{ident}: original video hash mismatch')
    if summary['fps']!=30 or summary['frames']!=n:errors.append(f'{ident}: invalid measured format')
    expected=(n+59)//60
    if len(list((root/f'references/sheets/{ident}').glob('sheet_*.jpg')))!=expected:errors.append(f'{ident}: sequential sheets missing')
for p in list(root.glob('*.md'))+list((root/'references').rglob('*.md')):
    for target in re.findall(r'\]\(([^)]+)\)',p.read_text()):
        if '://' in target or target.startswith('#'):continue
        q=(p.parent/target.split('#')[0])
        if not q.exists():errors.append(f'{p.relative_to(root)}: broken link {target}')
for p in root.rglob('*.py'):
    if 'node_modules' not in p.parts:compile(p.read_text(),str(p),'exec')
manifest=json.loads((root/'references/manifest.json').read_text())
if manifest['review']['sequential_sheets_inspected']!=56:errors.append('Review coverage changed')
if errors:
    print('\n'.join(errors));sys.exit(1)
print('PASS: 2 original hashes, 3294 frames, 56 sheets, CSV coverage, Markdown links and Python syntax')
