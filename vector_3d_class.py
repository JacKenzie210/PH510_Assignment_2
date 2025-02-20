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
    def __getitem__(self, index):
        if index == 0:
            return self.x
        elif index == 1:
            return self.y
        elif index == 2:
            return self.z
        else:
            raise Exception('Only 3 DImentional i.e max index = 2 ')
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

    def triangle_area(self,B, C):
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

    def triangle_angles(self,B,C, deg_or_rad):
        """
        Calculates the inner angles by working out the lengths of the sides 
        and using the cosine rule.
        
        4 arguments including self, 2 other vectors and a string "deg" or "rad"
        """
        A = self
        LineAB = B - A
        LineAB = Vector3D(LineAB[0],LineAB[1], LineAB[2])
        MagLineAB = LineAB.magnitude()

        LineAC = C - A
        LineAB = Vector3D(LineAC[0],LineAC[1], LineAC[2])
        MagLineAC = LineAC.magnitude()
        
        LineBC = C - B
        LineAB = Vector3D(LineBC[0],LineBC[1], LineBC[2])
        MagLineBC = LineBC.magnitude()

        Lines = np.array([MagLineAB,MagLineAC,MagLineBC])

        #Using cosine rule to determine angle
        AngleA = np.arccos( (Lines[1]**2+Lines[2]**2-Lines[0]**2) / (2*Lines[1]*Lines[2]) )
        AngleB = np.arccos( (Lines[0]**2+Lines[2]**2-Lines[1]**2) / (2*Lines[0]*Lines[2]) )     
        AngleC = np.arccos( (Lines[0]**2+Lines[1]**2-Lines[2]**2 ) / (2*Lines[0]*Lines[1]) )

        Angles = np.array([AngleA, AngleB, AngleC])

        if deg_or_rad == "deg":
            Angles = np.rad2deg(Angles)
        elif deg_or_rad == "rad":
            pass
        else:
            raise Exception('use "dag" or "rad"')
        return Angles

    
if __name__ == "__main__":
    V1 = 1,2,3
    test = Vector3D(V1[0],V1[1], V1[2])
    V2 = 4,6,8
    test2 = Vector3D(V2[0],V2[1],V2[2])
    V3 = 9,8,7
    test3 = Vector3D(V3[0],V3[1],V3[2])

    Ta = test.magnitude()
    print(f'test = {test}')

    # Tb = test.__str__()
    # print(f'test2 = {test2}')

    Tc = test+test2
    print(f'test+test2 = {Tc}')

    Td = test-test2
    print(f'test-test2 = {Td}')

    Te = test.dot(test2)
    print(f'test dot test2 = {Te}, numpy = {np.dot(V1,V2)}')

    Tf = test.cross(test2)
    print(f'test dot test2 = {Tf}, numpy = {np.cross(V1,V2)}')

    Tg = test.triangle_area(test2,test3)
    print(f'Area of Triangle test 1,2,3 vertices = {Tg}, verified using triangle calculator VC website')

    Th = test.triangle_angles(test2, test3, "deg")
    print(f'Inner angles = {Th}, verified using triangle calculator VC website')
