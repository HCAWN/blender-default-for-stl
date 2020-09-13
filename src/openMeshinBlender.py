import bpy
import sys
arguments = sys.argv
filename = arguments[4]
fileType = filename.split('.')[-1]
#clear scene
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete()
#import stl files
if fileType == 'stl':
    bpy.ops.import_mesh.stl(filepath = filename)
elif fileType == 'obj':
    bpy.ops.import_scene.obj(filepath = filename)
else:
    for i in range(10):
        print('------------ invalid file type ------------')