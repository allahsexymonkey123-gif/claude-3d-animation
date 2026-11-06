import * as THREE from 'three';
import {COLORS as C, SPEC} from './style';

export function rng(seed=1607) {
  let s=seed>>>0;
  return () => {s=(1664525*s+1013904223)>>>0;return s/4294967296;};
}
export const material = (color: string, extra: THREE.MeshStandardMaterialParameters = {}) =>
  new THREE.MeshStandardMaterial({color,roughness:.88,metalness:0,...extra});

export function box(parent: THREE.Object3D, name: string, size: [number,number,number],
  pos: [number,number,number], mat: THREE.Material) {
  const mesh=new THREE.Mesh(new THREE.BoxGeometry(...size),mat);mesh.name=name;mesh.position.set(...pos);
  mesh.castShadow=true;mesh.receiveShadow=true;parent.add(mesh);return mesh;
}

export function segment(parent: THREE.Object3D, a: THREE.Vector3,b: THREE.Vector3,radius: number,mat: THREE.Material) {
  const delta=b.clone().sub(a),len=delta.length();
  const mesh=new THREE.Mesh(new THREE.CylinderGeometry(radius,radius,len,10),mat);
  mesh.position.copy(a).add(b).multiplyScalar(.5);mesh.quaternion.setFromUnitVectors(new THREE.Vector3(0,1,0),delta.normalize());
  mesh.castShadow=true;parent.add(mesh);return mesh;
}

export function tree(parent: THREE.Object3D,x: number,z: number,seed: number,scale=1) {
  const g=new THREE.Group();g.position.set(x,0,z);g.scale.setScalar(scale);parent.add(g);
  const trunk=new THREE.Mesh(new THREE.CylinderGeometry(.19,.29,2.9,7),material(C.bark));
  trunk.position.y=1.4;trunk.castShadow=true;g.add(trunk);
  const random=rng(seed);
  for(let i=0;i<6;i++) {
    const leaf=new THREE.Mesh(new THREE.IcosahedronGeometry(1.1+random()*.3,1),material(C.leaves[i%4],{flatShading:true}));
    leaf.position.set((random()-.5)*1.6,2.8+random()*1.2,(random()-.5)*1.3);
    leaf.rotation.set(random(),random(),random());leaf.castShadow=true;leaf.receiveShadow=true;g.add(leaf);
  }
  return g;
}

function roof(parent: THREE.Object3D,cx: number,cz: number,w: number,d: number,y: number,rise=1.8) {
  const half=w/2;
  const geo=new THREE.BufferGeometry();
  geo.setAttribute('position',new THREE.Float32BufferAttribute([
    -half,y,-d/2, half,y,-d/2, 0,y+rise,-d/2,
    -half,y,d/2, 0,y+rise,d/2, half,y,d/2,
    -half,y,-d/2, 0,y+rise,-d/2, 0,y+rise,d/2,
    -half,y,-d/2, 0,y+rise,d/2, -half,y,d/2,
    0,y+rise,-d/2, half,y,-d/2, half,y,d/2,
    0,y+rise,-d/2, half,y,d/2, 0,y+rise,d/2,
  ],3));geo.computeVertexNormals();
  const r=new THREE.Mesh(geo,material(C.roof,{side:THREE.DoubleSide,flatShading:true}));r.position.set(cx,0,cz);r.castShadow=true;parent.add(r);
  // Fine horizontal bands on slopes. Geometry carries form; no global outline pass.
  for(let i=1;i<12;i++) {
    const q=i/12, yy=y+rise*q+.014,xx=half*(1-q);
    for(const sign of [-1,1]) box(parent,'roof-course',[.035,.025,d],[cx+sign*xx,yy,cz],material(C.roofDark));
  }
  segment(parent,new THREE.Vector3(cx-half,y,cz+d/2+.015),new THREE.Vector3(cx,y+rise,cz+d/2+.015),.055,material(C.trim));
  segment(parent,new THREE.Vector3(cx,y+rise,cz+d/2+.015),new THREE.Vector3(cx+half,y,cz+d/2+.015),.055,material(C.trim));
}

export function house(parent: THREE.Object3D) {
  const h=new THREE.Group();h.name='house';h.position.set(0,0,-5.9);parent.add(h);
  box(h,'house-body',[10.6,5.6,6.8],[0,2.8,0],material(C.stucco));
  for(let y=.6;y<5.6;y+=.22) {
    box(h,'clapboard-front',[10.6,.014,.018],[0,y,3.405],material('#B1AC99'));
    box(h,'clapboard-side',[.018,.014,6.8],[5.305,y,0],material('#B1AC99'));
  }
  box(h,'floor-trim',[10.8,.15,6.95],[0,2.82,0],material(C.trim));
  roof(h,0,0,11.3,7.3,5.6);
  const front=3.43;
  for(const [x,y] of [[-3.6,4.35],[-1.5,4.35],[.6,4.35],[2.7,4.35],[-3.6,1.55]] as [number,number][]) {
    box(h,'window-frame',[1.7,1.92,.10],[x,y,front],material(C.trim));
    box(h,'glass',[1.49,1.7,.04],[x,y,front+.075],material(C.glass,{roughness:.25}));
    box(h,'mullion',[.045,1.7,.07],[x,y,front+.11],material(C.trim));
    const shine=box(h,'glass-reflection',[.14,1.58,.015],[x+.35,y,front+.104],material('#B8D1D8'));
    shine.rotation.z=-.23;
  }
  box(h,'front-door',[1.1,2.25,.15],[-1.5,1.125,front+.10],material('#6E5234'));
  box(h,'door-trim',[1.4,2.55,.12],[-1.5,1.28,front+.02],material(C.trim));
  box(h,'door-visible',[1.1,2.25,.16],[-1.5,1.125,front+.12],material('#6E5234'));
  box(h,'door-knob',[.07,.07,.07],[-1.14,1.10,front+.23],material('#D6BB68'));
  box(h,'garage-extension',[5.9,3,2],[2.5,1.5,3.5],material(C.stucco));
  roof(h,2.5,3.4,6.35,2.7,3.05,1.1);
  const gf=4.53;
  box(h,'garage-trim',[5.65,2.87,.12],[2.5,1.44,gf],material(C.trim));
  box(h,'garage-door',[5.3,2.65,.12],[2.5,1.33,gf+.08],material(C.garage));
  for(let row=0;row<4;row++) for(let col=0;col<4;col++) {
    box(h,'garage-panel',[1.20,.54,.035],[.58+col*1.29,.36+row*.63,gf+.16],material(row===3?C.glass:C.concrete));
  }
  for(const x of [-4.5,-2.4,-.3,1.8,3.9]) {
    box(h,'foundation-stone',[2.0,.45,.12],[x,.225,front+.03],material('#A39E87'));
  }
  return h;
}

