SET bdfspyfile=openMeshinBlender.py
SET bdfspydirectory=%~dp0
SET bdfspypath=%bdfspydirectory%%bdfspyfile%
echo %stlpypath%
cmd /c blender --python %bdfspypath% -- %*