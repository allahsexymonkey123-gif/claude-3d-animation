import * as THREE from 'three';
import {mix,ramp} from './story';

export function cameraAt(frame: number) {
  const u=ramp(frame,0,360), close=ramp(frame,120,280);
  const position=new THREE.Vector3(mix(11,9.5,u),mix(18,16,u),mix(32,30,u));
  const target=new THREE.Vector3(mix(0,.5,u),mix(-1,-1.5,close),mix(0,1.5,close));
  return {position,target,fov:34,roll:0};
}
