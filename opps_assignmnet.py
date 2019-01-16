# -*- coding: utf-8 -*-
"""
Created on Mon Dec 24 06:23:43 2018

@author: harpal
"""

class Cylinder(object):
    pi=3.14
    def __init__(self,height=1,radius=1):
        self.height=height
        self.radius=radius
        
    def volume(self):
        return float((self.radius**2)*(self.height)*3.14)
    
    def surface_area(self):
        top=(self.radius*self.height)*3.14*2
        return float (top+((self.radius)**2)*(2*3.14))

c=Cylinder(2,3)
print(c.volume())
print(c.surface_area()) 