import {bundle} from '@remotion/bundler';
import {renderStill,selectComposition} from '@remotion/renderer';
import fs from 'node:fs';
import path from 'node:path';
const frames=(process.argv[2]??'0,135,270,359').split(',').map(Number);
if(frames.some(f=>!Number.isInteger(f)||f<0||f>=360))throw Error('Use integer demo frames 0..359');
fs.mkdirSync('out/stills',{recursive:true});
const serveUrl=await bundle({entryPoint:path.resolve('src/index.ts')});
const chromiumOptions={gl:'angle'};
const composition=await selectComposition({serveUrl,id:'DioramaShort',chromiumOptions});
for(const frame of frames){
  const output=`out/stills/f${String(frame).padStart(6,'0')}.png`;
  await renderStill({serveUrl,composition,output,frame,scale:.5,chromiumOptions});
  process.stdout.write(`${output}\n`);
}
