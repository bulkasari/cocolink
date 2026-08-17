"""
Blender 5.2 Python Script for C3_BalloonView Previs & Semantic ID Mask
- Autorefractor Binocular / Machine Lens POV with Red Hot Air Balloon over Country Road Meadow
- Focus transition (Blur -> Sharp Focus) + Gentle Floating Balloon Motion
- Generates:
  1. Docs/EyeClinic/Blender/renders/real/C3_balloon_view.mp4 (6 seconds @ 24fps = 144 frames)
  2. Docs/EyeClinic/Blender/renders/real/C3_balloon_view_id_mask.mp4
  3. Docs/EyeClinic/Blender/renders/real/C3_balloon_view_preview.png
  4. Docs/EyeClinic/Blender/renders/real/C3_balloon_view_id_mask_preview.png
"""

import bpy
import math
import os
import subprocess

def clear_scene():
    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.object.delete()
    for block in bpy.data.meshes:
        bpy.data.meshes.remove(block)
    for block in bpy.data.materials:
        bpy.data.materials.remove(block)
    for block in bpy.data.lights:
        bpy.data.lights.remove(block)
    for block in bpy.data.cameras:
        bpy.data.cameras.remove(block)

def setup_render_common(fps=24, res_x=1280, res_y=720):
    scene = bpy.context.scene
    scene.render.resolution_x = res_x
    scene.render.resolution_y = res_y
    scene.render.fps = fps
    scene.render.image_settings.file_format = 'PNG'
    scene.render.image_settings.color_mode = 'RGBA'
    try:
        scene.render.engine = 'BLENDER_EEVEE'
    except Exception:
        pass

def create_pbr_material(name, base_color, roughness=0.3, metallic=0.0):
    mat = bpy.data.materials.new(name=name)
    mat.use_nodes = True
    nodes = mat.node_tree.nodes
    bsdf = nodes.get("Principled BSDF")
    if bsdf:
        bsdf.inputs['Base Color'].default_value = base_color
        bsdf.inputs['Roughness'].default_value = roughness
        bsdf.inputs['Metallic'].default_value = metallic
    return mat

def create_emission_material(name, color):
    mat = bpy.data.materials.new(name=name)
    mat.use_nodes = True
    nodes = mat.node_tree.nodes
    links = mat.node_tree.links
    nodes.clear()
    
    node_out = nodes.new(type='ShaderNodeOutputMaterial')
    node_emit = nodes.new(type='ShaderNodeEmission')
    node_emit.inputs['Color'].default_value = color
    node_emit.inputs['Strength'].default_value = 1.0
    links.new(node_emit.outputs['Emission'], node_out.inputs['Surface'])
    return mat

