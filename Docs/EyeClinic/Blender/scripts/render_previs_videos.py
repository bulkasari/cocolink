"""
CocoLink 소아 안과 Step 3 시연 프리비즈 3개 씬 애니메이션 & 비디오 렌더러 (Blender 5.2)
- Scene 1: 3-1_chinrest.mp4 (코코가 턱을 올리는 씬)
- Scene 2: 3-2_balloon.mp4 (열기구를 바라보고 흐려졌다 또렷해지는 씬)
- Scene 3: 3-3_sunglasses.mp4 (별 선글라스를 선물받고 기뻐하는 씬)
"""

import bpy
import math
import os

def clear_scene():
    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.object.delete()

def setup_render_common(fps=24, res_x=1280, res_y=720):
    scene = bpy.context.scene
    scene.render.resolution_x = res_x
    scene.render.resolution_y = res_y
    scene.render.fps = fps
    scene.render.image_settings.file_format = 'PNG'

def create_material(name, color, roughness=0.35):
    mat = bpy.data.materials.new(name=name)
    mat.use_nodes = True
    bsdf = mat.node_tree.nodes.get("Principled BSDF")
    if bsdf:
        bsdf.inputs['Base Color'].default_value = color
        bsdf.inputs['Roughness'].default_value = roughness
    return mat

def build_base_environment():
    # 바닥
    bpy.ops.mesh.primitive_plane_add(size=14, location=(0, 0, 0))
    floor = bpy.context.active_object
    floor.name = "Floor"
    floor.data.materials.append(create_material("FloorMat", (0.92, 0.88, 0.82, 1.0)))

    # 뒷벽 (부드러운 민트)
    bpy.ops.mesh.primitive_plane_add(size=14, location=(0, 6, 4), rotation=(math.radians(90), 0, 0))
    wall = bpy.context.active_object
    wall.name = "BackWall"
    wall.data.materials.append(create_material("WallMat", (0.82, 0.94, 0.92, 1.0)))

    # 책상
    bpy.ops.mesh.primitive_cube_add(size=1, location=(0, 2.2, 0.75))
    desk = bpy.context.active_object
    desk.scale = (2.0, 1.1, 0.75)
    desk.data.materials.append(create_material("DeskMat", (0.85, 0.65, 0.45, 1.0)))

    # 검사기 본체
    bpy.ops.mesh.primitive_cube_add(size=1, location=(0, 2.3, 1.6))
    machine = bpy.context.active_object
    machine.scale = (0.75, 0.85, 0.65)
    machine.data.materials.append(create_material("MachineMat", (0.96, 0.96, 0.98, 1.0)))

    # 턱받침
    bpy.ops.mesh.primitive_cylinder_add(radius=0.045, depth=0.32, location=(0, 1.7, 1.5), rotation=(0, math.radians(90), 0))
    chinrest = bpy.context.active_object
    chinrest.data.materials.append(create_material("ChinrestMat", (0.2, 0.65, 0.9, 1.0)))

    # 렌즈
    bpy.ops.mesh.primitive_cylinder_add(radius=0.09, depth=0.08, location=(0, 1.85, 1.72), rotation=(math.radians(90), 0, 0))
    lens = bpy.context.active_object
    lens.data.materials.append(create_material("LensMat", (0.1, 0.1, 0.15, 1.0)))

    # 조명
    bpy.ops.object.light_add(type='SUN', location=(4, -4, 7))
    sun = bpy.context.active_object
    sun.data.energy = 4.0
    sun.data.color = (1.0, 0.98, 0.92)

    bpy.ops.object.light_add(type='POINT', location=(-3, 1, 3))
    fill = bpy.context.active_object
    fill.data.energy = 120
    fill.data.color = (0.9, 0.96, 1.0)

