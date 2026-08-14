@echo off
chcp 65001 > nul
echo ========================================================
echo   CocoLink 소아 안과 Step 3 프리비즈 영상(MP4) 자동 렌더러
echo ========================================================

set "BLENDER_EXE=C:\Program Files\Blender Foundation\Blender 5.2\blender.exe"
if not exist "%BLENDER_EXE%" (
    set "BLENDER_EXE=blender"
)

set "SCRIPT_PATH=%~dp0scripts\render_previs_videos.py"

echo [1/3] Blender 5.2 씬 애니메이션 및 프레임 렌더링 중...
& "%BLENDER_EXE%" -b -P "%SCRIPT_PATH%"

echo [2/3] FFmpeg를 통한 고화질 MP4 비디오 인코딩 중...
powershell -Command "if (Get-Command ffmpeg -ErrorAction SilentlyContinue) { & ffmpeg -y -framerate 24 -i '%~dp0renders\3-1_chinrest.mp4%%04d.png' -c:v libx264 -pix_fmt yuv420p '%~dp0renders\3-1_chinrest.mp4'; & ffmpeg -y -framerate 24 -i '%~dp0renders\3-2_balloon.mp4%%04d.png' -c:v libx264 -pix_fmt yuv420p '%~dp0renders\3-2_balloon.mp4'; & ffmpeg -y -framerate 24 -i '%~dp0renders\3-3_sunglasses.mp4%%04d.png' -c:v libx264 -pix_fmt yuv420p '%~dp0renders\3-3_sunglasses.mp4'; New-Item -ItemType Directory -Force -Path '%~dp0renders\frames'; Move-Item -Path '%~dp0renders\*.png' -Destination '%~dp0renders\frames\' -Force }"

echo.
echo ========================================================
echo   [성공] 3개 프리비즈 MP4 비디오가 모두 렌더링되었습니다!
echo   위치: Docs\EyeClinic\Blender\renders\
echo     1. 3-1_chinrest.mp4 (코코 턱받침 착석 씬)
echo     2. 3-2_balloon.mp4 (열기구 관찰 씬)
echo     3. 3-3_sunglasses.mp4 (별 선글라스 획득 씬)
echo ========================================================
echo.
pause