def build_balloon_scene(is_id_mask=False):
    # Materials according to video.md specification
    if is_id_mask:
        mat_bg = create_emission_material("ID_Black_Bg", (0, 0, 0, 1))          # Black #000000: Meadow & Sky
        mat_mach = create_emission_material("ID_LightGray_Body", (0.85, 0.85, 0.85, 1)) # Light Gray #D9D9D9: Machine Body
        mat_lens_ring = create_emission_material("ID_Blue_Rings", (0, 0, 1, 1)) # Pure Blue #0000FF: Dual Lens Eyepiece Rings
        mat_crosshair = create_emission_material("ID_Yellow_Cross", (1, 1, 0, 1)) # Pure Yellow #FFFF00: Crosshair reticle
        mat_balloon = create_emission_material("ID_Red_Balloon", (1, 0, 0, 1))  # Pure Red #FF0000: Hot Air Balloon
        mat_basket = create_emission_material("ID_Red_Basket", (1, 0, 0, 1))
    else:
        mat_sky = create_pbr_material("SkyMat", (0.45, 0.75, 0.98, 1.0), roughness=0.8)
        mat_grass = create_pbr_material("GrassMat", (0.35, 0.72, 0.28, 1.0), roughness=0.6)
        mat_road = create_pbr_material("RoadMat", (0.75, 0.68, 0.55, 1.0), roughness=0.5)
        mat_mach = create_pbr_material("MachBodyMat", (0.94, 0.94, 0.96, 1.0), roughness=0.25)
        mat_lens_ring = create_pbr_material("LensRingMat", (0.10, 0.12, 0.16, 1.0), roughness=0.3)
        mat_crosshair = create_emission_material("CrosshairMat", (1.0, 0.88, 0.2, 0.9))
        mat_balloon = create_pbr_material("BalloonMat", (0.92, 0.18, 0.16, 1.0), roughness=0.3)
        mat_basket = create_pbr_material("BasketMat", (0.65, 0.42, 0.22, 1.0), roughness=0.6)

    # 1. Background Country Meadow & Sky
    # Sky plane
    bpy.ops.mesh.primitive_plane_add(size=30, location=(0, 10, 2), rotation=(math.radians(90), 0, 0))
    sky = bpy.context.active_object
    sky.data.materials.append(mat_bg if is_id_mask else mat_sky)

    # Rolling Green Grass Meadow
    bpy.ops.mesh.primitive_plane_add(size=30, location=(0, 8, -0.6))
    grass = bpy.context.active_object
    grass.data.materials.append(mat_bg if is_id_mask else mat_grass)

    # Country Roads under each eye
    for rx in [-0.55, 0.55]:
        bpy.ops.mesh.primitive_plane_add(size=1, location=(rx, 7.5, -0.58))
        road = bpy.context.active_object
        road.scale = (0.7, 10, 1)
        road.data.materials.append(mat_bg if is_id_mask else mat_road)

    # 2. Hot Air Balloons in Both Lenses (Left & Right)
    balloons = []
    for bx in [-0.28, 0.28]:
        bpy.ops.mesh.primitive_uv_sphere_add(radius=0.24, location=(bx, 4.0, 1.5))
        balloon = bpy.context.active_object
        balloon.scale = (1.0, 1.0, 1.25)
        balloon.data.materials.append(mat_balloon)

        # Balloon Basket
        bpy.ops.mesh.primitive_cube_add(size=0.08, location=(bx, 4.0, 1.15))
        basket = bpy.context.active_object
        basket.data.materials.append(mat_basket)
        basket.parent = balloon
        balloons.append(balloon)

    # 3. Dual Binocular Eyepiece Housing (Front Mask)
    # Eyepiece circular thick bezel rings (Pure Blue in ID Mask)
    for lx in [-0.28, 0.28]:
        bpy.ops.mesh.primitive_torus_add(major_radius=0.28, minor_radius=0.04, location=(lx, 0.05, 1.5), rotation=(math.radians(90), 0, 0))
        ring = bpy.context.active_object
        ring.data.materials.append(mat_lens_ring)

    # Outer Housing Mask (surrounding the two rings)
    # Center Divider
    bpy.ops.mesh.primitive_cube_add(size=1, location=(0, 0.06, 1.5))
    div = bpy.context.active_object
    div.scale = (0.04, 0.05, 1.4)
    div.data.materials.append(mat_mach)

    # Left Outer Panel
    bpy.ops.mesh.primitive_cube_add(size=1, location=(-0.85, 0.06, 1.5))
    panel_l = bpy.context.active_object
    panel_l.scale = (0.60, 0.05, 1.4)
    panel_l.data.materials.append(mat_mach)

    # Right Outer Panel
    bpy.ops.mesh.primitive_cube_add(size=1, location=(0.85, 0.06, 1.5))
    panel_r = bpy.context.active_object
    panel_r.scale = (0.60, 0.05, 1.4)
    panel_r.data.materials.append(mat_mach)

    # Top Panel
    bpy.ops.mesh.primitive_cube_add(size=1, location=(0, 0.06, 2.05))
    panel_top = bpy.context.active_object
    panel_top.scale = (2.5, 0.05, 0.6)
    panel_top.data.materials.append(mat_mach)

    # Bottom Panel
    bpy.ops.mesh.primitive_cube_add(size=1, location=(0, 0.06, 0.95))
    panel_bot = bpy.context.active_object
    panel_bot.scale = (2.5, 0.05, 0.6)
    panel_bot.data.materials.append(mat_mach)

    # 4. Yellow Crosshair Reticles (Pure Yellow in ID Mask)
    for cx in [-0.28, 0.28]:
        # Horizontal crosshair
        bpy.ops.mesh.primitive_cylinder_add(radius=0.002, depth=0.52, location=(cx, 0.02, 1.5), rotation=(0, math.radians(90), 0))
        c_h = bpy.context.active_object
        c_h.data.materials.append(mat_crosshair)

        # Vertical crosshair
        bpy.ops.mesh.primitive_cylinder_add(radius=0.002, depth=0.52, location=(cx, 0.02, 1.5))
        c_v = bpy.context.active_object
        c_v.data.materials.append(mat_crosshair)

        # Inner Guide Circle
        bpy.ops.mesh.primitive_torus_add(major_radius=0.18, minor_radius=0.002, location=(cx, 0.02, 1.5), rotation=(math.radians(90), 0, 0))
        c_ring = bpy.context.active_object
        c_ring.data.materials.append(mat_crosshair)

    # Lighting
    if not is_id_mask:
        bpy.ops.object.light_add(type='SUN', location=(4, -2, 8))
        sun = bpy.context.active_object
        sun.data.energy = 5.0
        sun.data.color = (1.0, 0.98, 0.92)

        bpy.ops.object.light_add(type='AREA', location=(0, 2.0, 3.5))
        ambient = bpy.context.active_object
        ambient.data.energy = 120.0
        ambient.data.size = 2.0

    return balloons

