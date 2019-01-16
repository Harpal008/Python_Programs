# -*- coding: utf-8 -*-
"""
Created on Tue Jan  8 21:21:39 2019

@author: harpal
"""

#Public =memberName
#protected=_memberName
#private=__memberName

class Car:
    numberofWheels=4
    _color="black"
    __yearOfManufacture=2010 #_Car__yearOfManufacture
    
class BMW(Car):
    def __init__(self):
        print("Protected attribute color",self._color)

car=Car()
print("Public Attributes numberofwheels:",car.numberofWheels)

bmw=BMW()  
print("year of manufacture",car._Car__yearOfManufacture)
