# -*- coding: utf-8 -*-
"""
Created on Tue Dec 25 15:43:56 2018

@author: harpal
"""

def gensquares(N):
    for num in range(N):
        yield num**2

for x in gensquares(10):
    print (x)
    
'''Create a generator that yields "n" random numbers between a low and high number (that are inputs). Note: Use the random library. For example:
'''
print("##########################################")
      
import random
random.randint(1,10) 

def rand_num(low,high,n):
    for i in range(n):
        yield random.randint(low,high) 
        
for num in rand_num(1,10,12):
    print (num)
     
print("##########################################")
    
s = 'hello'
s=iter(s)
print(next(s))