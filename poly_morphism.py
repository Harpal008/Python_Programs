# -*- coding: utf-8 -*-
"""
Created on Tue Jan  8 21:32:41 2019

@author: harpal
"""

class Employee:
    def setNumberOfWorkinghours(self):
        self.numberofworkinghours=40
        
    def displayNumberOfWorkingHours(self):
        print(self.numberofworkinghours)
        
 
class Trainee(Employee):
    def setNumberOfWorkinghours(self):
        self.numberofworkinghours=45    
      
    def resetNumberOfWorkingHours(self):
        super().setNumberOfWorkinghours()
       
employee=Employee()
employee.setNumberOfWorkinghours()
print("Number of working hours of employee :", end= ' ' )
employee.displayNumberOfWorkingHours()

trainee=Trainee()
trainee.setNumberOfWorkinghours()
print("Number of working hours of trainee :", end= ' ' )
trainee.displayNumberOfWorkingHours()
trainee.resetNumberOfWorkingHours()
print("Reset Number of working hours of trainee :", end= ' ' )
trainee.displayNumberOfWorkingHours()