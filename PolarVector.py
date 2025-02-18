# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 11:07:10 2025

@author: jackm
"""

from Vector3D_Class import Vector3D as v3d
import numpy as np
from math import atan2

class PolarVector(v3d):
    def __init__(self,r,t,p):
        v3d.__init__(self,
                   r*np.cos(t)*np.cos(p),
                   r*np.cos(t)*np.sin(p),
                   r*np.sin(t))
    def r(self):
        return self.magnitude()
    def phi(self):
        return atan2(self.x,self.y)
    def theta(self):
        return np.arcsin(self.z/self.magnitude())

if __name__ == "__main__":
    """
    Testing the polar cordinate returns
    """
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
    