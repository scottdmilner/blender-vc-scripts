import bpy

#create a parent empty for all selected objects and add the empty to a collection
sel_objs = [obj for obj in bpy.context.selected_objects if obj.type == 'MESH']
bpy.ops.object.select_all(action='DESELECT')

#the name of the group
groupname = "choir"

try:
    bpy.data.collections[groupname]
except:
    c = bpy.data.collections.new(groupname)
    bpy.context.scene.collection.children.link(c)
try:
    bpy.data.collections[groupname + "_planes"]
except:
    cc = bpy.data.collections.new(groupname + "_planes")
    bpy.data.collections[groupname].children.link(cc)

for obj in sel_objs:
    emp = bpy.data.objects.new("P " + obj.name, None)
    emp.location = obj.location
    bpy.context.scene.collection.objects.link(emp)
    obj.parent = emp
    obj.location = [0,0,0]
    bpy.data.collections[groupname].objects.link(emp)
    bpy.data.collections[groupname + "_planes"].objects.link(obj)
    if not obj.data.vertex_colors:
        obj.data.vertex_colors.new()
