#!/usr/bin/env python3
"""Join measured frame data, manually reviewed semantic beats and automatic voice timing.

Run after analyze_reference.py for the included two references. The beat table is a
manual semantic review, not an automatic hard-cut detector or individual full-res audit.
"""
import csv,json,pathlib
ROOT=pathlib.Path(__file__).resolve().parents[2]/'references'

BEATS={
 'ref01':[
  (0,90,'establish','House/driveway establishment; opening comparison hook; surface appears.'),
  (90,224,'load-and-failure','Closer house view; blue car enters/parks; slab sinks and crack appears.'),
  (224,350,'base-section','Move into low section; dirt removed; granular base and top slab revealed; BASE label.'),
  (350,478,'shrink-crack','Move overhead; drying/shrink demonstration; fixed middle crack grows.'),
  (478,589,'rebar-reveal','Return oblique; concrete reveals aligned steel mesh; REBAR label.'),
  (589,717,'rebar-limit','Return overhead; steel disappears beneath concrete; cracks remain and branch.'),
  (717,839,'control-joint-layout','Cut lines across slab; split squares; temporary green explanatory tint.'),
  (839,932,'control-joint-label','CONTROL JOINTS label; spacing example and additional crack.'),
  (932,1050,'sidewalk-example','Sweep across tree to horizontal sidewalk section; mint joints and localized cracks.'),
  (1050,1120,'return-to-grid','Return to familiar overhead driveway grid.'),
  (1120,1240,'root-lift','Move lower oblique; root grows from left; one thick panel lifts.'),
  (1240,1285,'trip-edge','Push to lifted panel edge; TRIP EDGE leader label.'),
  (1285,1320,'jackhammer','Tool enters; local vibration and crack/break preparation.'),
  (1320,1370,'remove-and-patch','Rigid pieces separate; root removed; replacement patch fills opening.'),
  (1370,1398,'new-patch-label','NEW PATCH label; mismatched concrete example.'),
  (1398,1492,'smaller-grid','Return overhead; large slab grid becomes finer square grid.'),
  (1492,1540,'paver-pattern','Top surface changes to modular terracotta/tan pavers.'),
  (1540,1649,'sand-section','Move to section; sand and base layers; SAND/PAVERS labels.'),
  (1649,1707,'local-paver-lift','Move oblique; root lifts local pavers, neighboring blocks retain grid.'),
  (1707,1770,'remove-trim-return','A few pavers rise/move; root trimmed; same positions refilled.'),
  (1770,1808,'return-wide','Return to recognizable house/driveway; next explanatory payoff.'),
  (1808,1860,'car-and-strength-label','Car enters/parks; small strength claim label in the supplied reference.'),
  (1860,1930,'payoff-push','Closer view around parked car and completed pavers.'),
  (1930,2049,'joint-emphasis-ending','Paver joints emphasize separation; final phrase and settling hold.')
 ],
 'ref02':[
  (0,90,'establish','Modern house, sloping drive, pavers assemble; opening flooding headline.'),
  (90,195,'rain-and-count','Title leaves; rain starts; count graphic rises; runoff moves toward house.'),
  (195,224,'flood-failure','FLOODED stamp appears over water at house.'),
  (224,294,'trench-install','Storm resets; drain cut/installed across lower driveway.'),
  (294,350,'trench-label','TRENCH DRAIN label and leader; mechanism named.'),
  (350,395,'lowest-spot','LOWEST SPOT status; rain/flow resumes in same scene.'),
  (395,445,'overflow','Water pools/overflows at garage; no invented camera cut.'),
  (445,475,'pit-opening','Push close to underground section; connecting inlet/pit opening appears.'),
  (475,510,'pit-and-pump','PIT leader; recessed section and blue pump are revealed.'),
  (510,531,'return-pipe','Discharge/return pipe emerges connected to pump.'),
  (531,625,'whole-route','Pull wider; water fills and pumps along visible route toward street.'),
  (625,665,'sump-label','SUMP PUMP label; route held for reading.'),
  (665,725,'missing-pump','Return wide; NO PUMP red/white stamp.'),
  (725,753,'looks-done','LOOKS DONE label, held before first storm.'),
  (753,774,'first-storm','Brief white flash and renewed rain/flow, same geometry.'),
  (774,820,'leaves','Move closer; leaves travel into drain with surface water.'),
  (820,885,'jam','JAMMED stamp and continued local rain/flow.'),
  (885,976,'leaf-basket','LEAF BASKET label; leaves collect before the hidden mechanism.'),
  (976,1000,'power-storm','Repeated short flashes, followed by power failure state.'),
  (1000,1078,'power-out','POWER OUT label, route and house remain aligned.'),
  (1078,1128,'battery-backup','BATTERY BACKUP label and leader; new reliability feature.'),
  (1128,1185,'curb-outlet','Reframe to curb; visible blue discharge; CURB OUTLET label.'),
  (1185,1245,'evening-payoff','Water continues toward outlet; evening sky/windows; final resolved caption.')
 ]
}

