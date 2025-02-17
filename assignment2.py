# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 14:13:02 2025

@author: jackm
"""

import numpy as np


#creating a class for a vector (currently in arbitray/cartesian coords)
class vector:
    
    def __init__(self,x,y,z):
        
        self.x = x
        self.y = y
        self.z = z
        
    def __str__(self):
        return str([self.x,self.y,self.z])

    def magnitude(self):
        
        mag = np.sqrt(self.x**2)+np.sqrt(self.y**2)+np.sqrt(self.z**2)
        print(f"V = {mag}")
        return mag
    
    def __add__(self,other):
        return vector(self.x+other.x, self.y+other.y, self.z +other.z)
    
    def __sub__(self,other):
        return vector(self.x-other.x, self.y-other.y, self.z -other.z)
    
    def dot(self,other):
        return (self.x*other.x + self.y*other.y + self.z*other.z)
    
    def cross(self,other):
        x_new = (self.y*other.z)-(other.y*self.z)
        y_new = (self.z*other.x) - (other.z*self.x)
        z_new = (self.x*other.y) - (other.x*self.y)
        new_vector = [x_new,y_new, z_new]
        return new_vector


test = vector(1,2,3)
test2 = vector(4,6,8)


a = test.magnitude()
print(f'test = {test}')

b = test.__str__()
print(f'test2 = {test2}')

c = test+test2
print(f'test+test2 = {c}')

d = test-test2
print(f'test-test2 = {d}')

e = test.dot(test2)
print(f'test dot test2 = {e}')

f = test.cross(test2)
print(f'test dot test2 = {f}')