def build_coco_character():
    mat_fur = create_material("CocoFur", (0.58, 0.38, 0.22, 1.0))
    mat_scarf = create_material("CocoScarf", (0.98, 0.85, 0.12, 1.0))

    # 의자
    bpy.ops.mesh.primitive_cylinder_add(radius=0.38, depth=0.55, location=(0, 0.9, 0.55))
    chair = bpy.context.active_object
    chair.data.materials.append(create_material("ChairMat", (0.35, 0.8, 0.7, 1.0)))

    # 몸통
    bpy.ops.mesh.primitive_uv_sphere_add(radius=0.38, location=(0, 0.9, 1.1))
    body = bpy.context.active_object
    body.name = "Coco_Body"
    body.scale = (1.0, 0.9, 1.15)
    body.data.materials.append(mat_fur)

    # 스카프
    bpy.ops.mesh.primitive_torus_add(major_radius=0.26, minor_radius=0.065, location=(0, 0.9, 1.42))
    scarf = bpy.context.active_object
    scarf.name = "Coco_Scarf"
    scarf.data.materials.append(mat_scarf)

    # 머리
    bpy.ops.mesh.primitive_uv_sphere_add(radius=0.34, location=(0, 0.92, 1.72))
    head = bpy.context.active_object
    head.name = "Coco_Head"
    head.data.materials.append(mat_fur)

    # 귀 좌/우
    bpy.ops.mesh.primitive_uv_sphere_add(radius=0.11, location=(-0.24, 0.92, 2.02))
    ear_l = bpy.context.active_object
    ear_l.name = "Coco_Ear_L"
    ear_l.data.materials.append(mat_fur)
    ear_l.parent = head

    bpy.ops.mesh.primitive_uv_sphere_add(radius=0.11, location=(0.24, 0.92, 2.02))
    ear_r = bpy.context.active_object
    ear_r.name = "Coco_Ear_R"
    ear_r.data.materials.append(mat_fur)
    ear_r.parent = head

    return head, body, scarf

def render_scene_1(out_dir):
    """Scene 1 (3-1): 곰돌이가 턱을 올리는 씬 (5초 = 120프레임)"""
    print("\n🎬 [Scene 1/3] 3-1_chinrest 씬 렌더링 준비...")
    clear_scene()
    setup_render_common()
    build_base_environment()
    head, body, scarf = build_coco_character()

    # 카메라 설정
    bpy.ops.object.camera_add(location=(2.3, -0.8, 1.9), rotation=(math.radians(75), 0, math.radians(55)))
    cam = bpy.context.active_object
    cam.data.lens = 45
    bpy.context.scene.camera = cam

    # 코코 머리 & 몸통 이동 애니메이션 (턱받침으로 다가가기)
    scene = bpy.context.scene
    scene.frame_start = 1
    scene.frame_end = 120  # 5초

    # 프레임 1: 살짝 뒤에 앉아있음
    head.location = (0, 0.92, 1.72)
    head.keyframe_insert(data_path="location", frame=1)
    body.location = (0, 0.9, 1.1)
    body.keyframe_insert(data_path="location", frame=1)

    # 프레임 60: 앞으로 숙이며 턱받침에 착 댐
    head.location = (0, 1.6, 1.6)
    head.keyframe_insert(data_path="location", frame=60)
    body.location = (0, 1.2, 1.15)
    body.keyframe_insert(data_path="location", frame=60)

    # 프레임 120까지 유지
    head.keyframe_insert(data_path="location", frame=120)
    body.keyframe_insert(data_path="location", frame=120)

    out_file = os.path.join(out_dir, "3-1_chinrest.mp4")
    scene.render.filepath = out_file
    print(f"🎥 렌더링 시작 ➔ {out_file}")
    bpy.ops.render.render(animation=True)
    print("✅ Scene 1 렌더 완료!")

def render_scene_2(out_dir):
    """Scene 2 (3-2): 열기구 보기 렌더링 (5초 = 120프레임)"""
    print("\n🎬 [Scene 2/3] 3-2_balloon 씬 렌더링 준비...")
    clear_scene()
    setup_render_common()

    # 배경 (푸른 하늘과 초원)
    bpy.ops.mesh.primitive_plane_add(size=20, location=(0, 10, 3), rotation=(math.radians(90), 0, 0))
    sky = bpy.context.active_object
    sky.data.materials.append(create_material("SkyMat", (0.55, 0.82, 0.98, 1.0)))

    bpy.ops.mesh.primitive_plane_add(size=20, location=(0, 5, -1))
    grass = bpy.context.active_object
    grass.data.materials.append(create_material("GrassMat", (0.4, 0.8, 0.35, 1.0)))

    # 빨간 열기구 생성
    bpy.ops.mesh.primitive_uv_sphere_add(radius=0.9, location=(0, 6, 2.5))
    balloon = bpy.context.active_object
    balloon.name = "HotAirBalloon"
    balloon.data.materials.append(create_material("BalloonMat", (0.95, 0.22, 0.2, 1.0)))

    # 바구니
    bpy.ops.mesh.primitive_cube_add(size=0.35, location=(0, 6, 1.2))
    basket = bpy.context.active_object
    basket.data.materials.append(create_material("BasketMat", (0.7, 0.45, 0.25, 1.0)))
    basket.parent = balloon

    # 조명
    bpy.ops.object.light_add(type='SUN', location=(3, 2, 8))
    sun = bpy.context.active_object
    sun.data.energy = 5.0

    # 카메라 (열기구 정면 샷)
    bpy.ops.object.camera_add(location=(0, 0, 2.2), rotation=(math.radians(90), 0, 0))
    cam = bpy.context.active_object
    cam.data.lens = 50
    bpy.context.scene.camera = cam

    # 열기구 둥실둥실 애니메이션
    scene = bpy.context.scene
    scene.frame_start = 1
    scene.frame_end = 120

    balloon.location = (0, 6, 2.2)
    balloon.keyframe_insert(data_path="location", frame=1)

    balloon.location = (0.2, 6, 2.7)
    balloon.keyframe_insert(data_path="location", frame=60)

    balloon.location = (0, 6, 2.4)
    balloon.keyframe_insert(data_path="location", frame=120)

    out_file = os.path.join(out_dir, "3-2_balloon.mp4")
    scene.render.filepath = out_file
    print(f"🎥 렌더링 시작 ➔ {out_file}")
    bpy.ops.render.render(animation=True)
    print("✅ Scene 2 렌더 완료!")

