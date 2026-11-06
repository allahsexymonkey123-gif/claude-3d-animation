import React,{useEffect,useState} from 'react';
import {ThreeCanvas} from '@remotion/three';
import {AbsoluteFill,Audio,staticFile,useCurrentFrame,delayRender,continueRender,cancelRender} from 'remotion';
import * as THREE from 'three';
import {World} from './World';
import {COLORS as C,SPEC} from './style';
import {CAPTIONS} from './story';

export type ShortProps = {captions: boolean;labels: boolean;title: string;voice: string|null};
export const DioramaShort: React.FC<ShortProps> = ({captions,labels,title,voice}) => {
  const f=useCurrentFrame(),cue=CAPTIONS.find(c=>f>=c.a&&f<c.b);
  const [fontHandle]=useState(()=>delayRender('Montserrat font'));
  useEffect(()=>{document.fonts.load('900 60px Montserrat').then(()=>continueRender(fontHandle)).catch(cancelRender);},[fontHandle]);
  return <AbsoluteFill style={{background:C.sky}}>
    <style>{`@font-face {font-family: Montserrat;src:url('${staticFile('fonts/Montserrat-Variable.ttf')}') format('truetype');font-weight:100 900;} .zen-type {font-family:Montserrat,Arial,sans-serif!important;}`}</style>
    <ThreeCanvas width={1080} height={1920} shadows
      camera={{fov:34,near:.1,far:180,position:[11,18,32]}}
      gl={{antialias:true,toneMapping:THREE.ACESFilmicToneMapping,toneMappingExposure:1.05}}
    ><World/></ThreeCanvas>
    {title&&f<72&&<div className="zen-type" style={{position:'absolute',top:180,left:80,right:80,textAlign:'center',
      fontFamily:'Arial, sans-serif',fontWeight:900,fontSize:62,lineHeight:1.02,color:'white',
      WebkitTextStroke:'9px #111415',paintOrder:'stroke fill',textTransform:'uppercase'}}>{title}</div>}
    {labels&&f>=150&&f<330&&<div className="zen-type" style={{position:'absolute',left:125,top:1320,color:'white',
      background:'#111415',padding:'9px 16px',fontFamily:'Arial, sans-serif',fontWeight:800,fontSize:25,letterSpacing:1}}>DRAINAGE ROUTE</div>}
    {captions&&cue&&<div className="zen-type" style={{position:'absolute',left:70,right:70,top:1920*SPEC.overlay.captionY,
      textAlign:'center',fontFamily:'Arial, sans-serif',fontSize:SPEC.overlay.captionFont,fontWeight:900,
      lineHeight:1.08,color:'white',WebkitTextStroke:`${SPEC.overlay.captionStroke}px ${C.captionStroke}`,
      paintOrder:'stroke fill',textShadow:'0 3px 2px #0005'}}>
      {cue.text.split(' ').map((word,i)=><React.Fragment key={i}><span style={{color:word.toLowerCase()===cue.green?.toLowerCase()?C.accent:'white'}}>{word}</span>{' '}</React.Fragment>)}
    </div>}
    {voice&&<Audio src={staticFile(voice)}/>}
  </AbsoluteFill>;
};
