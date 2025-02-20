# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 11:07:10 2025

@author: jackm

Polar Vector Class
"""

from math import atan2
import numpy as np
from vector_3d_class import Vector3D as v3d

class PolarVector(v3d):
    """
    Sub class of Vector3D_Class which can take polar co-ordinate inputs and
    also allows conversion from polar to/from cartesian co-ordinates
    """
    def __init__(self,r,t,p):
        
        #Unit Convertsion from Degrees to radians
        #(assumes no input > 2pi for radians and < 2pi for degree )
        if t > abs(2*np.pi):
            np.deg2rad(t)
        if p > abs(2*np.pi):
            np.deg2rad(p)
        
        v3d.__init__(self,
                   r*np.sin(t)*np.sin(p),
                   r*np.sin(t)*np.cos(p),
                   r*np.cos(t))
        

        
        eps = 1e-10 #error tolerence to turn very small numbers to 0 
        self.x = 0 if abs(self.x) < eps else self.x
        self.y = 0 if abs(self.y) < eps else self.y
        self.z = 0 if abs(self.z) < eps else self.z
        
        
        
    def r(self):
        "returns the radius from the vector magnitude"
        return self.magnitude()
    def phi(self):
        "returns phi using cartesian coordinates"
        return atan2(self.x,self.y)
    def theta(self):
        "return theta using cartesian coordinates"
        return np.arcsin(self.z/self.magnitude())

if __name__ == "__main__":
    test0 = PolarVector(1,np.pi/2,np.pi)
    print(f'Polar_coords return = {test0.r(),test0.phi(),test0.theta()}')
    """
    Testing to ensure PolarVector behaves as intended
    """
    #values for test vector checks.
    r = 2
    t = np.pi
    p = np.pi/2
    x = r*np.cos(t)*np.cos(p)
    y =r*np.cos(t)*np.sin(p)
    z = r*np.sin(t)
    #cartesian vector
    testv3d = v3d(x,y,z)
    #Polar vector
    test = PolarVector(r,t,p)
    print(f' Polar = {test} \nCartesian ={testv3d}\n')
    print(f' Polar mag = {test.magnitude()} \nCartesian mag ={testv3d.magnitude()}\n')
    print(f' Polar + Polar = {test+test} \n + Cartesian  ={test + testv3d}\n')
    print(f' Polar - Polar = {test-test} \n - Cartesian sub ={testv3d - test}\n')
    print(f'polar.polar = {test.dot(test)} \n polar.cartesian = {test.dot(testv3d)}')
    print(f'polarXpolar = {test.cross(test)} \n polarXcartesian = {test.cross(testv3d)}')
    