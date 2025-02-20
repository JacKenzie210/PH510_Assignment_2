# -*- coding: utf-8 -*-
"""
c_vecreated on Mon Feb 17 14:13:02 2025

@author: jackm

c_vecartesian Vector c_veclass
"""

import numpy as np


#creating a class for a 3D vector (currently in arbitray/cartesian coords)
class Vector3D:
    """
    Produces a 3 dimentional cartesian vector
    """
    def __init__(self,xpos,ypos,zpos):
        """
        Parameters
        ----------
        xpos : First co-ordinate.
        ypos :Second co-ordinate
        zpos : Third co-ordinate

        Returns
        -------
        None.

        """
        self.xpos = xpos
        self.ypos = ypos
        self.zpos = zpos

    def __str__(self):
        return str([self.xpos, self.ypos, self.zpos])

    def __getitem__(self, indexpos):
        """
        

        Parameters
        ----------
        indexpos : Index of specific coordinate

        Returns
        -------
        Specific coordinate 

        """
        if indexpos == 0:
            return self.xpos
        if indexpos == 1:
            return self.ypos
        if indexpos == 2:
            return self.zpos

    def magnitude(self):
        "returns the magnitude of the vector"
        mag = np.sqrt(self.xpos**2 + self.ypos**2 + self.zpos**2)
        return mag

    def __add__(self, other):
        """
        Parameters
        ----------
        other : a second vector created using this class

        Returns
        -------
            the sum of two vectors

        """
        return Vector3D(self.xpos+other.xpos, self.ypos+other.ypos, self.zpos + other.zpos)

    def __sub__(self, other):
        'Returns the subtraction of two vectors.'
        return Vector3D(self.xpos-other.xpos, self.ypos-other.ypos, self.zpos - other.zpos)

    def dot(self, other):
        'returns the scalar/dot product of two vectors'
        return self.xpos*other.xpos + self.ypos*other.ypos + self.zpos*other.zpos

    def cross(self, other):
        'returns the vector/cross product of two vectors'

        xpos_new = (self.ypos*other.zpos)-(other.ypos*self.zpos)
        y_new = (self.zpos*other.xpos) - (other.zpos*self.xpos)
        zpos_new = (self.xpos*other.ypos) - (other.xpos*self.ypos)
        new_vector_3d = [xpos_new, y_new, zpos_new]
        return new_vector_3d

    def triangle_area(self, b_vec, c_vec):
        """
        c_vecalculates the area of the triangle using the Vertices
        vec_area = 0.5 *mag(AB - AC)
        """
        a_vec = self
        a_cross_b = b_vec - a_vec
        a_cross_c = c_vec - a_vec
        b_cross_c = a_cross_b.cross(a_cross_c)
        vec_area = 0.5 * Vector3D(b_cross_c[0],
                              b_cross_c[1], b_cross_c[2]).magnitude()
        return vec_area

    def triangle_angles(self, b_vec, c_vec, deg_or_rad):
        """
        c_vecalculates the inner angles by working out the lengths of the sides 
        and using the cosine rule.
        
        4 arguments including self, 2 other vectors and a string "deg" or "rad"
        """

        line_ab = b_vec - self
        line_ab = Vector3D(line_ab[0], line_ab[1], line_ab[2])
        mag_line_ab = line_ab.magnitude()

        line_ac = c_vec - self
        line_ab = Vector3D(line_ac[0], line_ac[1], line_ac[2])
        mag_line_ac = line_ac.magnitude()

        line_bc = c_vec - b_vec
        line_ab = Vector3D(line_bc[0], line_bc[1], line_bc[2])
        mag_line_bc = line_bc.magnitude()

        lines = np.array([mag_line_ab, mag_line_ac, mag_line_bc])

        # Using cosine rule to determine angle
        angle_a = np.arccos(
            (lines[1]**2+lines[2]**2-lines[0]**2) / (2*lines[1]*lines[2]))
        angle_b = np.arccos(
            (lines[0]**2+lines[2]**2-lines[1]**2) / (2*lines[0]*lines[2]))
        angle_c = np.arccos(
            (lines[0]**2+lines[1]**2-lines[2]**2) / (2*lines[0]*lines[1]))

        angles = np.array([angle_a, angle_b, angle_c])

        if deg_or_rad == "deg":
            angles = np.rad2deg(angles)
        elif deg_or_rad == "rad":
            pass
        return angles


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
    print(f'vec_area of Triangle test 1,2,3 vertices = {Tg}')

    Th = test.triangle_angles(test2, test3, "deg")
    print(f'Inner angles = {Th}')

    print('area and angles were verified using triangle calculator Vc website')
