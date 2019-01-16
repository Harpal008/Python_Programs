# -*- coding: utf-8 -*-
"""
Created on Wed Jan  9 10:59:44 2019

@author: harpal
"""

def f(g,**args):
    return g(args)

#print f(lambda z: reduce (lambda x,y:x+y,z,0),1,2,3)

print(i for i  in filter (lambda x:x&(x-1)==0,range(1,20)))

def func(a,b):
    if b==0:
        return a
    else:
        return func(a^b,(a&b)<<1)

print(func(5,6))

print(5^6)

print(8.4//2)