export type BuiltWorld = {root: THREE.Group;slab: THREE.Group;water: THREE.Group;flow: THREE.Mesh[];pipe: THREE.Group;soil: THREE.Mesh};
export function buildWorld(): BuiltWorld {
  const root=new THREE.Group();const random=rng(7621);
  const soil=box(root,'cutaway-soil',[14,8,22],[0,-4,0],material(C.soil));
  // Cut the driveway footprint out of the lawn. A removed slab reveals aggregate, not grass.
  const lawns=[[-7,-.2,-11,11],[5.2,7,-11,11],[-.2,5.2,-11,-3],[-.2,5.2,9,11]];
  for(const [x0,x1,z0,z1] of lawns) {
    box(root,'lawn',[x1-x0,.09,z1-z0],[(x0+x1)/2,.045,(z0+z1)/2],material(C.grass));
    for(let z=-10.5;z<11;z+=1.8) {
      const lo=Math.max(z0,z-.45),hi=Math.min(z1,z+.45);
      if(hi>lo)box(root,'mowing-stripe',[x1-x0,.009,hi-lo],[(x0+x1)/2,.096,(lo+hi)/2],material(C.grassStripe));
    }
  }
  // Aggregate embedded on the exposed front and right cut faces; seeded and fixed.
  const pebbleGeo=new THREE.IcosahedronGeometry(.045,0), mats=C.aggregate.map(c=>material(c));
  for(let i=0;i<650;i++) {
    const m=new THREE.Mesh(pebbleGeo,mats[i%mats.length]);
    if(i<440) m.position.set(-7+random()*14,-7.8+random()*7.7,11.007);
    else m.position.set(7.007,-7.8+random()*7.7,-11+random()*22);
    m.scale.set(1+random(),.5+random(),.25+random()*.3);m.rotation.z=random()*Math.PI;root.add(m);
  }
  house(root);tree(root,-4.7,3.1,4,1.05);tree(root,-5,-6,17,.65);
  box(root,'footpath',[14,.12,1.25],[0,.12,9.5],material(C.concrete));
  box(root,'road',[3.2,.1,28],[-8.65,-.04,0],material('#343A39'));
  for(let i=0;i<5;i++) {
    const hill=new THREE.Mesh(new THREE.IcosahedronGeometry(1,0),material(i%2?'#C7CDB9':'#D2D5BF',{flatShading:true}));
    hill.scale.set(18,4+i%3,10);hill.position.set(-30+i*15,-3,-30);root.add(hill);
  }
  const d=SPEC.driveway;
  box(root,'aggregate-base',[d.width,.32,d.length],[d.x,-.08,d.centerZ],material(C.gravel));
  // Separated rigid slabs: actual gaps, no disappearing surface substitution.
  const slab=new THREE.Group();root.add(slab);
  for(let r=0;r<4;r++) for(let c=0;c<2;c++) {
    const b=box(slab,'concrete-panel',[d.width/2-.035,.14,d.length/4-.035],
      [d.x-d.width/4+c*d.width/2,.17,d.centerZ-d.length/2+d.length/8+r*d.length/4],material(C.concrete));
    b.userData.baseY=b.position.y;
  }
  // Open-front underground route is shown IN FRONT of soil face, making its path inspectable.
  const pipe=new THREE.Group();root.add(pipe);
  const path=[new THREE.Vector3(2.5,-.3,11.10),new THREE.Vector3(2.5,-.9,11.10),new THREE.Vector3(-4.7,-1.6,11.10),new THREE.Vector3(-4.7,-1.75,11.10)];
  for(let i=0;i<path.length-1;i++) segment(pipe,path[i],path[i+1],.12,material(C.pipe));
  const water=new THREE.Group();root.add(water);
  const flow: THREE.Mesh[]=[];
  for(let i=0;i<32;i++) {
    const droplet=new THREE.Mesh(new THREE.SphereGeometry(.075,6,4),material(C.water,{roughness:.22,emissive:C.water,emissiveIntensity:.12}));
    water.add(droplet);flow.push(droplet);
  }
  // Translucent channel strip is an illustrative overlay, not a fluid simulation.
  box(water,'surface-water',[d.width-.12,.025,1.2],[d.x,.28,8.3],material(C.water,{transparent:true,opacity:.58,roughness:.3,depthWrite:false}));
  return {root,slab,water,flow,pipe,soil};
}
