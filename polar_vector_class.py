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
    def __init__(self,rad,theta,phi):

        #Unit Convertsion from Degrees to radians
        #(assumes no input > 2pi for radians and < 2pi for degree )
        if theta > abs(2*np.pi):
            np.deg2rad(theta)
        if phi > abs(2*np.pi):
            np.deg2rad(phi)

        v3d.__init__(self,
                   rad*np.sin(theta)*np.sin(phi),
                   rad*np.sin(theta)*np.cos(phi),
                   rad*np.cos(theta))

        eps = 1e-10 #error tolerence to turn very small numbers to 0
        self.xpos = 0 if abs(self.xpos) < eps else self.xpos
        self.ypos = 0 if abs(self.ypos) < eps else self.ypos
        self.zpos = 0 if abs(self.zpos) < eps else self.zpos

    def rad(self):
        "returns the radius from the vector magnitude"
        return self.magnitude()
    def phi(self):
        "returns phi using cartesian coordinates"
        return atan2(self.xpos,self.ypos)
    def theta(self):
        "return theta using cartesian coordinates"
        return np.arcsin(self.zpos/self.magnitude())

if __name__ == "__main__":

    test0 = PolarVector(1,np.pi/2,np.pi)
    print(f'Polar_coords return = {test0.rad(),test0.phi(),test0.theta()}')

    #values for test vector checks.
    rad_test = 2
    theta_test = np.pi
    phi_test = np.pi/2
    xpos_test = rad_test*np.cos(theta_test)*np.cos(phi_test)
    ypos_test =rad_test*np.cos(theta_test)*np.sin(phi_test)
    zpos_test = rad_test*np.sin(theta_test)
    #cartesian vector
    testv3d = v3d(xpos_test,ypos_test,zpos_test)
    #Polar vector
    test = PolarVector(rad_test,theta_test,phi_test)
    print(f' Polar = {test} \nCartesian ={testv3d}\n')
    print(f' Polar mag = {test.magnitude()} \nCartesian mag ={testv3d.magnitude()}\n')
    print(f' Polar + Polar = {test+test} \n + Cartesian  ={test + testv3d}\n')
    print(f' Polar - Polar = {test-test} \n - Cartesian sub ={testv3d - test}\n')
    print(f'polar.polar = {test.dot(test)} \n polar.cartesian = {test.dot(testv3d)}')
    print(f'polarXpolar = {test.cross(test)} \n polarXcartesian = {test.cross(testv3d)}')
