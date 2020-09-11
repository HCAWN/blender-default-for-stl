SET stlpyfile=openSTLinBlender.py
SET stlpydirectory=%~dp0
SET stlpypath=%stlpydirectory%%stlpyfile%
echo %stlpypath%
cmd /c blender --python %stlpypath% -- %*