# Materials, color and texture

## Evidence and sampling

Measure from decoded frames. The included full-size JPEGs are study images; compressed and lit pixels do not reveal original material albedos. `../measurements/palette_samples.json` stores every chosen ROI and its median RGB. The median was measured from the saved study JPEG, so small codec differences may shift a value by a few levels. For tighter comparisons, decode the same frame directly to PNG from the included original MP4.

Whole-image per-frame statistics are in the CSVs. Median image mean Y′ is .4899 for ref01 and .3872 for ref02; median mean saturation is .4450 and .4407. Y′ uses display-encoded BT.709 coefficients, **not** linear photometric luminance. Soil coverage, captions, camera framing and night/storm changes affect these values; do not use them as a blanket exposure target for every shot.

## Palette and material targets

| Surface | M sampled displayed color | T material starting point | Required reading |
|---|---|---|---|
| Concrete | `#B4B0A4` | warm gray albedo, roughness .85–.95, metalness 0 | Fine speckle, clear thickness, dark narrow joints |
| Grass | `#54A332` | vivid mid-green with alternate lighter bands | Broad mowing stripes plus small edge tufts |
| Roof | `#B24718` | rust/terracotta, roughness .8 | Repeated courses/tile relief, brighter ridge edges |
| Siding | `#C8B79E` | warm cream/tan, roughness .85 | Horizontal course relief and small shadow gaps |
| Soil | `#684111` | ochre-brown, roughness .95 | Varied little stones, mild mottling, fine roots near top |
| Vehicle | `#0D54A2` | simple saturated blue, roughness .4–.6 | Broad clean panels, dark glazing, distinct rubber wheels |
| Sky | `#90CBEE` | blue sky/background gradient | Quiet pale hills; no noisy HDR sky |
| Plaster | `#BEB5A6` | warm off-white, roughness .85 | Subtle mottling without large grunge streaks |
| Garage | `#1D2025` | near-black blue-gray, roughness .65 | Real horizontal panels and opening recess |
| Glass | `#7C8D9E` | muted blue-gray, roughness .2–.4 | Broad pale diagonal reflection strips |
| Pump | `#0A5A95` | medium blue casing | Black base/top and small float detail, not metallic blue chrome |

The target albedos in `templates/diorama/style.ts` deliberately differ from sampled lit pixels. Tune under the actual light rig. Keep sRGB textures marked as color textures and let the renderer work in linear space. Avoid applying sRGB conversion twice. Use one tone mapper/exposure setup for all shots unless the story explicitly changes lighting.

## Texture scale recipes (T)

- **Concrete:** At the 512-wide reference scale, texture mostly reads as 1–3 px stipple, with a low contrast range. Start with a seeded 512–1024 px tile, broad low-contrast noise and sparse darker pin specks. In world units, make aggregate texture features roughly .003–.015 m. Avoid animated noise and high-frequency single-pixel sparkle.
- **Soil:** Use a low-contrast brown base with sparse gray/tan embedded pebbles. Vary pebble radius by roughly 3:1, orientation and density. Keep most pebbles smaller than 1% of the section height. Add thin root strands near the lawn edge. Stones should look embedded rather than floating confetti.
- **Base:** Gray aggregate with grain visibly coarser than the concrete texture. Preserve a clearly different silhouette/boundary from the dirt and the pale sand bed.
- **Pavers:** Related terracotta, brown and tan blocks with per-block color jitter, not a random rainbow. Use herringbone or a deliberate bond with a repeatable module. Add shallow edge bevels; keep narrow mortar/sand lines. Make block count/size remain consistent through zooms.
- **Grass:** Broad stripes are world-space features. Their spacing cannot swim when the camera moves. Use small blades at edges, but a dense fur simulation is unnecessary.
- **Siding/roof:** Course lines follow construction direction. Avoid a generic noise map that hides whether a surface is wood, roof tile or concrete.
- **Glass:** Reflection bands are large and quiet. Use a small number of diagonal pale strips or an environment reflection, not rapidly changing mirrored scenery.
- **Water:** Light blue/teal, partially transparent, with directional white/blue streaks. The drainage clip shows readable simplified flow sheets, foam near obstacles and a bright blue route in the section. Use shallow ripples with no ocean waves.

## Selective diagram colors

Green tinted concrete in ref01 around f780–830 is a temporary explanatory overlay. Thin mint-green highlights also mark sidewalk control joints; bright white gaps emphasize paver separation near the ending. Keep these overlays transient and aligned with real surfaces. Do not permanently tint every concrete slab green.

Use green for a part being named or a positive mechanism, pale blue for moving water, and red/white for failure stamps. These are narrative accents. Keep the base world palette stable so those accents have meaning.

## Avoid

Smooth plastic foliage, gold metal everywhere, purple grade on the whole scene, heavy bloom, thick contour ink, photoreal grunge, high-frequency noisy bump maps, saturated white plaster, black-crushed lawns, and textures that change seed, scale or UV orientation between frames.
