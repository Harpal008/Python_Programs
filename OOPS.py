# -*- coding: utf-8 -*-
"""
Created on Sun Dec 23 07:49:21 2018

@author: harpal
"""
l=[1,2,3]
print(l.count(2))
  
class Sample(object):
    pass
x=Sample()
print(type(x))


class Dog(object):
    #Class Object Attribute
    species='mammal'
    
    def __init__(self,breed,name):
        self.breed=breed
        self.name=name
                
sam=Dog(breed='Lab',name='sammy')
print(sam)
print(sam.breed,sam.name,sam.species)


class Circle(object):
    #class object Attribues 
    pi=3.14
    
    def __init__(self,radius=1):
        self.radius=radius
    
    def area(self):
      return (self.radius**2)*Circle.pi
  
    def set_radius(self,new_radius):
        self.radius=new_radius
    
    def get_radius(self):
        return self.radius
    
    def perimeter(self):
        return (2*Circle.pi*self.radius)
    
    
    
c=Circle(radius=10)
print(c.radius)
print("Area",c.area())
print(c.get_radius())
c.set_radius(200)
print("New Radius",c.get_radius())
print("Perimeter",c.perimeter())

print("***************************")
c.set_radius(20)
print(c.radius)
print("Area",c.area())
print(c.get_radius())
print(c.perimeter())
print("***************************")

c=Circle(radius=100)
print(c.radius)
print(c.pi)    
print("Area",c.area())
print("******INHERITANCE *********************")

class Animal(object):
    def __init__(self):
        print("Animal Created")
    
    def whoAmI(self):
        print("Animal")
        
    def eat(self):
        print("Eating")
        
class Dog(Animal):
    def __init__(self):
        Animal.__init__(self)
        print("Dog created")
    def whoAmI(self):
        print("Dog")
    def bark(self):
        print("woof")
        
 
d=Dog()
d.whoAmI()
d.eat()
d.bark()

print("******special Objects*********************")

class Book(object):
    def __init__(self,title,author,pages):
        print("A book has been created !")
        self.title=title
        self.author=author
        self.pages=pages
        
    def __str__(self):
        return "Title :%s,Author :%s,Pages :%d"%(self.title,self.author,self.pages)
      
b=Book('Python' ,'Harpal',100) 
print(b)

print("**************************************************")

'''Fill in the Line class methods to accept coordinate as a pair of tuples and return the slope and distance of the line.'''


class Line(object):
    
    def __init__(self,coor1,coor2):
        self.coor1=coor1
        self.coor2=coor2
    
    def distance(self):
        x1,y1=self.coor1
        x2,y2=self.coor2
        return ((x2-x1)**2+(y2-y1)**2)**0.5
           
    def slope(self):
         x1,y1=self.coor1
         x2,y2=self.coor2
         return float ((y2-y1)/(x2-x1))
    
coordinate1 = (3,2)
coordinate2 = (8,10)
 
li = Line(coordinate1,coordinate2)
print(li.distance())
print(li.slope())
       
        
print("**************************************************")
class Cylinder(object):
    pi=3.14
    def __init__(self,height=1,radius=1):
        self.height=height
        self.radius=radius
        
    def volume(self):
        return((self.radius**2)*(self.height)*Cylinder.pi)
    
    def surface_area(self):
        return (((((self.radius*self.height)*Cylinder.pi)*2)+(self.radius**2)*(2*Cylinder.pi)))

c = Cylinder(2,3)
print(c.volume())
print(c.surface_area()) 


print("*************Exception handling*************************************")

try :
    print(2+'s')
except TypeError:
    print("There was a type error")
finally:
    print("Finally this was printed")
    
try :
    print(2+'s')
except :
    print("There was a type error")
finally:
    print("Finally this was printed")    
    

try:
    f=open('testfile.txt','w')
    f.write('test write this')
except:
    print("erro in writing to file!")
else:
    print ("File Wrie was success")
    
    
    
try:
    f=open('testfile1.txt','r')
    f.write('test write this')
except:
    print("E rror in writing to file!")
else:
    print ("File Wrie was success")    
    
def askint():
    while True:
        try:
            val=int(input("please enter an integer:"))
        except:
            print("Look like yiu didn't enter an integer!")
            continue
        else :
            print("Correct, that is an integre")
            break
        finally:
            print("Finally block executed")
        
        print(val)
        
'''askint()''' 

print("*******Exception handling assignment**************")
try :
    for i in ['a','b','c']:
        print (i**2)
except:
    print("Error occured in excuting code ")
else:
    print("No error occured")

try:
    x=5
    y=0
    z=x/y




except ZeroDivisionError:
    print("Error occured in divsion")
else:
    print("No error in div")
finally:
    print("All Done!")



def ask():
    while True:
        try:    
            a=int(input('Input an Integer'))
        except:
            print("An error occurred! Please try again!")
            continue
        else:
            print("Thank you, you number squared is:",a**2)
            break
    
ask()    
    
    






 
