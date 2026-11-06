# Lighting and rendering

## Observed look

The clips show clear daylight form shading, soft ambient fill, distinct contact shadows and readable edges. Lawn and tree facets vary in value. Garage openings/glass are dark; pale architecture retains visible surface color. Trees, cars, slabs and root lifts cast shadows belonging to the same scene. Depth is carried by perspective, occlusion, layer thickness and shadow, rather than heavy depth of field.

The shorter reference adds rain streaks/flow and a few brief white storm flashes; its final seconds change toward evening, with warmer windows and a cool darker sky. Do not infer exact light wattage, shadow-map resolution, render engine or post-processing nodes from the final MP4.

## New scene settings (T)

| Setting | Starting value | Adjustment criterion |
|---|---|---|
| Key direction | Above/front-left, elevation 40–60° | Garage panel relief and crown facets read without black sides |
| Three.js directional intensity | 2–3 under the starter's ACES setup | Treat units as renderer-specific; compare output pixels |
| Hemisphere fill | .8–1.2 | Keep shaded soil and underside readable |
| Key tint | Soft neutral/warm white | Avoid making green grass yellow or plaster orange |
| Ambient sky tint | Neutral/pale blue | Preserve subdued cool shadows |
| Shadow map | 2048, 4096 for important close-ups | No shimmering leaves, jagged slab edges or acne |
| Shadow bias | Start near −.0002 and tune per scale | No floating shadow gap or false dark patches |
| Contact AO | Small radius relative to part size | Seat stones/slabs in the world; avoid black halos |
| Tone mapping | One consistent ACES/neutral pipeline | Never stack multiple filmic transforms |
| Exposure | Start 1.0–1.1 | Keep white trim below hard clipping |
| Bloom | Off, or very slight only on true lamps | Do not soften every lit edge |
| Depth of field | Off for diagram/plan, very subtle for a close insert if needed | Labels and layer boundaries stay sharp |
| Grain | Off | Avoid muddy compressed output |
| Motion blur | None for holds; optional subtle blur on fast moves | Keep readable edges on each frame |

Three.js version-specific intensity/exposure settings are not interchangeable with Blender watts/strength. In Blender, match the resulting picture with a broad area/sun key, ambient world fill, contact shadows and a view transform chosen once. A different renderer can implement the same style; do not claim the references used either engine.

## Render pipeline

1. Model and light at the intended portrait aspect.
2. Use deterministic frame time, seeded static detail and real depth.
3. Render 1080×1920 at 30 fps; use anti-aliasing and high enough shadow resolution.
4. Composite crisp typography **after** 3D rendering so caption outlines stay clean. Scale fonts, strokes and leaders with output width.
5. Keep SDR Rec.709/sRGB output consistent. Use H.264 yuv420p at CRF 16–18 for delivery; save PNG stills for QA.
6. If a final export uses 1440×2560, scale all screen-space overlay dimensions by 4/3. Do not double-apply scaling through renderer DPR and composition size.
7. Verify native 30 fps timestamps. Duplicating 15 frames per second into a 30 fps container will not reproduce the motion.

## Evening transition (T)

For an ending like ref02 f1180–1244, blend light direction/intensity, sky/hill values and window emission over roughly 30–60 frames. Change the scene, not just a dark transparent overlay on the entire frame. Keep the explanatory water route readable. Warm window glow can be visible without giant bloom halos. Verify the transition with consecutive frames, since tone/exposure stepping can be more distracting than any material simplification.

## Fine-detail checks

Test a garage panel edge, diagonal roof fascia, paver joint and thin leader line at full delivery resolution. Check one shadow under a raised slab and one underground intersection. No Z-fighting, alpha sorting errors, shadow acne, light leaks at soil/top joins or material color changes as the camera crosses a view angle.
