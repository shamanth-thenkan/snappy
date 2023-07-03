import json
import bpy
import numpy as np
import bmesh




with open ('scene.babylon', 'r') as data:
    data = json.load(data)
    # print (scene)

# extract mesh from scene
mesh = data['meshes']
# print (mesh)

# extract lights from scene
lights = data['lights']

# extract cameras from scene
cameras = data['cameras']

# extract vertex data from scene for each mesh
vertexData = data['geometries']['vertexData']
# print (vertexData)

# read geometry id in mesh[1]
geometryId = mesh[1]['geometryId']
name = mesh[1]['name']
# print (geometryId)


# one function to extract data from vertexData
# search for geometryId in vertexData
for i in range(len(vertexData)):
    if vertexData[i]['id'] == geometryId:
        # print (vertexData[i])
        # extract position data from vertexData
        positions = vertexData[i]['positions']
        # print ('Positions',positions)
        # extract indices data from vertexData
        indices = vertexData[i]['indices']
        # print ('Index',indices)
        # extract normals data from vertexData
        normals = vertexData[i]['normals']
        # print ('Normal',normals)
        # extract uvs data from vertexData
        uvs = vertexData[i]['uvs']
        # print ('UV',uvs)

# second function to create arrays from data
# create a numpy array of positions 3xy
x = len(positions)
y = x/3
x1 = len(indices)
y1 = x1/3
positions = np.array(positions)
positions = positions.reshape(int(y),3)
print (positions)
normals = np.array(normals)
normals = normals.reshape(int(y),3)
print (normals)
uvs = np.array(uvs)
uvs = uvs.reshape(int(y),2)
print (uvs)
indices = np.array(indices)
indices = indices.reshape(int(y1),3)
print (indices)

# new scene
new_scene = bpy.data.scenes.new('new_scene')
bpy.context.window.scene = new_scene
bpy.context.window.scene = new_scene

# add to collection
collection = bpy.data.collections.new('collection')
bpy.context.scene.collection.children.link(collection)



# fourth function to create mesh from data
# create mesh and mesh face from data
mesh_data = bpy.data.meshes.new(name)
# create object
raw_obj = bpy.data.objects.new(name, mesh_data)
# add object to scene collection
collection.objects.link(raw_obj)

# create mesh from data
mesh_data.from_pydata(positions,[],indices)
mesh_obj = bpy.data.objects.new(name, mesh_data)







































