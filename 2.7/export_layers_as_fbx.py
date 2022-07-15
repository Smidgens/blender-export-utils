# ==========================================
# https://github.com/Smidgens
# ==========================================

import bpy
import os
import shutil
import sys
from contextlib import contextmanager

# Export layers
layer_selection = [0, 1, 2, 3, 4, 10, 11, 12, 13, 14]

# active layers
active_layers = [
	1, 1, 1, 1, 1,
	0, 0, 0, 0, 0,
	1, 1, 1, 1, 1,
	0, 0, 0, 0, 0,
]

def main():
	fileName = bpy.path.basename(bpy.context.blend_data.filepath)
	fileName = fileName.split(".")[0]
	print(str.format("Exporting '{0}.blend'", fileName))
	with suppress_output():
		run_export(fileName)
		return True

# anti-spam
@contextmanager
def suppress_output():
	with open(os.devnull, "w") as devnull:
		old_stdout = sys.stdout
		sys.stdout = devnull
		try:
			yield
		finally:
			sys.stdout = old_stdout

# name: file path
def run_export(name):
	
	# deselect all
	bpy.ops.object.mode_set(mode='OBJECT', toggle=True)
	bpy.ops.object.select_all(action='DESELECT')

	# clear selection and export
	for num in range(0, 20):
		# activate layers
		bpy.context.scene.layers[num] = active_layers[num]
		if(active_layers[num]):	
			bpy.ops.object.select_by_layer(extend=True, layers=num+1)

	# Export file
	bpy.ops.export_scene.fbx(
		filepath=str.format("{0}.fbx", name),
		use_selection=True,
		global_scale=1,
		apply_unit_scale=False
	)

main()