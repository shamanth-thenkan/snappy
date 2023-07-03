import json
import bpy
import numpy as np

with open ('scene.babylon', 'r') as scene:
    scene = json.load(scene)
    # print (scene)

# extract mesh from scene
mesh = scene['meshes']

# extract lights from scene
lights = scene['lights']

# extract cameras from scene
cameras = scene['cameras']

# print (mesh[0])

# code to check for sphere in mesh and create a sphere in blender
for i in range(len(mesh)):
    if mesh[i]['name']=='sphere':
        print ('---------------',mesh[i])
        # Create a new mesh object
        bpy.ops.mesh.primitive_uv_sphere_add(radius=1, location=(int(mesh[i]['position'][0]), int(mesh[i]['position'][1]), int(mesh[i]['position'][2])))
        # activate the sphere
        bpy.context.active_object.name = 'sphere'
        # Get a reference to the created object
        obj = bpy.context.object


        # Set the object's name and unique ID
        obj.name = "sphere"
        obj["uniqueId"] = 26

        # Set the object's position
        obj.location = (0, 1, 0)

        # Set the object's rotation
        obj.rotation_euler = (0, 0, 0)

        # Set the object's scaling
        obj.scale = (1, 1, 1)

        # Set the object's visibility
        obj.hide_render = not True

        # Set the object's material
        material = bpy.data.materials.get("default material")
        if material is not None:
            obj.data.materials.append(material)

    
    if mesh[i]['name']=='box':
        print ('---------------',mesh[i])
        

    # if mesh[i]['name']=='ground':
        # print ('---------------',mesh[i])

        # # Create a new mesh object
        # plane_obj = bpy.data.objects.new('plane', bpy.data.meshes.new('plane_mesh'))

        # # Link the mesh object to the scene
        # scene = bpy.context.scene
        # scene.collection.objects.link(plane_obj)

        # # Set the object's properties   
        # plane_obj.name = 'ground'
        # plane_obj.location = (0, 0, 0)

        # # Create the plane mesh
        # plane_mesh = plane_obj.data

        # # Set the plane's dimensions
        # width = 6
        # height = 6
        # bpy.ops.mesh.primitive_plane_add(size=1, enter_editmode=False, align='WORLD')
        # # scale the plane
        # bpy.ops.transform.resize(value=(width, height, 1))

        # # Set other properties
        # plane_mesh.name = 'ground'
        # plane_mesh['uniqueId'] = 28
        # plane_mesh['type'] = 'GroundMesh'
        # plane_mesh['position'] = [0, 0, 0]
        # plane_mesh['rotation'] = [0, 0, 0]
        # plane_mesh['scaling'] = [1, 1, 1]
        # plane_mesh['localMatrix'] = {'0': 1, '1': 0, '2': 0, '3': 0, '4': 0, '5': 1, '6': 0, '7': 0, '8': 0, '9': 0, '10': 1, '11': 0, '12': 0, '13': 0, '14': 0, '15': 1}
        # plane_mesh['isEnabled'] = True
        # plane_mesh['isVisible'] = True
        # plane_mesh['infiniteDistance'] = False
        # plane_mesh['pickable'] = True
        # plane_mesh['receiveShadows'] = False
        # plane_mesh['billboardMode'] = 0
        # plane_mesh['visibility'] = 1
        # plane_mesh['checkCollisions'] = False
        # plane_mesh['isBlocker'] = False
        # plane_mesh['overrideMaterialSideOrientation'] = None
        # plane_mesh['isUnIndexed'] = False
        # plane_mesh['geometryUniqueId'] = 29
        # plane_mesh['geometryId'] = '8a55deda-7969-44b7-ac33-5b7b419f6115'
        # plane_mesh['subMeshes'] = [{'materialIndex': 0, 'verticesStart': 0, 'verticesCount': 4, 'indexStart': 0, 'indexCount': 6}]
        # plane_mesh['materialUniqueId'] = 32
        # plane_mesh['materialId'] = 'default material'
        # plane_mesh['instances'] = []
        # plane_mesh['animations'] = []
        # plane_mesh['ranges'] = []
        # plane_mesh['layerMask'] = 268435455
        # plane_mesh['alphaIndex'] = 1.7976931348623157e+308
        # plane_mesh['hasVertexAlpha'] = False
        # plane_mesh['overlayAlpha'] = 0.5
        # plane_mesh['overlayColor'] = [1, 0, 0]
        # plane_mesh['applyFog'] = True
        # plane_mesh['subdivisionsX'] = 1
        # plane_mesh['subdivisionsY'] = 1
        # plane_mesh['minX'] = -3
        # plane_mesh['maxX'] = 3
        # plane_mesh['minZ'] = -3
        # plane_mesh['maxZ'] = 3
        # plane_mesh['width'] = 6
        # plane_mesh['height'] = 6




















