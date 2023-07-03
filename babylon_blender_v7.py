import json
import bpy
import numpy as np
import mathutils


# functions to extract vertex position from vertexData
def vertex(position):
    x=len(position)
    y=x/3
    position = np.array(position)
    position = position.reshape(int(y),3)
    return position

# functions to extract vertex indices from vertexData
def index(indices):
    x = len(indices)
    y = x/3
    indices = np.array(indices)
    indices = indices.reshape(int(y),3)
    return indices

# functions to extract vertex uvs from vertexData
def uvs(uv):
    x = len(uv)
    y = x/2
    uv = np.array(uv)
    uv = uv.reshape(int(y),2)
    return uv

# functions to extract vertex normals from vertexData
def normal(normals):
    x = len(normals)
    y = x/3
    normals = np.array(normals)
    normals = normals.reshape(int(y),3)
    return normals

# main funcion to serialize babylon file in blender
def main(data):
    # extract mesh from scene
    mesh = data['meshes']
    print (mesh)

    # extract lights from scene
    lights = data['lights']
    # print (lights)

    # extract cameras from scene
    camera = data['cameras']
    # print ('camera',camera)

    # extract vertex data from scene for each mesh
    vertexData = data['geometries']['vertexData']

    # new scene
    new_scene = bpy.data.scenes.new('new_scene')
    bpy.context.window.scene = new_scene

    # add to collection
    collection = bpy.data.collections.new('collection')
    bpy.context.scene.collection.children.link(collection)

    # loop through every mesh and create an object in the scene
    for i in range(len(mesh)):
        geometryId = mesh[i]['geometryId']
        name = mesh[i]['name']
        vert = vertex(vertexData[i]['positions'])
        indices = index(vertexData[i]['indices'])
        normals = normal(vertexData[i]['normals'])
        # create mesh from vertex, indices, normals
        mesh_data = bpy.data.meshes.new(name)
        mesh_data.from_pydata(vert,[],indices)
        # flip normals
        mesh_data.flip_normals()
        mesh_data.update()
        # create object from mesh
        obj = bpy.data.objects.new(name,mesh_data)
        # move object from mesh data
        obj.location = ((mesh[i]['position'][0]),(mesh[i]['position'][1]),(mesh[i]['position'][2]))
        # rotate object from mesh data
        obj.rotation_euler = ((mesh[i]['rotation'][0]),(mesh[i]['rotation'][1]),(mesh[i]['rotation'][2]))
        # scale object from mesh data   
        obj.scale = ((mesh[i]['scaling'][0]),(mesh[i]['scaling'][1]),(mesh[i]['scaling'][2]))
        # smoothen mesh
        for f in mesh_data.polygons:
            f.use_smooth = True
        # link object to scene collection
        collection.objects.link(obj)


    # ------------------------create camera-----------------------------------

    # create camera from camera data
    cam_data = bpy.data.cameras.new('camera')
    cam = bpy.data.objects.new('camera',cam_data)
    cam_data.type = 'PERSP'

    # adding camera properties
    # convert fov from radians to degrees
    fov = camera[0]['fov']
    fov = fov * 57.2958

    # setting fov and clip
    cam_data.lens = fov
    cam_data.clip_start = camera[0]['minZ']
    cam_data.clip_end = camera[0]['maxZ']

    # setting camera location and rotation
    cam.location = ((camera[0]['position'][0]),(camera[0]['position'][1]),(camera[0]['position'][2]))
    cam.rotation_euler = (int(camera[0]['rotation'][0]),int(camera[0]['rotation'][1]),int(camera[0]['rotation'][2]))

    # add depth of field
    cam_data.dof.use_dof = True
    cam_data.dof.focus_distance = camera[0]['radius']

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

    # ---------------------------------create light----------------------------------------------

    # set light from light data

    # check light type and create light
    if lights[0]['type'] == 0:
        light_data = bpy.data.lights.new('light',type='POINT')
    elif lights[0]['type'] == 1:
        light_data = bpy.data.lights.new('light',type='SPOT')
    elif lights[0]['type'] == 2:
        light_data = bpy.data.lights.new('light',type='HEMI')
    elif lights[0]['type'] == 3:
        light_data = bpy.data.lights.new('light',type='SUN')

    # add light properties
    light_data.energy = lights[0]['intensity']

    # add light color
    light_data.color = (int(lights[0]['diffuse'][0]),int(lights[0]['diffuse'][1]),int(lights[0]['diffuse'][2]))
    light_data.specular_factor = int(lights[0]['specular'][0])

    # check if light has shadow
    if lights[0]['shadowEnabled'] == True:
        light_data.use_shadow = True
    else:
        light_data.use_shadow = False

    # create new light object
    light = bpy.data.objects.new('light',light_data)

    # link light to scene collection
    collection.objects.link(light)


# Load babylon file
with open ('scene.babylon', 'r') as data:
    data = json.load(data)
    
__name__ = '__main__'

if __name__ == '__main__':
    main(data)































































