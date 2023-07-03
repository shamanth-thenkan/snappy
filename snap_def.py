import bpy
import json
import mathutils
import numpy as np



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