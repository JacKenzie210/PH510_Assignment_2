# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 12:52:33 2025

@author: jackm

Applying the Cartesian Class to calculate Areas of triangle
"""
import numpy as np
from vector_3d_class import Vector3D as v3d
from polar_vector_class import PolarVector as pol

###########################################################
#triangles A-D Vertices Cartesian co-ordinates (x,y,z)
###########################################################

#Triangle A vertices
VertA = v3d(0,0,0) , v3d(1,0,0), v3d(0,1,0)
AreaTA =v3d.TriangleArea(VertA[0], VertA[1], VertA[2])
print(f'Area of Triangle A = {AreaTA}')

#Triangle B vertices
VertB = v3d(-1,-1,-1) , v3d(0,-1,-1), v3d(0,1,0)
AreaTB =v3d.TriangleArea(VertB[0], VertB[1], VertB[2])
print(f'Area of Triangle B = {AreaTB}')

#Triangle C vertices
VertC = v3d(1,0,0) , v3d(0,0,1), v3d(0,0,0)
AreaTC =v3d.TriangleArea(VertC[0], VertC[1], VertC[2])
print(f'Area of Triangle C = {AreaTC}')

#Triangle D vertices
VertD = v3d(0,0,0) , v3d(1,-1,0), v3d(0,0,1)
AreaTD =v3d.TriangleArea(VertD[0], VertD[1], VertD[2])
print(f'Area of Triangle D = {AreaTD}')



###########################################################
#triangles 1-4 Vertices Polar co-ordinates (r, theta, phi)
###########################################################

#Triangle 1 vertices
Vert1 = pol(0,0,0) , pol(1,0,0), pol(1,np.pi/2, 0)
AreaT1 =v3d.TriangleArea(Vert1[0], Vert1[1], Vert1[2])
print(f'Area of Triangle 1 = {AreaT1}')


#Triangle 2 vertices
Vert2 = pol(1,0,0) , pol(1,np.pi/2,0), pol(1,np.pi/2,np.pi)
AreaT2 =pol.TriangleArea(Vert2[0], Vert2[1], Vert2[2])
print(f'Area of Triangle 2 = {AreaT2}')

#Triangle 3 vertices
Vert3 = pol(0,0,0) , pol(2,0,0), pol(2,np.pi/2,0)
AreaT3 =pol.TriangleArea(Vert3[0], Vert3[1], Vert3[2])
print(f'Area of Triangle 3 = {AreaT3}')

#Triangle 4 vertices
Vert4 = pol(1,np.pi/2,0) , pol(1,np.pi/2,np.pi), pol(1,np.pi/2,3*np.pi/2)
AreaT4 =pol.TriangleArea(Vert4[0], Vert4[1], Vert4[2])
print(f'Area of Triangle 4 = {AreaT4}')
print(Vert4[0], Vert4[1],Vert4[2])

print(pol(1,np.pi/2,0))