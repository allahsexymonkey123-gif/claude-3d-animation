import React,{useLayoutEffect,useMemo} from 'react';
import {useThree} from '@react-three/fiber';
import {useCurrentFrame} from 'remotion';
import * as THREE from 'three';
import {buildWorld} from './geometry';
import {cameraAt} from './camera';
import {COLORS as C,SPEC} from './style';
import {ramp} from './story';

export const World: React.FC = () => {
  const f=useCurrentFrame(),{camera}=useThree();
  const world=useMemo(buildWorld,[]);
  // Pure absolute-time posing. Rendering f300 before f0 yields the same frame.
  useLayoutEffect(()=>{
    const c=cameraAt(f);camera.position.copy(c.position);camera.up.set(0,1,0);camera.lookAt(c.target);
    if(camera instanceof THREE.PerspectiveCamera) {camera.fov=c.fov;camera.updateProjectionMatrix();}
    const lift=ramp(f,90,150);
    world.slab.position.set(-ramp(f,170,210)*24,lift*1.65,0);world.slab.visible=true;
    world.pipe.visible=f>=135;
    world.water.visible=f>=240;
    for(let i=0;i<world.flow.length;i++) {
      const t=((f-240)/90+i/world.flow.length)%1;
      const a=.15,b=.85;
      let x=2.5,y=-.3,z=11.25;
      if(t<a)y=-.3-(t/a)*.6;
      else if(t<b){const u=(t-a)/(b-a);x=2.5-7.2*u;y=-.9-.7*u;}
      else{x=-4.7;y=-1.6-.15*((t-b)/(1-b));}
      world.flow[i].position.set(x,y,z);
    }
  },[f,camera,world]);
  useLayoutEffect(()=>()=>{
    const geometries=new Set<THREE.BufferGeometry>(),materials=new Set<THREE.Material>();
    world.root.traverse(o=>{if(o instanceof THREE.Mesh){geometries.add(o.geometry);for(const m of Array.isArray(o.material)?o.material:[o.material])materials.add(m);}});
    for(const g of geometries)g.dispose();for(const m of materials)m.dispose();
  },[world]);
  return <>
    <color attach="background" args={[C.sky]}/>
    <hemisphereLight args={['#EAF1F5','#5C745B',SPEC.lights.fill]}/>
    <directionalLight position={[-14,24,17]} intensity={SPEC.lights.key} color="#FFF6E7" castShadow
      shadow-mapSize={[2048,2048]} shadow-bias={SPEC.lights.shadowBias}
      shadow-camera-left={-22} shadow-camera-right={22} shadow-camera-top={22} shadow-camera-bottom={-22}
      shadow-camera-near={1} shadow-camera-far={80}/>
    <primitive object={world.root}/>
  </>;
};
