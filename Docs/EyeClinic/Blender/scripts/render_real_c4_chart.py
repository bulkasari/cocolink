"""
Blender 5.2 Python Script for C4_ChartMatch Previs & Realistic Graphic
- Scene: 1st-person POV child's eye level in Pediatric Eye Clinic
- Wall-mounted Korean Standard 3M Light Box Eye Chart (한식표준 3M용 시력표 실물 텍스처 적용)
  - Features real chart texture from Docs/EyeClinic/Graphic/real/B5276385504_41125294488.jpg
  - Target Picture Symbol: ✈️ Airplane (Row 0.2 / 0.3)
- Optometrist nurse holding a cute pointer stick, pointing to the airplane on the Korean eye chart and smiling warmly
- Generates:
  1. Docs/EyeClinic/Graphic/real/real_c4_chart_match.png (Realistic Keyframe)
  2. Docs/EyeClinic/Blender/renders/real/C4_chart_match.mp4 (6s @ 24fps = 144 frames)
  3. Docs/EyeClinic/Blender/renders/real/C4_chart_match_id_mask.mp4 (Semantic Color ID Mask)
  4. Docs/EyeClinic/Blender/renders/real/C4_chart_match_preview.png
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
    for block in bpy.data.images:
        bpy.data.images.remove(block)

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

def create_pbr_material(name, base_color, roughness=0.35, metallic=0.0):
    mat = bpy.data.materials.new(name=name)
    mat.use_nodes = True
    bsdf = mat.node_tree.nodes.get("Principled BSDF")
    if bsdf:
        bsdf.inputs['Base Color'].default_value = base_color
        bsdf.inputs['Roughness'].default_value = roughness
        bsdf.inputs['Metallic'].default_value = metallic
    return mat

def create_emission_material(name, color, strength=1.0):
    mat = bpy.data.materials.new(name=name)
    mat.use_nodes = True
    nodes = mat.node_tree.nodes
    links = mat.node_tree.links
    nodes.clear()
    
    node_out = nodes.new(type='ShaderNodeOutputMaterial')
    node_emit = nodes.new(type='ShaderNodeEmission')
    node_emit.inputs['Color'].default_value = color
    node_emit.inputs['Strength'].default_value = strength
    links.new(node_emit.outputs['Emission'], node_out.inputs['Surface'])
    return mat

def create_textured_chart_material(image_path):
    mat = bpy.data.materials.new(name="KoreanChartMat")
    mat.use_nodes = True
    nodes = mat.node_tree.nodes
    links = mat.node_tree.links
    nodes.clear()

    node_out = nodes.new(type='ShaderNodeOutputMaterial')
    node_emit = nodes.new(type='ShaderNodeEmission')
    node_emit.inputs['Strength'].default_value = 1.15
    
    if os.path.exists(image_path):
        img = bpy.data.images.load(image_path)
        node_tex = nodes.new(type='ShaderNodeTexImage')
        node_tex.image = img
        links.new(node_tex.outputs['Color'], node_emit.inputs['Color'])
    else:
        node_emit.inputs['Color'].default_value = (0.95, 0.95, 0.95, 1.0)
        
    links.new(node_emit.outputs['Emission'], node_out.inputs['Surface'])
    return mat

def build_chart_scene(is_id_mask=False, chart_texture_path=""):
    # Materials setup
    if is_id_mask:
        mat_bg = create_emission_material("ID_Black", (0, 0, 0, 1))           # Black: Room floor/walls
        mat_chart_board = create_emission_material("ID_ChartBoard", (0, 0, 1, 1)) # Blue: Light Box Chart
        mat_target_plane = create_emission_material("ID_Plane", (1, 1, 0, 1))     # Yellow: Target icon (✈️ Airplane)
        mat_other_icons = create_emission_material("ID_OtherIcons", (1, 0, 0, 1)) # Red: Other picture icons
        mat_nurse_body = create_emission_material("ID_Nurse", (0, 1, 0, 1))       # Green: Nurse
        mat_pointer = create_emission_material("ID_Pointer", (1, 0, 1, 1))        # Magenta: Pointer Stick
    else:
        mat_floor = create_pbr_material("FloorWood", (0.85, 0.68, 0.48, 1), roughness=0.35)
        mat_wall = create_pbr_material("WallIvory", (0.96, 0.94, 0.90, 1), roughness=0.6)
        mat_wood_cab = create_pbr_material("WoodCab", (0.80, 0.62, 0.44, 1), roughness=0.4)
        mat_chart_frame = create_pbr_material("ChartBoxFrame", (0.82, 0.84, 0.86, 1), roughness=0.25, metallic=0.7)
        mat_nurse_scrub = create_pbr_material("NurseScrub", (0.15, 0.55, 0.62, 1), roughness=0.45) # Professional teal scrub
        mat_nurse_skin = create_pbr_material("NurseSkin", (0.95, 0.82, 0.74, 1), roughness=0.35)
        mat_nurse_hair = create_pbr_material("NurseHair", (0.10, 0.07, 0.05, 1), roughness=0.6)
        mat_pointer = create_pbr_material("PointerGold", (0.95, 0.80, 0.25, 1), roughness=0.2, metallic=0.7)
        mat_pointer_tip = create_pbr_material("PointerTipPink", (0.98, 0.55, 0.65, 1), roughness=0.3)

    # 1. Environment: Floor & Back Wall
    bpy.ops.mesh.primitive_plane_add(size=16, location=(0, 2, 0))
    floor = bpy.context.active_object
    floor.data.materials.append(mat_bg if is_id_mask else mat_floor)

    bpy.ops.mesh.primitive_plane_add(size=16, location=(0, 4.5, 2.5), rotation=(math.radians(90), 0, 0))
    bwall = bpy.context.active_object
    bwall.data.materials.append(mat_bg if is_id_mask else mat_wall)

    if not is_id_mask:
        # Background clinic desk / side equipment table
        bpy.ops.mesh.primitive_cube_add(size=1, location=(-1.8, 4.2, 1.2))
        cab = bpy.context.active_object
        cab.scale = (1.2, 0.4, 1.6)
        cab.data.materials.append(mat_wood_cab)

    # 2. Wall-mounted Korean Standard Light Box Eye Chart (한식표준 3M용 시력표)
    # Box Frame (Aluminum/White light box body)
    bpy.ops.mesh.primitive_cube_add(size=1, location=(-0.35, 4.40, 1.65))
    chart_box = bpy.context.active_object
    chart_box.scale = (0.95, 0.08, 1.60)  # Aspect ratio matches tall vertical Hahn chart
    chart_box.data.materials.append(mat_bg if is_id_mask else mat_chart_frame)

    # Illuminated Chart Face (Display Surface with real texture)
    bpy.ops.mesh.primitive_plane_add(size=1, location=(-0.35, 4.355, 1.65), rotation=(math.radians(90), 0, 0))
    chart_face = bpy.context.active_object
    chart_face.scale = (0.86, 1.50, 1.0)
    
    if is_id_mask:
        chart_face.data.materials.append(mat_chart_board)
    else:
        mat_chart_tex = create_textured_chart_material(chart_texture_path)
        chart_face.data.materials.append(mat_chart_tex)

    # 3. ID Mask overlays for Target (✈️ Airplane) & Other picture icons
    if is_id_mask:
        # Target Symbol: ✈️ Airplane (0.2 line, right column)
        bpy.ops.mesh.primitive_plane_add(size=0.14, location=(-0.08, 4.35, 1.88), rotation=(math.radians(90), 0, 0))
        target_icon = bpy.context.active_object
        target_icon.data.materials.append(mat_target_plane)

        # Other Symbols: 🦋 Butterfly (0.3 line), 🐦 Bird (0.4 line), 🚗 Car (0.6 line)
        # Butterfly
        bpy.ops.mesh.primitive_plane_add(size=0.12, location=(-0.08, 4.35, 1.73), rotation=(math.radians(90), 0, 0))
        icon_bfly = bpy.context.active_object
        icon_bfly.data.materials.append(mat_other_icons)
        # Bird
        bpy.ops.mesh.primitive_plane_add(size=0.11, location=(-0.08, 4.35, 1.60), rotation=(math.radians(90), 0, 0))
        icon_bird = bpy.context.active_object
        icon_bird.data.materials.append(mat_other_icons)
        # Car
        bpy.ops.mesh.primitive_plane_add(size=0.10, location=(-0.08, 4.35, 1.40), rotation=(math.radians(90), 0, 0))
        icon_car = bpy.context.active_object
        icon_car.data.materials.append(mat_other_icons)

    # 4. Friendly Optometrist Nurse Standing Beside Chart (Right Side)
    # Torso (Teal scrub)
    bpy.ops.mesh.primitive_cube_add(size=1, location=(0.78, 3.85, 1.35))
    nurse_torso = bpy.context.active_object
    nurse_torso.scale = (0.34, 0.24, 0.65)
    nurse_torso.data.materials.append(mat_nurse_body if is_id_mask else mat_nurse_scrub)

    # Head
    bpy.ops.mesh.primitive_uv_sphere_add(radius=0.12, location=(0.78, 3.85, 1.82))
    nurse_head = bpy.context.active_object
    nurse_head.data.materials.append(mat_nurse_body if is_id_mask else mat_nurse_skin)

    # Hair Bun
    bpy.ops.mesh.primitive_uv_sphere_add(radius=0.08, location=(0.78, 3.97, 1.88))
    nurse_bun = bpy.context.active_object
    nurse_bun.data.materials.append(mat_nurse_body if is_id_mask else mat_nurse_hair)

    # Right Arm holding pointer stick extending toward the Airplane icon on the chart
    bpy.ops.mesh.primitive_cylinder_add(radius=0.04, depth=0.45, location=(0.54, 3.75, 1.55), rotation=(math.radians(8), math.radians(60), math.radians(-25)))
    arm = bpy.context.active_object
    arm.data.materials.append(mat_nurse_body if is_id_mask else mat_nurse_scrub)

    # Hand
    bpy.ops.mesh.primitive_uv_sphere_add(radius=0.045, location=(0.32, 3.70, 1.70))
    hand = bpy.context.active_object
    hand.data.materials.append(mat_nurse_body if is_id_mask else mat_nurse_skin)

    # Pointer Stick (Pointing directly at the Airplane icon at x=-0.08, z=1.88)
    bpy.ops.mesh.primitive_cylinder_add(radius=0.008, depth=0.60, location=(0.10, 3.95, 1.80), rotation=(math.radians(3), math.radians(72), math.radians(-12)))
    pointer = bpy.context.active_object
    pointer.data.materials.append(mat_pointer)

    # Cute Pointer Tip (Star/Bear tip)
    bpy.ops.mesh.primitive_uv_sphere_add(radius=0.024, location=(-0.16, 4.22, 1.88))
    pointer_tip = bpy.context.active_object
    pointer_tip.data.materials.append(mat_pointer if is_id_mask else mat_pointer_tip)

    # 5. Lighting (Warm pediatric clinic mood)
    if not is_id_mask:
        # Key Area Light
        bpy.ops.object.light_add(type='AREA', location=(0.5, 1.5, 2.8), rotation=(math.radians(45), math.radians(-15), 0))
        key_l = bpy.context.active_object
        key_l.data.energy = 220.0
        key_l.data.size = 2.0
        key_l.data.color = (1.0, 0.96, 0.92)

        # Soft Fill Light
        bpy.ops.object.light_add(type='AREA', location=(-1.5, 1.8, 2.2), rotation=(math.radians(40), math.radians(25), 0))
        fill_l = bpy.context.active_object
        fill_l.data.energy = 140.0
        fill_l.data.size = 2.0
        fill_l.data.color = (0.92, 0.96, 1.0)

        # Ceiling Cove Warm Light
        bpy.ops.object.light_add(type='POINT', location=(0, 3.2, 3.0))
        cove_l = bpy.context.active_object
        cove_l.data.energy = 100.0
        cove_l.data.color = (1.0, 0.94, 0.88)

    return pointer, pointer_tip, hand, arm

def setup_camera_and_animation(pointer, pointer_tip, hand, arm):
    # Child's eye level POV camera (Height 1.18m looking toward the wall chart and nurse)
    bpy.ops.object.camera_add(location=(0, 1.2, 1.45), rotation=(math.radians(88), 0, math.radians(-3)))
    cam = bpy.context.active_object
    cam.data.lens = 35  # Natural eye-level portrait lens
    bpy.context.scene.camera = cam

    scene = bpy.context.scene
    scene.frame_start = 1
    scene.frame_end = 144  # 6.0 seconds @ 24fps

    # Gentle guidance motion on pointer pointing at the Airplane icon
    if pointer:
        pointer.keyframe_insert(data_path="location", frame=1)
        pointer.location = (0.10, 3.95, 1.80)
        pointer.keyframe_insert(data_path="location", frame=70)
        pointer.location = (0.12, 3.95, 1.82)
        pointer.keyframe_insert(data_path="location", frame=144)

    return cam

def render_sequence(out_dir, chart_texture_path, is_id_mask=False):
    prefix = "C4_chart_match_id_mask" if is_id_mask else "C4_chart_match"
    print(f"🎬 [Starting] Rendering sequence for: {prefix}...")
    clear_scene()
    setup_render_common(fps=24, res_x=1280, res_y=720)
    pointer, pointer_tip, hand, arm = build_chart_scene(is_id_mask=is_id_mask, chart_texture_path=chart_texture_path)
    cam = setup_camera_and_animation(pointer, pointer_tip, hand, arm)

    scene = bpy.context.scene
    temp_prefix = os.path.join(out_dir, f"{prefix}_frame_")
    scene.render.filepath = temp_prefix
    
    # 1. Render Frame Sequence
    bpy.ops.render.render(animation=True)

    # 2. Render Single Keyframe Preview (Frame 60: Pointer clearly at Airplane icon)
    scene.frame_set(60)
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
        if f.startswith(f"{prefix}_frame_") and f.endswith(".png") and not f.endswith("_preview.png"):
            try:
                os.remove(os.path.join(out_dir, f))
            except Exception:
                pass
    print(f"✅ Successfully generated {mp4_out}")

if __name__ == "__main__":
    out_dir = r"d:\Github\Unity\cocolink\Docs\EyeClinic\Blender\renders\real"
    chart_texture_path = r"d:\Github\Unity\cocolink\Docs\EyeClinic\Graphic\real\B5276385504_41125294488.jpg"
    os.makedirs(out_dir, exist_ok=True)
    
    # 1. Render Realistic Previs Video & Graphic Asset
    render_sequence(out_dir, chart_texture_path, is_id_mask=False)
    
    # 2. Render Semantic Color ID Mask
    render_sequence(out_dir, chart_texture_path, is_id_mask=True)
    print("🎉 C4_ChartMatch Previs renders completed successfully!")
