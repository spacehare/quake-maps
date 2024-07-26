'''
jitspoe: https://www.youtube.com/watch?v=b5taIvtQOXQ
- 5:10 for tiling textures
'''

import bpy
from pathlib import Path

cam = bpy.context.scene.camera


def init(camera, x: int, y: int):
    camera.data.type = 'ORTHO'
    bpy.context.scene.render.filter_size = 0.5


def render(output_path: Path | str, x: int, y: int):
    bpy.context.scene.render.resolution_x = x
    bpy.context.scene.render.resolution_y = y
    cam.data.ortho_scale = max(x, y)
    bpy.context.scene.render.filepath = str(output_path)
    bpy.ops.render.render(write_still=True)
