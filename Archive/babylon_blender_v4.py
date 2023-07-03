import json
import bpy
import numpy as np
import mathutils
# from snap_def import *

def vertex(position):
    x=len(position)
    y=x/3
    position = np.array(position)
    position = position.reshape(int(y),3)
    return position
    
def index(indices):
    x = len(indices)
    y = x/3
    indices = np.array(indices)
    indices = indices.reshape(int(y),3)
    return indices

def uvs(uv):
    x = len(uv)
    y = x/2
    uv = np.array(uv)
    uv = uv.reshape(int(y),2)
    return uv

with open ('scene.babylon', 'r') as data:
    data = json.load(data)
    # print (scene)

# extract mesh from scene
mesh = data['meshes']
# print (mesh)

# extract lights from scene
lights = data['lights']
# print (lights)

# extract cameras from scene
camera = data['cameras']
print ('camera',camera)

# extract vertex data from scene for each mesh
vertexData = data['geometries']['vertexData']

# new scene
new_scene = bpy.data.scenes.new('new_scene')
bpy.context.window.scene = new_scene

# add to collection
collection = bpy.data.collections.new('collection')
bpy.context.scene.collection.children.link(collection)

for i in range(len(mesh)):
    geometryId = mesh[i]['geometryId']
    name = mesh[i]['name']
    vert = vertex(vertexData[i]['positions'])
    indices = index(vertexData[i]['indices'])
    # create mesh from vertex and indices
    mesh_data = bpy.data.meshes.new(name)
    mesh_data.from_pydata(vert,[],indices)
    mesh_data.update(calc_edges=True)
    # create object from mesh
    obj = bpy.data.objects.new(name,mesh_data)
    # move object from mesh data
    obj.location = (int(mesh[i]['position'][0]),int(mesh[i]['position'][1]),int(mesh[i]['position'][2]))
    # rotate object from mesh data
    obj.rotation_euler = (int(mesh[i]['rotation'][0]),int(mesh[i]['rotation'][1]),int(mesh[i]['rotation'][2]))
    # scale object from mesh data   
    obj.scale = (int(mesh[i]['scaling'][0]),int(mesh[i]['scaling'][1]),int(mesh[i]['scaling'][2]))
    # smoothen mesh
    for f in mesh_data.polygons:
        f.use_smooth = True
    # link object to scene collection
    collection.objects.link(obj)


# ----------------------------------------------------------------------------------------
# create camera from camera data
cam_data = bpy.data.cameras.new('camera')
cam = bpy.data.objects.new('camera',cam_data)
# check camera type
if camera[0]['type'] == 'FreeCamera':
    cam_data.type = 'PERSP'
elif camera[0]['type'] == 'ArcRotateCamera':
    cam_data.type = 'ORTHO'

# # camera properties
cam_data.lens = int(camera[0]['fov'])
cam_data.clip_start = int(camera[0]['minZ'])
cam_data.clip_end = int(camera[0]['maxZ'])
cam.location = (int(camera[0]['position'][0]),int(camera[0]['position'][1]),int(camera[0]['position'][2]))
# cam.rotation_euler = (0,int(camera[0]['beta']),int(camera[0]['alpha']))
# set upVector for camera
cam.up_axis = 'Y'
#create target object
target = bpy.data.objects.new('target',None)
target.location = (int(camera[0]['target'][0]),int(camera[0]['target'][1]),int(camera[0]['target'][2]))
# link target to scene collection
collection.objects.link(target)
# set track to constraint
track = cam.constraints.new('TRACK_TO')
track.target = target

# link camera to scene collection
collection.objects.link(cam)

# ----------------------------------------------------------------------------------------
# # # set light from light data
# light_data = bpy.data.lights.new('light',type='SUN')

# # light properties
# light_data.energy = lights[0]['intensity']
# # light color
# light_data.color = (int(lights[0]['diffuse'][0]),int(lights[0]['diffuse'][1]),int(lights[0]['diffuse'][2]))
# light_data.specular_factor = int(lights[0]['specular'][0])
# # enable shadow
# light_data.use_shadow = True

# # create new light object
# light = bpy.data.objects.new('light',light_data)



# # link light to scene collection
# collection.objects.link(light)



































































