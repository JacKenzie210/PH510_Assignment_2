# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 14:13:02 2025

@author: jackm
"""

import numpy as np


#creating a class for a 3D vector (currently in arbitray/cartesian coords)
class vector3D:
    
    
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
        mag = np.sqrt(self.x**2)+np.sqrt(self.y**2)+np.sqrt(self.z**2)
        print(f"V = {mag}")
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
        return vector3D(self.x+other.x, self.y+other.y, self.z +other.z)
    
    def __sub__(self,other):
        'Returns the subtraction of two vectors.'
        return vector3D(self.x-other.x, self.y-other.y, self.z -other.z)
    
    def dot(self,other):
        'returns the scalar/dot product of two vectors'
        return (self.x*other.x + self.y*other.y + self.z*other.z)
    
    def cross(self,other):
        'returns the vector/cross product of two vectors'
        x_new = (self.y*other.z)-(other.y*self.z)
        y_new = (self.z*other.x) - (other.z*self.x)
        z_new = (self.x*other.y) - (other.x*self.y)
        new_vector3D = [x_new,y_new, z_new]
        return new_vector3D



if __name__ == "__main__":
        
    V1 = 1,2,3
    test = vector3D(V1[0],V1[1], V1[2])
    V2 = 4,6,8
    test2 = vector3D(V2[0],V2[1],V2[2])
    
    
    a = test.magnitude()
    print(f'test = {test}')
    
    b = test.__str__()
    print(f'test2 = {test2}')
    
    c = test+test2
    print(f'test+test2 = {c}')
    
    d = test-test2
    print(f'test-test2 = {d}')
    
    e = test.dot(test2)
    print(f'test dot test2 = {e}, numpy = {np.dot(V1,V2)}')
    
    f = test.cross(test2)
    print(f'test dot test2 = {f}, numpy = {np.cross(V1,V2)}')
    
    
    
