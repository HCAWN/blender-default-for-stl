import bpy
import sys
arguments = sys.argv
print(arguments)
filename = arguments[4]
#clear scene
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete()
#import stl files
bpy.ops.import_mesh.stl(filepath = filename)