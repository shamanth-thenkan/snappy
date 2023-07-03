import json
import bpy
import numpy as np
import bmesh

with open ('scene.babylon', 'r') as scene:
    scene = json.load(scene)
    # print (scene)

# extract mesh from scene
mesh = scene['meshes']
# print (mesh)

# extract lights from scene
lights = scene['lights']

# extract cameras from scene
cameras = scene['cameras']

# print (mesh[0])

# code to check for sphere in mesh and create a sphere in blender
for i in range(len(mesh)):
    if mesh[i]['name']=='sphere':
        print ('sphere',mesh[i])       
        # create a uv sphere
        bpy.ops.mesh.primitive_uv_sphere_add(radius=1, location=(int(mesh[i]['position'][0]), int(mesh[i]['position'][1]), int(mesh[i]['position'][2])))
        obj_sphere = bpy.context.object
        obj_sphere.name = mesh[i]['name']
        obj_sphere.scale = (mesh[i]['scaling'][0], mesh[i]['scaling'][1], mesh[i]['scaling'][2])
        obj_sphere.rotation_euler = (mesh[i]['rotation'][0], mesh[i]['rotation'][1], mesh[i]['rotation'][2])
        obj_sphere.location = (mesh[i]['position'][0], mesh[i]['position'][1], mesh[i]['position'][2])
        bpy.ops.object.shade_smooth()

    # if mesh[i]['name']=='box':
    #     print ('box',mesh[i])
    #     # create a cube
    #     bpy.ops.mesh.primitive_cube_add(size=2, location=(int(mesh[i]['position'][0]), int(mesh[i]['position'][1]), int(mesh[i]['position'][2])))
    #     obj_cube = bpy.context.object
    #     obj_cube.name = mesh[i]['name']
    #     obj_cube.scale = (mesh[i]['scaling'][0], mesh[i]['scaling'][1], mesh[i]['scaling'][2])
    #     obj_cube.rotation_euler = (mesh[i]['rotation'][0], mesh[i]['rotation'][1], mesh[i]['rotation'][2])
    #     obj_cube.location = (mesh[i]['position'][0], mesh[i]['position'][1], mesh[i]['position'][2])

    # if mesh[i]['name']=='ground':
    #     print ('ground',mesh[i])
    #     # create a plane
    #     bpy.ops.mesh.primitive_plane_add(size=2, location=(int(mesh[i]['position'][0]), int(mesh[i]['position'][1]), int(mesh[i]['position'][2])))
    #     obj_plane = bpy.context.object
    #     obj_plane.name = mesh[i]['name']
    #     obj_plane.scale = (mesh[i]['scaling'][0], mesh[i]['scaling'][1], mesh[i]['scaling'][2])
    #     obj_plane.rotation_euler = (mesh[i]['rotation'][0], mesh[i]['rotation'][1], mesh[i]['rotation'][2])
    #     obj_plane.location = (mesh[i]['position'][0], mesh[i]['position'][1], mesh[i]['position'][2])

# # create camera from scene
for i in range(len(cameras)):
    if cameras[i]['name']=='camera':
        print ('camera',cameras[i])
       
        # get camera type
        camera_type = cameras[i]['type']
        if camera_type == 'ArcRotateCamera':
            # create new empty camera
            bpy.ops.object.camera_add()
            obj_camera = bpy.context.object
            obj_camera.name = cameras[i]['name']
            # add camera location
            obj_camera.location = (cameras[i]['position'][0], cameras[i]['position'][1], cameras[i]['position'][2])
            # add camera rotation
            obj_camera.rotation_euler = (cameras[i]['rotation'][0], cameras[i]['rotation'][1], cameras[i]['rotation'][2])
            # add camera lens
            bpy.data.cameras[obj_camera.name].lens = cameras[i]['fov']

            # create track to constraint
            bpy.ops.object.constraint_add(type='TRACK_TO')
            # set track to constraint properties to target camera
            bpy.context.object.constraints["Track To"].target = bpy.data.objects[cameras[i]['target']]
            # set track to constraint properties to track axis
            bpy.context.object.constraints["Track To"].track_axis = 'TRACK_NEGATIVE_Z'
            # set track to constraint properties to up axis
            bpy.context.object.constraints["Track To"].up_axis = 'UP_Y'
            









        






















