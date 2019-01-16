# -*- coding: utf-8 -*-
"""
Created on Tue Dec 25 11:29:14 2018

@author: harpal
"""

def gen_cubes(n):
    for num in range(n):
        yield num**3
        
for x in gen_cubes(10):
    print (x)
    
print("######## Fibonaci series  #######")    
def genfibon(n):
    a=1
    b=1
    for i in range(n):
        yield a
        t=a
        a=b
        b=t+b
        
for num in genfibon(10):
    print(num)
    
    
def genfibon(n):
    a=1
    b=1
    for i in range(n):
        yield a
        a,b = b,a+b
        
for num in genfibon(10):
    print(num)    
    
def simple_gen():
     for x in range(3):
         yield x
         
g=simple_gen()
print(next(g)) 
print(next(g)) 
print(next(g)) 

s='hello'
for let in s:
    print(let)
    
next(s)


        
         