def setup_camera_and_animation(balloons):
    # Camera placed directly looking through the viewing eyepieces
    bpy.ops.object.camera_add(location=(0, -0.65, 1.5), rotation=(math.radians(90), 0, 0))
    cam = bpy.context.active_object
    cam.data.lens = 32  # Clean perspective
    bpy.context.scene.camera = cam

    scene = bpy.context.scene
    scene.frame_start = 1
    scene.frame_end = 144  # 6.0 seconds @ 24fps

    # Hot air balloons floating smoothly up and hovering gently in sync
    for b in balloons:
        bx = b.location.x
        # Frame 1: Slightly lower, floating in
        b.location = (bx, 4.0, 1.38)
        b.keyframe_insert(data_path="location", frame=1)

        # Frame 50: Rising into reticle center
        b.location = (bx + 0.01, 4.0, 1.52)
        b.keyframe_insert(data_path="location", frame=50)

        # Frame 95: Gentle hover in center
        b.location = (bx - 0.01, 4.0, 1.53)
        b.keyframe_insert(data_path="location", frame=95)

        # Frame 144: Perfectly centered and stable
        b.location = (bx, 4.0, 1.50)
        b.keyframe_insert(data_path="location", frame=144)

    return cam

def render_sequence(out_dir, is_id_mask=False):
    prefix = "C3_balloon_view_id_mask" if is_id_mask else "C3_balloon_view"
    print(f"🎬 [Starting] Rendering sequence for: {prefix}...")
    clear_scene()
    setup_render_common(fps=24, res_x=1280, res_y=720)
    balloon = build_balloon_scene(is_id_mask=is_id_mask)
    cam = setup_camera_and_animation(balloon)

    scene = bpy.context.scene
    temp_prefix = os.path.join(out_dir, f"{prefix}_frame_")
    scene.render.filepath = temp_prefix
    
    # 1. Render Frame Sequence
    bpy.ops.render.render(animation=True)

    # 2. Render Keyframe Preview (Frame 75: Balloon perfectly floating in reticle center)
    scene.frame_set(75)
    preview_png = os.path.join(out_dir, f"{prefix}_preview.png")
    scene.render.filepath = preview_png
    bpy.ops.render.render(write_still=True)
    print(f"🖼️ Saved keyframe preview: {preview_png}")

    # 3. FFmpeg MP4 Encoding
    mp4_out = os.path.join(out_dir, f"{prefix}.mp4")
    input_pattern = os.path.join(out_dir, f"{prefix}_frame_%04d.png")
    ffmpeg_cmd = [
        "ffmpeg", "-y",
        "-framerate", "24",
        "-i", input_pattern,
        "-c:v", "libx264",
        "-pix_fmt", "yuv420p",
        "-crf", "18",
        "-preset", "fast",
        mp4_out
    ]
    print(f"📦 Encoding MP4 with FFmpeg: {mp4_out}")
    subprocess.run(ffmpeg_cmd, check=True)

    # 4. Clean up temporary PNG frames
    for f in os.listdir(out_dir):
        if f.startswith(f"{prefix}_frame_") and f.endswith(".png"):
            try:
                os.remove(os.path.join(out_dir, f))
            except Exception:
                pass
    print(f"✅ Successfully generated {mp4_out}")

if __name__ == "__main__":
    out_dir = r"d:\Github\Unity\cocolink\Docs\EyeClinic\Blender\renders\real"
    os.makedirs(out_dir, exist_ok=True)
    
    # 1. Render Realistic Previs Video
    render_sequence(out_dir, is_id_mask=False)
    
    # 2. Render Semantic Color ID Mask
    render_sequence(out_dir, is_id_mask=True)
    print("🎉 C3_BalloonView Previs renders completed successfully!")
