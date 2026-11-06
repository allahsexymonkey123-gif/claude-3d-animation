// Reconstruction targets, not recovered source asset/material/camera settings.
// Scene uses metres, Y-up, house at -Z, street at +Z. See measurements.md.
export const COLORS = {
  sky: '#90CBEE', horizon: '#DCE4CF', soil: '#805015', soilDark: '#573713',
  aggregate: ['#B7AD8A','#8E8266','#C7C0A6','#75694E'],
  grass: '#55C22E', grassStripe: '#6CCC36', grassDark: '#34861E',
  leaves: ['#4C9C1D','#61B72B','#37811E','#72BF32'], bark: '#79502B',
  stucco: '#D9D5C4', trim: '#F4EEDF', roof: '#B44322', roofDark: '#80311C',
  blackTrim: '#23282A', garage: '#B9BCAE', glass: '#7199AA', glassDark: '#314E61',
  concrete: '#B5B5A8', concreteDark: '#909387', gravel: '#8E8B7C',
  pavers: ['#A45C36','#B7754C','#955039','#C68A59','#884D34'],
  water: '#69BBCD', pipe: '#D7DDDC', caption: '#FFFFFF', accent: '#60DF79',
  captionStroke: '#111415', warning: '#D14B43', mint: '#A0E8C6'
} as const;

export const SPEC = {
  lot: {width: 14, length: 22, soilDepth: 8},
  driveway: {x: 2.5, width: 5.4, length: 12.0, centerZ: 3.0, slab: .14, base: .32},
  house: {width: 10.6, depth: 7.2, height: 5.6},
  camera: {fov: 34, near: .1, far: 180, position: [11,18,32] as const, target: [0,-1,0] as const},
  lights: {key: 2.5, fill: 1.1, shadowMap: 2048, shadowBias: -.0002},
  overlay: {captionY: .735, captionFont: 76, captionStroke: 8, titleY: .10, labelFont: 25},
} as const;
