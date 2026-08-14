"""
CocoLink 소아 안과 3D 프리비즈(Previs) 자동 씬 생성 스크립트 (Blender 4.x / 5.x)
실행 방법: Blender 상단 메뉴 'Scripting' 탭 -> 'New' -> 이 코드 붙여넣기 -> 'Run Script (Alt+P)'
"""

import bpy
import math

def clear_scene():
    """기존 기본 오브젝트 정리"""
    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.object.delete()

def setup_render_settings():
    """렌더 및 카메라 규격 설정 (16:9, EEVEE, 24fps)"""
    scene = bpy.context.scene
    scene.render.resolution_x = 1920
    scene.render.resolution_y = 1080
    scene.render.fps = 24
    scene.frame_start = 1
    scene.frame_end = 360  # 총 15초 분량

def create_material(name, color, roughness=0.4):
    """간단한 색상 머티리얼 생성"""
    mat = bpy.data.materials.new(name=name)
    mat.use_nodes = True
    bsdf = mat.node_tree.nodes.get("Principled BSDF")
    if bsdf:
        bsdf.inputs['Base Color'].default_value = color
        bsdf.inputs['Roughness'].default_value = roughness
    return mat

def create_eye_clinic_environment():
    """안과 예비검사실 방 및 바닥 생성"""
    mat_floor = create_material("FloorMat", (0.9, 0.85, 0.75, 1.0))
    mat_wall = create_material("WallMat", (0.85, 0.93, 0.92, 1.0))
    
    # 바닥
    bpy.ops.mesh.primitive_plane_add(size=12, location=(0, 0, 0))
    floor = bpy.context.active_object
    floor.name = "Floor"
    floor.data.materials.append(mat_floor)
    
    # 뒷벽
    bpy.ops.mesh.primitive_plane_add(size=12, location=(0, 5, 4), rotation=(math.radians(90), 0, 0))
    wall = bpy.context.active_object
    wall.name = "BackWall"
    wall.data.materials.append(mat_wall)

def create_autorefrac_machine():
    """소아용 자동굴절검사기 (열기구 기계 & 턱받침) 블록아웃"""
    mat_machine = create_material("MachineMat", (0.95, 0.95, 0.97, 1.0))
    mat_chinrest = create_material("ChinrestMat", (0.2, 0.6, 0.85, 1.0))
    mat_screen = create_material("ScreenMat", (0.95, 0.3, 0.2, 1.0)) # 열기구 화면 빨간색
    
    # 책상
    bpy.ops.mesh.primitive_cube_add(size=1, location=(0, 2, 0.75))
    table = bpy.context.active_object
    table.name = "Desk"
    table.scale = (1.8, 1.0, 0.75)
    table.data.materials.append(create_material("DeskMat", (0.8, 0.6, 0.4, 1.0)))
    
    # 기계 본체
    bpy.ops.mesh.primitive_cube_add(size=1, location=(0, 2.1, 1.6))
    body = bpy.context.active_object
    body.name = "Autorefractor_Body"
    body.scale = (0.7, 0.8, 0.6)
    body.data.materials.append(mat_machine)
    
    # 턱받침 기둥 및 턱받침 바
    bpy.ops.mesh.primitive_cylinder_add(radius=0.03, depth=0.4, location=(0, 1.6, 1.65))
    pole = bpy.context.active_object
    pole.name = "Chinrest_Pole"
    
    bpy.ops.mesh.primitive_cylinder_add(radius=0.04, depth=0.3, location=(0, 1.6, 1.5), rotation=(0, math.radians(90), 0))
    chinrest = bpy.context.active_object
    chinrest.name = "Chinrest"
    chinrest.data.materials.append(mat_chinrest)
    
    # 렌즈 (아이 눈높이)
    bpy.ops.mesh.primitive_cylinder_add(radius=0.08, depth=0.1, location=(0, 1.7, 1.75), rotation=(math.radians(90), 0, 0))
    lens = bpy.context.active_object
    lens.name = "Machine_Lens"
    lens.data.materials.append(create_material("LensMat", (0.1, 0.1, 0.15, 1.0)))