def main():
    timeline={key:[dict(start=a,end=b,id=name,observation=text,range_status='Manual semantic range; not a hard-cut or recovered keyframe boundary') for a,b,name,text in beats] for key,beats in BEATS.items()}
    (ROOT/'measurements/beat_timeline.json').write_text(json.dumps(timeline,indent=2))
    fields=['reference','frame','native_pts_s','study_frame','sequential_sheet','semantic_beat','beat_observation','active_asr_words','asr_segment','review_method']
    rows=[]
    for ident,n in [('ref01',2049),('ref02',1245)]:
        tx=json.loads((ROOT/f'measurements/{ident}/transcript.auto.json').read_text())
        segs=tx['segments'];words=[w for s in segs for w in s['words']]
        stamps=list(csv.DictReader((ROOT/f'measurements/{ident}/native_timestamps.csv').open()))
        assert len(stamps)==n
        assert timeline[ident][0]['start']==0 and timeline[ident][-1]['end']==n
        assert all(timeline[ident][i]['end']==timeline[ident][i+1]['start'] for i in range(len(timeline[ident])-1))
        for f in range(n):
            t=float(stamps[f]['source_pts_s']);beat=next(b for b in timeline[ident] if b['start']<=f<b['end'])
            active=''.join(w['word'] for w in words if w['start']<=t<w['end']).strip()
            seg=next((s['text'].strip() for s in segs if s['start']<=t<s['end']),'')
            rows.append(dict(reference=ident,frame=f,native_pts_s=stamps[f]['source_pts_s'],study_frame=f'frames/{ident}/f{f:06d}.jpg',
                sequential_sheet=f'sheets/{ident}/sheet_{f//60*60:06d}.jpg',semantic_beat=beat['id'],beat_observation=beat['observation'],
                active_asr_words=active,asr_segment=seg,review_method='Every-frame numeric scan + visual sequential contact-sheet review; beat-range semantic note; selected native-size stills'))
    with (ROOT/'measurements/frame_review_index.csv').open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=fields);w.writeheader();w.writerows(rows)
    sources=[json.loads((ROOT/f'measurements/{id}/summary.json').read_text()) for id in ['ref01','ref02']]
    manifest=dict(version='1.0.0',created='2026-11-06',upstream=dict(url='https://github.com/mromidev/claude-animated-shorts',
        commit='e3b817b6afc6cd413466d43f11ba31209e034bbf',role='Structural/workflow reference; not the new visual style'),
        sources=sources,review=dict(total_native_frames=3294,total_sequential_sheets=56,sequential_sheets_inspected=56,
          all_frames_numerically_analyzed=True,native_30fps_timestamps_verified=True,
          visual_method='All consecutive frames viewed on 60-frame sheets; representative native-size stills additionally inspected. Not all frames inspected separately full-size.',
          audio_method='Automatic word-timed transcription, mixed-track autocorrelation and EBU R128 analysis; subjective timbre not verified by direct listening.',
          selected_native_stills={'ref01':[140,800],'ref02':[30,500]},
          unknowns=['source meshes/UVs','real-world dimensions','source camera intrinsics','source easing curves','renderer/shader settings','voice identity/provider/preset','isolated music/SFX stems']),
        rights=dict(code_docs='MIT',reference_media='Original rights retained; see references/LICENSE-MEDIA.md',font='SIL OFL; see public/fonts/OFL.txt'))
    (ROOT/'manifest.json').write_text(json.dumps(manifest,indent=2))
    print(f'Indexed {len(rows)} frames and {sum(len(v) for v in timeline.values())} semantic ranges')

if __name__=='__main__':main()
