# -*- coding: utf-8 -*-
"""
Created on Tue Jan  8 20:50:29 2019

@author: harpal
"""
"##################"
print("###############################") 
print("Single Inheritance")
print("###############################") 
class Apple:
    manufacture="Apple"
    contactWebsite="www.apple.com/contact"
    
    def contactDetails(self):
        print("To contact us,log on us",self.contactWebsite)
        
        
class Macbook(Apple):
    def __init__(self):
        self.yearOfManufacture=2017
        
    def manufacturedetails(self):
        print("This MackBook was manufacture in the year {} by {}".format(self.yearOfManufacture,self.manufacture))
        
macbook=Macbook()
macbook.manufacturedetails()
macbook.contactDetails()

print("###############################") 
print("Multiple Inheritance") 
print("###############################") 

class OperatingSystem:
    multitasking=True
    name= "Mac OS"
    
class Apple:
    website="www.apple.com"
    name= "Apple"
    
class Macbook(OperatingSystem,Apple):
    def __init__(self):
        if self.multitasking is True:
            print("this is multi tasking system .visit {} for details".format(self.website))
            print(self.name)
 
macbook=Macbook()    

print("###############################") 
print("Multilevel Inheritance") 
print("###############################") 

class MusicalInstuments:
    NumberofMajorKeys=12
    
class StringInstruments(MusicalInstuments):
    typeofwood="ToneWood"
    
class Guitar(StringInstruments):
    def __init__(self):
        self.numberofstring=6
        print("this Guiter constsis of {} made of {} and it play {}".format(self.numberofstring,self.typeofwood,self.NumberofMajorKeys))
    
guitar=Guitar()    
    
    
    
    
    
    
    
    
          
      
      
      