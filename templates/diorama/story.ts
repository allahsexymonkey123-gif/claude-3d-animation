export const FPS = 30;
export const TOTAL = 360;
export const clamp = (x: number) => Math.max(0, Math.min(1,x));
export const smooth = (x: number) => {x=clamp(x); return x*x*x*(x*(x*6-15)+10);};
export const ramp = (f: number, a: number, b: number) => smooth((f-a)/(b-a));
export const mix = (a: number,b: number,u: number) => a+(b-a)*u;
export type CaptionCue = {a: number; b: number; text: string; green?: string};
// 12-second ORIGINAL motion study, silent unless an external voice file is supplied.
// For real stories, replace these with manually verified voice-derived phrase boundaries.
export const CAPTIONS: CaptionCue[] = [
  {a:0,b:45,text:'Water needs a path',green:'path'},
  {a:45,b:90,text:'A solid surface blocks it',green:'blocks'},
  {a:90,b:135,text:'Open the ground'},
  {a:135,b:180,text:'Give it a channel',green:'channel'},
  {a:180,b:240,text:'Follow the route below',green:'route'},
  {a:240,b:300,text:'Then let it flow',green:'flow'},
  {a:300,b:360,text:'Keep the outlet clear',green:'clear'},
];
export const BEATS = [
  {a:0,b:90,name:'establish',camera:'front three-quarter',action:'plot and driveway held'},
  {a:90,b:150,name:'reveal',camera:'gentle push',action:'slab lifts as a rigid piece'},
  {a:150,b:240,name:'mechanism',camera:'continuous drift',action:'channel and route visible'},
  {a:240,b:330,name:'test',camera:'closer three-quarter',action:'water travels through route'},
  {a:330,b:360,name:'payoff',camera:'settle',action:'hold outlet and flowing water'},
];
