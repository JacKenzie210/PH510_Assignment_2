# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 14:13:02 2025

@author: jackm

Cartesian Vector Class
"""

import numpy as np


#creating a class for a 3D vector (currently in arbitray/cartesian coords)
class Vector3D:
    """
    Produces a 3 dimentional cartesian vector
    """
    def __init__(self,x,y,z):
        """
        Parameters
        ----------
        x : First co-ordinate.
        y :Second co-ordinate
        z : Third co-ordinate

        Returns
        -------
        None.

        """
        self.x = x
        self.y = y
        self.z = z
    def __str__(self):
        return str([self.x,self.y,self.z])

    def magnitude(self):
        "returns the magnitude of the vector"
        mag = np.sqrt(self.x**2 +self.y**2 + self.z**2)
        #print(f"V magnitude = {mag}")
        return mag
    def __add__(self,other):
        """
        Parameters
        ----------
        other : A second vector created using this class

        Returns
        -------
            the sum of two vectors

        """
        return Vector3D(self.x+other.x, self.y+other.y, self.z +other.z)
    def __sub__(self,other):
        'Returns the subtraction of two vectors.'
        return Vector3D(self.x-other.x, self.y-other.y, self.z -other.z)
    def dot(self,other):
        'returns the scalar/dot product of two vectors'
        return self.x*other.x + self.y*other.y + self.z*other.z
    def cross(self,other):
        'returns the vector/cross product of two vectors'
        x_new = (self.y*other.z)-(other.y*self.z)
        y_new = (self.z*other.x) - (other.z*self.x)
        z_new = (self.x*other.y) - (other.x*self.y)
        new_vector_3d = [x_new,y_new, z_new]
        return new_vector_3d
    def TriangleArea(self,B, C):
        """
        Calculates the area of the triangle using the Vertices
        Area = 0.5 *mag(AB x AC)
        """
        A = self
        AB = B - A #note this is B - A but due to how __sub__ does self- other,
        AC = C - A #the order needs flipped
        ABxAC = AB.cross(AC)
        Area = 0.5 * Vector3D(ABxAC[0],ABxAC[1],ABxAC[2]).magnitude()

        return Area
if __name__ == "__main__":
    V1 = 1,2,3
    test = Vector3D(V1[0],V1[1], V1[2])
    V2 = 4,6,8
    test2 = Vector3D(V2[0],V2[1],V2[2])
    V3 = 9,8,7
    test3 = Vector3D(V3[0],V3[1],V3[2])

    Ta = test.magnitude()
    print(f'test = {test}')

    Tb = test.__str__()
    print(f'test2 = {test2}')

    Tc = test+test2
    print(f'test+test2 = {Tc}')

    Td = test-test2
    print(f'test-test2 = {Td}')

    Te = test.dot(test2)
    print(f'test dot test2 = {Te}, numpy = {np.dot(V1,V2)}')

    Tf = test.cross(test2)
    print(f'test dot test2 = {Tf}, numpy = {np.cross(V1,V2)}')

    Tg = test.TriangleArea(test2,test3)
    print(f'Area of Triangle test = {Tg}, verified using triangle calculator VC website')
