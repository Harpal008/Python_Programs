# -*- coding: utf-8 -*-
"""
Created on Tue Dec 25 08:12:31 2018

@author: harpal
"""

def func():
    return 1

print(func())

s='This is a global varible'

def func():
    print(locals())
    
#print( globals().keys() )
print(func())

def hello(name='test'):
    return 'Hello '+name

print(hello())
greet=hello
del hello
#hello()

greet()

print("#### Function within functions #########")

def hello(name='Ram'):
    print('The hello() function has been executed')
    def greet():
        return '\t this is inside the great() function'
    def welcome():
        return'\t This is inside the welcome() function'
    
    print(greet())
    print(welcome())
    print("Now we are back inside the Hello() functions")


hello()

def hello(name='Ram'):
    def greet():
        return '\t this is inside the great() function'
    def welcome():
        return'\t This is inside the welcome() function'
    
    if name =='Ram':
        return greet
    else: 
        return welcome

x=hello() 
print(x)
print(x())

print("#### Function as Argument #########")
      
def hello():
    return 'Hi Ram!'

def other(func):
    print("other code goes here!")
    print(func())      

other(hello)      
      
def new_decoratores(func):
    def wrap_func():
        print('code here, before executing the func')
        func()
        print('code here, after executing the func')

    return wrap_func

def func_needs_decorator():
    print('This function needs a decorator!')
    

func_needs_decorator=new_decoratores(func_needs_decorator)
func_needs_decorator()


@new_decoratores
def func_needs_decorator():
    print("This functions needs a decorator!")
    
func_needs_decorator()








 
      