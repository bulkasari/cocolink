"""
Blender 5.2 Python Script for C3_ChinRest Previs
- Photorealistic & Stylized 3D Previs Scene matching `real_eyeclinic_exam_room.jpeg`
- 1st-person POV approach to autorefractor chinrest (5 seconds, 120 frames @ 24fps)
- Outputs:
  1. C3_chinrest.mp4 (Realistic 3D Previs)
  2. C3_chinrest_id_mask.mp4 (Semantic Color ID Mask)
  3. C3_chinrest_preview.png (Keyframe preview)
  4. C3_chinrest_id_mask_preview.png (ID mask keyframe preview)
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

def create_pbr_material(name, base_color, roughness=0.3, metallic=0.0, specular=0.5):
    mat = bpy.data.materials.new(name=name)
    mat.use_nodes = True
    nodes = mat.node_tree.nodes
    bsdf = nodes.get("Principled BSDF")
    if bsdf:
        bsdf.inputs['Base Color'].default_value = base_color
        bsdf.inputs['Roughness'].default_value = roughness
        bsdf.inputs['Metallic'].default_value = metallic
        if 'Specular IOR Level' in bsdf.inputs:
            bsdf.inputs['Specular IOR Level'].default_value = specular
        elif 'Specular' in bsdf.inputs:
            bsdf.inputs['Specular'].default_value = specular
    return mat

def create_wood_floor_mat():
    mat = bpy.data.materials.new(name="WoodFloorMat")
    mat.use_nodes = True
    nodes = mat.node_tree.nodes
    links = mat.node_tree.links
    bsdf = nodes.get("Principled BSDF")
    if bsdf:
        bsdf.inputs['Base Color'].default_value = (0.82, 0.65, 0.46, 1.0)
        bsdf.inputs['Roughness'].default_value = 0.35
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

def build_scene(is_id_mask=False):
    # --- Materials Setup ---
    if is_id_mask:
        mat_bg = create_emission_material("ID_Black", (0, 0, 0, 1))          # Background / Walls / Floor
        mat_desk = create_emission_material("ID_Desk", (1, 1, 0, 1))         # Yellow: #FFFF00 Desk
        mat_mach = create_emission_material("ID_Mach", (0, 0, 1, 1))         # Blue: #0000FF Autorefractor Body
        mat_pad = create_emission_material("ID_Chin", (1, 0, 0, 1))          # Red: #FF0000 Chinrest & Forehead Rest
        mat_lens = create_emission_material("ID_Lens", (0, 1, 1, 1))         # Cyan: #00FFFF Optical Lenses
        mat_nurse = create_emission_material("ID_Nurse", (0, 1, 0, 1))       # Green: #00FF00 Nurse Hand/Body
    else:
        mat_bg_floor = create_wood_floor_mat()
        mat_bg_wall = create_pbr_material("WallMat", (0.96, 0.94, 0.90, 1.0), roughness=0.6)
        mat_wood_cabinet = create_pbr_material("WoodCabMat", (0.80, 0.62, 0.44, 1.0), roughness=0.4)
        mat_desk = create_pbr_material("DeskMat", (0.92, 0.93, 0.94, 1.0), roughness=0.25)
        mat_mach = create_pbr_material("MachWhiteMat", (0.97, 0.97, 0.98, 1.0), roughness=0.2)
        mat_mach_dark = create_pbr_material("MachDarkMat", (0.15, 0.17, 0.20, 1.0), roughness=0.3)
        mat_pad = create_pbr_material("PadDarkBlueMat", (0.18, 0.22, 0.28, 1.0), roughness=0.45) # Pediatric navy cushion
        mat_tissue = create_pbr_material("TissueMat", (0.98, 0.98, 0.96, 1.0), roughness=0.7)
        mat_lens = create_pbr_material("LensGlassMat", (0.02, 0.02, 0.04, 1.0), roughness=0.05, metallic=0.9)
        mat_lens_led_green = create_emission_material("LEDGreen", (0.1, 1.0, 0.3, 1.0))
        mat_lens_led_orange = create_emission_material("LEDOrange", (1.0, 0.6, 0.1, 1.0))
        mat_nurse_scrub = create_pbr_material("NurseScrub", (0.55, 0.85, 0.75, 1.0), roughness=0.5) # Mint scrub
        mat_nurse_skin = create_pbr_material("NurseSkin", (0.95, 0.82, 0.74, 1.0), roughness=0.35)
        mat_gown_green = create_pbr_material("GownGreen", (0.4, 0.8, 0.3, 1.0), roughness=0.6)
        mat_gown_yellow = create_pbr_material("GownYellow", (0.95, 0.8, 0.2, 1.0), roughness=0.6)
        mat_gown_pink = create_pbr_material("GownPink", (0.95, 0.5, 0.6, 1.0), roughness=0.6)
        mat_gown_blue = create_pbr_material("GownBlue", (0.3, 0.6, 0.9, 1.0), roughness=0.6)

    # 1. Environment: Floor & Walls
    # Floor
    bpy.ops.mesh.primitive_plane_add(size=16, location=(0, 2, 0))
    floor = bpy.context.active_object
    floor.data.materials.append(mat_bg if is_id_mask else mat_bg_floor)

    # Back Wall
    bpy.ops.mesh.primitive_plane_add(size=16, location=(0, 5.5, 3), rotation=(math.radians(90), 0, 0))
    bwall = bpy.context.active_object
    bwall.data.materials.append(mat_bg if is_id_mask else mat_bg_wall)

    # Left Wall
    bpy.ops.mesh.primitive_plane_add(size=16, location=(-3.5, 2, 3), rotation=(0, math.radians(90), 0))
    lwall = bpy.context.active_object
    lwall.data.materials.append(mat_bg if is_id_mask else mat_bg_wall)

    # Right Wall
    bpy.ops.mesh.primitive_plane_add(size=16, location=(3.5, 2, 3), rotation=(0, math.radians(-90), 0))
    rwall = bpy.context.active_object
    rwall.data.materials.append(mat_bg if is_id_mask else mat_bg_wall)

    if not is_id_mask:
        # Background: Cabinet
        bpy.ops.mesh.primitive_cube_add(size=1, location=(-1.2, 5.2, 1.8))
        cab = bpy.context.active_object
        cab.scale = (2.2, 0.5, 2.0)
        cab.data.materials.append(mat_wood_cabinet)

        # Wall Poster: Eye Chart on Right Wall
        bpy.ops.mesh.primitive_plane_add(size=1, location=(3.45, 2.5, 2.2), rotation=(0, math.radians(-90), 0))
        poster = bpy.context.active_object
        poster.scale = (0.7, 1.0, 1.0)
        mat_poster = create_pbr_material("ChartPoster", (0.95, 0.95, 0.95, 1.0), roughness=0.4)
        poster.data.materials.append(mat_poster)

        # Hanging colorful gowns on right
        gowns = [(mat_gown_green, 1.4), (mat_gown_yellow, 1.7), (mat_gown_pink, 2.0), (mat_gown_blue, 2.3)]
        for gmat, gy in gowns:
            bpy.ops.mesh.primitive_cylinder_add(radius=0.08, depth=0.75, location=(3.38, gy, 1.5))
            gown_obj = bpy.context.active_object
            gown_obj.scale = (0.6, 1.0, 1.0)
            gown_obj.data.materials.append(gmat)

    # 2. Examination Table
    bpy.ops.mesh.primitive_cube_add(size=1, location=(0, 2.2, 0.72))
    desk = bpy.context.active_object
    desk.scale = (1.5, 0.9, 0.72)
    desk.data.materials.append(mat_desk if is_id_mask else mat_desk)

    # Table Stand Column
    bpy.ops.mesh.primitive_cylinder_add(radius=0.10, depth=0.6, location=(0, 2.2, 0.35))
    table_leg = bpy.context.active_object
    table_leg.data.materials.append(mat_desk if is_id_mask else mat_desk)

    # 3. Pediatric Autorefractor Main Body
    # Machine Base on Table
    bpy.ops.mesh.primitive_cube_add(size=1, location=(0, 2.15, 0.78))
    mach_base = bpy.context.active_object
    mach_base.scale = (0.58, 0.65, 0.08)
    mach_base.data.materials.append(mat_mach)

    # Machine Main Housing (Upper White Shell)
    bpy.ops.mesh.primitive_cube_add(size=1, location=(0, 2.22, 1.25))
    mach_housing = bpy.context.active_object
    mach_housing.scale = (0.54, 0.62, 0.65)
    mach_housing.data.materials.append(mat_mach)

    # Rear LCD Monitor on Doctor's side
    bpy.ops.mesh.primitive_cube_add(size=1, location=(0.28, 2.50, 1.15), rotation=(math.radians(-20), math.radians(15), 0))
    mach_lcd = bpy.context.active_object
    mach_lcd.scale = (0.24, 0.04, 0.18)
    mach_lcd.data.materials.append(mat_mach if is_id_mask else mat_mach_dark)

    # Joystick on base
    bpy.ops.mesh.primitive_cylinder_add(radius=0.02, depth=0.14, location=(0.18, 2.45, 0.88))
    joy = bpy.context.active_object
    joy.data.materials.append(mat_mach if is_id_mask else mat_mach_dark)

    # 4. Binocular Visor & Optical Lenses (Front Facing Child)
    # Dark Visor Oval Plate
    bpy.ops.mesh.primitive_cube_add(size=1, location=(0, 1.88, 1.34))
    visor = bpy.context.active_object
    visor.scale = (0.36, 0.05, 0.20)
    visor.data.materials.append(mat_mach if is_id_mask else mat_mach_dark)

    # Left Lens
    bpy.ops.mesh.primitive_cylinder_add(radius=0.065, depth=0.04, location=(-0.09, 1.85, 1.34), rotation=(math.radians(90), 0, 0))
    lens_l = bpy.context.active_object
    lens_l.data.materials.append(mat_lens)

    # Right Lens
    bpy.ops.mesh.primitive_cylinder_add(radius=0.065, depth=0.04, location=(0.09, 1.85, 1.34), rotation=(math.radians(90), 0, 0))
    lens_r = bpy.context.active_object
    lens_r.data.materials.append(mat_lens)

    if not is_id_mask:
        # Small LED indicator dots beside lenses
        bpy.ops.mesh.primitive_uv_sphere_add(radius=0.012, location=(-0.16, 1.84, 1.34))
        led1 = bpy.context.active_object
        led1.data.materials.append(mat_lens_led_green)
        
        bpy.ops.mesh.primitive_uv_sphere_add(radius=0.012, location=(0.16, 1.84, 1.34))
        led2 = bpy.context.active_object
        led2.data.materials.append(mat_lens_led_orange)

    # 5. Chinrest & Forehead Rest Arch Structure
    # Left Vertical Support Column
    bpy.ops.mesh.primitive_cylinder_add(radius=0.022, depth=0.62, location=(-0.25, 1.72, 1.25))
    post_l = bpy.context.active_object
    post_l.data.materials.append(mat_mach)

    # Right Vertical Support Column
    bpy.ops.mesh.primitive_cylinder_add(radius=0.022, depth=0.62, location=(0.25, 1.72, 1.25))
    post_r = bpy.context.active_object
    post_r.data.materials.append(mat_mach)

    # Top Forehead Rest Bar
    bpy.ops.mesh.primitive_cylinder_add(radius=0.028, depth=0.50, location=(0, 1.72, 1.54), rotation=(0, math.radians(90), 0))
    f_bar = bpy.context.active_object
    f_bar.data.materials.append(mat_pad)

    # Forehead Curved Pad
    bpy.ops.mesh.primitive_cube_add(size=1, location=(0, 1.71, 1.54))
    f_pad = bpy.context.active_object
    f_pad.scale = (0.28, 0.05, 0.05)
    f_pad.data.materials.append(mat_pad)

    # Bottom Chinrest Cup (Navy Pad)
    bpy.ops.mesh.primitive_cube_add(size=1, location=(0, 1.70, 1.05))
    chin_cup = bpy.context.active_object
    chin_cup.scale = (0.26, 0.14, 0.04)
    chin_cup.data.materials.append(mat_pad)

    # Chinrest Adjustment Knobs on sides
    bpy.ops.mesh.primitive_cylinder_add(radius=0.032, depth=0.06, location=(-0.28, 1.72, 1.05), rotation=(0, math.radians(90), 0))
    knob_l = bpy.context.active_object
    knob_l.data.materials.append(mat_mach if is_id_mask else mat_mach_dark)

    bpy.ops.mesh.primitive_cylinder_add(radius=0.032, depth=0.06, location=(0.28, 1.72, 1.05), rotation=(0, math.radians(90), 0))
    knob_r = bpy.context.active_object
    knob_r.data.materials.append(mat_mach if is_id_mask else mat_mach_dark)

    if not is_id_mask:
        # Sanitary paper strip on chinrest
        bpy.ops.mesh.primitive_plane_add(size=1, location=(0, 1.70, 1.072))
        tissue = bpy.context.active_object
        tissue.scale = (0.16, 0.07, 1.0)
        tissue.data.materials.append(mat_tissue)

    # 6. Optometrist Nurse Guiding Hand & Arm (Friendly Guiding Pose on Right)
    # Upper Body Torso
    bpy.ops.mesh.primitive_cube_add(size=1, location=(0.78, 2.0, 1.35))
    nurse_body = bpy.context.active_object
    nurse_body.scale = (0.35, 0.25, 0.65)
    nurse_body.data.materials.append(mat_nurse if is_id_mask else mat_nurse_scrub)

    # Nurse Head
    bpy.ops.mesh.primitive_uv_sphere_add(radius=0.12, location=(0.78, 2.0, 1.78))
    nurse_head = bpy.context.active_object
    nurse_head.data.materials.append(mat_nurse if is_id_mask else mat_nurse_skin)

    # Guiding Arm reaching toward chinrest
    bpy.ops.mesh.primitive_cylinder_add(radius=0.045, depth=0.45, location=(0.52, 1.75, 1.15), rotation=(math.radians(35), math.radians(-35), math.radians(50)))
    arm = bpy.context.active_object
    arm.name = "NurseArm"
    arm.data.materials.append(mat_nurse if is_id_mask else mat_nurse_scrub)

    # Guiding Hand near chinrest
    bpy.ops.mesh.primitive_uv_sphere_add(radius=0.055, location=(0.35, 1.66, 1.08))
    hand = bpy.context.active_object
    hand.name = "NurseHand"
    hand.scale = (1.3, 0.8, 0.4)
    hand.data.materials.append(mat_nurse if is_id_mask else mat_nurse_skin)

    # 7. Cinematic Lighting Setup (Real Preview Mode)
    if not is_id_mask:
        # Warm Key Light (Above Front-Left)
        bpy.ops.object.light_add(type='AREA', location=(-1.2, 0.6, 2.8), rotation=(math.radians(45), math.radians(-25), math.radians(20)))
        key_light = bpy.context.active_object
        key_light.data.energy = 220.0
        key_light.data.size = 1.5
        key_light.data.color = (1.0, 0.96, 0.90)

        # Soft Fill Light (Right Side)
        bpy.ops.object.light_add(type='AREA', location=(1.8, 0.8, 2.4), rotation=(math.radians(40), math.radians(30), math.radians(-20)))
        fill_light = bpy.context.active_object
        fill_light.data.energy = 140.0
        fill_light.data.size = 1.8
        fill_light.data.color = (0.92, 0.96, 1.0)

        # Warm Ceiling Ambient Light
        bpy.ops.object.light_add(type='POINT', location=(0, 2.2, 3.2))
        cove_light = bpy.context.active_object
        cove_light.data.energy = 160.0
        cove_light.data.color = (1.0, 0.94, 0.88)

        # Chinrest Rim/Accent Light
        bpy.ops.object.light_add(type='SPOT', location=(0, 1.2, 2.0), rotation=(math.radians(35), 0, 0))
        spot = bpy.context.active_object
        spot.data.energy = 60.0
        spot.data.spot_size = math.radians(45)
        spot.data.color = (1.0, 0.98, 0.94)

    return hand, arm

def setup_camera_animation():
    # 1st-Person POV Camera (Child seated in chair approaching chinrest)
    bpy.ops.object.camera_add(location=(0, -0.20, 1.45), rotation=(math.radians(88), 0, 0))
    cam = bpy.context.active_object
    cam.data.lens = 28  # 28mm wide angle for immersive 1st-person POV
    bpy.context.scene.camera = cam

    scene = bpy.context.scene
    scene.frame_start = 1
    scene.frame_end = 120  # 5.0 seconds @ 24fps

    # --- Frame 1 (0.0s): Seated comfortably, looking at the clinic machine & nurse smiling ---
    cam.location = (0.0, -0.20, 1.45)
    cam.rotation_euler = (math.radians(87), 0, 0)
    cam.keyframe_insert(data_path="location", frame=1)
    cam.keyframe_insert(data_path="rotation_euler", frame=1)

    # --- Frame 40 (1.6s): Child gently leans forward, guided by nurse hand ---
    cam.location = (0.0, 0.65, 1.38)
    cam.rotation_euler = (math.radians(85), 0, 0)
    cam.keyframe_insert(data_path="location", frame=40)
    cam.keyframe_insert(data_path="rotation_euler", frame=40)

    # --- Frame 80 (3.3s): Approaching chinrest cup and forehead bar closely ---
    cam.location = (0.0, 1.20, 1.34)
    cam.rotation_euler = (math.radians(88), 0, 0)
    cam.keyframe_insert(data_path="location", frame=80)
    cam.keyframe_insert(data_path="rotation_euler", frame=80)

    # --- Frame 105~120 (4.4s ~ 5.0s): Chin resting comfortably on pad, forehead on bar, looking straight into lenses ---
    cam.location = (0.0, 1.48, 1.34)
    cam.rotation_euler = (math.radians(90), 0, 0)
    cam.keyframe_insert(data_path="location", frame=105)
    cam.keyframe_insert(data_path="rotation_euler", frame=105)

    cam.location = (0.0, 1.49, 1.34)
    cam.rotation_euler = (math.radians(90), 0, 0)
    cam.keyframe_insert(data_path="location", frame=120)
    cam.keyframe_insert(data_path="rotation_euler", frame=120)

    return cam

def render_sequence(out_dir, is_id_mask=False):
    prefix = "C3_chinrest_id_mask" if is_id_mask else "C3_chinrest"
    print(f"🎬 [Starting] Rendering sequence for: {prefix}...")
    clear_scene()
    setup_render_common(fps=24, res_x=1280, res_y=720) # 720p HD for fast clean render
    hand, arm = build_scene(is_id_mask=is_id_mask)
    cam = setup_camera_animation()

    # Hand subtle guiding animation
    if hand and arm:
        hand.keyframe_insert(data_path="location", frame=1)
        hand.location = (0.30, 1.62, 1.12)
        hand.keyframe_insert(data_path="location", frame=50)
        hand.location = (0.35, 1.66, 1.08)
        hand.keyframe_insert(data_path="location", frame=120)

    scene = bpy.context.scene
    temp_prefix = os.path.join(out_dir, f"{prefix}_frame_")
    scene.render.filepath = temp_prefix
    
    # 1. Render Frame Sequence
    bpy.ops.render.render(animation=True)

    # 2. Render Single Keyframe Previews (Frames 1, 45, 110)
    if not is_id_mask:
        scene.frame_set(1)
        scene.render.filepath = os.path.join(out_dir, f"{prefix}_start.png")
        bpy.ops.render.render(write_still=True)

        scene.frame_set(45)
        scene.render.filepath = os.path.join(out_dir, f"{prefix}_approach.png")
        bpy.ops.render.render(write_still=True)

        scene.frame_set(110)
        scene.render.filepath = os.path.join(out_dir, f"{prefix}_rest.png")
        bpy.ops.render.render(write_still=True)
    
    scene.frame_set(45)
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
            except Exception as e:
                pass
    print(f"✅ Successfully generated {mp4_out}")

if __name__ == "__main__":
    out_dir = r"d:\Github\Unity\cocolink\Docs\EyeClinic\Blender\renders\real"
    os.makedirs(out_dir, exist_ok=True)
    
    # Render realistic previs video
    render_sequence(out_dir, is_id_mask=False)
    
    # Render AI Video conditioning Semantic ID Mask
    render_sequence(out_dir, is_id_mask=True)
    print("🎉 All Previs renders completed successfully!")
