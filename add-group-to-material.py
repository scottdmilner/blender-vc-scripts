import bpy

sel_objs = [obj for obj in bpy.context.selected_objects if obj.type == 'MESH']
bpy.ops.object.select_all(action='DESELECT')

groupname = "UV Crop"

for obj in sel_objs:
    mat = obj.active_material
    group = mat.node_tree.nodes.new("ShaderNodeGroup")
    group.node_tree = bpy.data.node_groups[groupname]
    
    image = mat.node_tree.nodes.get("Image Texture")
    
    mat.node_tree.links.new(image.inputs[0], group.outputs[0])