def render_scene_3(out_dir):
    """Scene 3 (3-3): 별 선글라스 획득 씬 (5초 = 120프레임)"""
    print("\n🎬 [Scene 3/3] 3-3_sunglasses 씬 렌더링 준비...")
    clear_scene()
    setup_render_common()
    build_base_environment()
    head, body, scarf = build_coco_character()

    # 별 선글라스 오브젝트
    mat_gold = create_material("GoldMat", (1.0, 0.84, 0.0, 1.0), roughness=0.1)
    
    bpy.ops.mesh.primitive_cylinder_add(radius=0.14, depth=0.03, location=(-0.16, 0.62, 1.76), rotation=(math.radians(90), 0, 0))
    glass_l = bpy.context.active_object
    glass_l.data.materials.append(mat_gold)
    glass_l.name = "Glass_L"
    
    bpy.ops.mesh.primitive_cylinder_add(radius=0.14, depth=0.03, location=(0.16, 0.62, 1.76), rotation=(math.radians(90), 0, 0))
    glass_r = bpy.context.active_object
    glass_r.data.materials.append(mat_gold)
    glass_r.name = "Glass_R"

    # 안경 브릿지
    bpy.ops.mesh.primitive_cube_add(size=1, location=(0, 0.62, 1.76))
    bridge = bpy.context.active_object
    bridge.scale = (0.1, 0.02, 0.02)
    bridge.data.materials.append(mat_gold)

    # 카메라 정면 클로즈업
    bpy.ops.object.camera_add(location=(0, -0.6, 1.75), rotation=(math.radians(90), 0, 0))
    cam = bpy.context.active_object
    cam.data.lens = 55
    bpy.context.scene.camera = cam

    # 코코 기쁨 바운스 애니메이션
    scene = bpy.context.scene
    scene.frame_start = 1
    scene.frame_end = 120

    # 안경 착용 후 기뻐서 통통 뛰기
    for f, z_offset in [(1, 0), (30, 0.08), (60, 0), (90, 0.08), (120, 0)]:
        head.location = (0, 0.92, 1.72 + z_offset)
        head.keyframe_insert(data_path="location", frame=f)
        glass_l.location = (-0.16, 0.62, 1.76 + z_offset)
        glass_l.keyframe_insert(data_path="location", frame=f)
        glass_r.location = (0.16, 0.62, 1.76 + z_offset)
        glass_r.keyframe_insert(data_path="location", frame=f)
        bridge.location = (0, 0.62, 1.76 + z_offset)
        bridge.keyframe_insert(data_path="location", frame=f)

    out_file = os.path.join(out_dir, "3-3_sunglasses.mp4")
    scene.render.filepath = out_file
    print(f"🎥 렌더링 시작 ➔ {out_file}")
    bpy.ops.render.render(animation=True)
    print("✅ Scene 3 렌더 완료!")

def main():
    script_dir = os.path.dirname(os.path.abspath(__file__)) if '__file__' in globals() else "d:/Github/Unity/cocolink/Docs/EyeClinic/Blender/scripts"
    out_dir = os.path.abspath(os.path.join(script_dir, "..", "renders"))
    os.makedirs(out_dir, exist_ok=True)

    print(f"==================================================")
    print(f"  CocoLink Step 3 3D 프리비즈 렌더러 시작")
    print(f"  출력 폴더: {out_dir}")
    print(f"==================================================")

    render_scene_1(out_dir)
    render_scene_2(out_dir)
    render_scene_3(out_dir)

    print("\n🎉 모든 프리비즈 영상(MP4) 렌더링이 성공적으로 완료되었습니다!")

if __name__ == "__main__":
    main()