def create_coco_bear_blockout():
    """3D 곰돌이 코코 블록아웃 (머리, 몸통, 노란 스카프)"""
    mat_fur = create_material("CocoFurMat", (0.55, 0.35, 0.22, 1.0))
    mat_scarf = create_material("CocoScarfMat", (0.98, 0.82, 0.15, 1.0))
    
    # 의자
    bpy.ops.mesh.primitive_cylinder_add(radius=0.35, depth=0.5, location=(0, 0.8, 0.5))
    chair = bpy.context.active_object
    chair.name = "Coco_Chair"
    chair.data.materials.append(create_material("ChairMat", (0.3, 0.75, 0.65, 1.0)))
    
    # 몸통
    bpy.ops.mesh.primitive_uv_sphere_add(radius=0.35, location=(0, 0.8, 1.05))
    body = bpy.context.active_object
    body.name = "Coco_Body"
    body.scale = (1.0, 0.9, 1.1)
    body.data.materials.append(mat_fur)
    
    # 노란 스카프
    bpy.ops.mesh.primitive_torus_add(major_radius=0.25, minor_radius=0.06, location=(0, 0.8, 1.35))
    scarf = bpy.context.active_object
    scarf.name = "Coco_Scarf"
    scarf.data.materials.append(mat_scarf)
    
    # 머리
    bpy.ops.mesh.primitive_uv_sphere_add(radius=0.32, location=(0, 0.82, 1.62))
    head = bpy.context.active_object
    head.name = "Coco_Head"
    head.data.materials.append(mat_fur)
    
    # 귀 (좌/우)
    bpy.ops.mesh.primitive_uv_sphere_add(radius=0.1, location=(-0.22, 0.82, 1.9))
    ear_l = bpy.context.active_object
    ear_l.name = "Coco_Ear_L"
    ear_l.data.materials.append(mat_fur)
    
    bpy.ops.mesh.primitive_uv_sphere_add(radius=0.1, location=(0.22, 0.82, 1.9))
    ear_r = bpy.context.active_object
    ear_r.name = "Coco_Ear_R"
    ear_r.data.materials.append(mat_fur)

def setup_lighting_and_camera():
    """부드러운 스튜디오 조명 및 3인칭 시연 카메라 세팅"""
    # 조명 (따뜻한 키라이트 + 필라이트)
    bpy.ops.object.light_add(type='SUN', location=(3, -3, 6))
    sun = bpy.context.active_object
    sun.data.energy = 3.5
    sun.data.color = (1.0, 0.96, 0.9)
    
    bpy.ops.object.light_add(type='POINT', location=(-2, 0, 3))
    point = bpy.context.active_object
    point.data.energy = 80
    point.data.color = (0.9, 0.95, 1.0)
    
    # 3인칭 카메라 (Side-Quarter View)
    bpy.ops.object.camera_add(location=(2.2, -1.2, 2.0), rotation=(math.radians(72), 0, math.radians(45)))
    cam = bpy.context.active_object
    cam.name = "Previs_Camera_3rdPerson"
    cam.data.lens = 50
    bpy.context.scene.camera = cam

def main():
    clear_scene()
    setup_render_settings()
    create_eye_clinic_environment()
    create_autorefrac_machine()
    create_coco_bear_blockout()
    setup_lighting_and_camera()
    
    # .blend 파일 자동 저장
    import os
    save_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'assets', 'eyeclinic_previs_v01.blend'))
    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    bpy.ops.wm.save_as_mainfile(filepath=save_path)
    print(f"✅ CocoLink 소아 안과 3D 프리비즈가 성공적으로 생성 및 저장되었습니다: {save_path}")

if __name__ == "__main__":
    main()
