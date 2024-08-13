import bpy

bpy.ops.object.mode_set(mode='OBJECT')
tgt = bpy.context.active_object
bpy.ops.object.duplicate()
tgt = bpy.context.active_object
if tgt.type != 'MESH':
    bpy.ops.object.convert(target='MESH')

mod = tgt.modifiers.new(name='geo', type='NODES')
mod.node_group = bpy.data.node_groups['ConvexSplit']
bpy.ops.object.modifier_apply(modifier=mod.name)
bpy.ops.object.mode_set(mode='EDIT')
bpy.ops.mesh.separate(type='LOOSE')
bpy.ops.object.mode_set(mode='OBJECT')
# bpy.ops.object.delete()
