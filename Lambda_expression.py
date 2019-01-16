# -*- coding: utf-8 -*-
"""
Created on Sat Dec 22 09:18:17 2018

@author: harpal
"""
def square(num):
    result=num**2
    return result

a=square(2)

print(a)

def square(num):
    return num**2

a=square(2)

print(a)

def square(num): return num**2
a=square(3)  
print(a)

sqaure=lambda num:num**2
sqaure(10)
print(square(10))

'''check even'''
even=lambda num:num%2==0
print(even(4))

'''First Char of a string'''
s="This is new line module"
#lst=s.split(" ")
first_char=lambda lst:lst[0]
print(first_char(s))

rev=lambda s:s[::-1]
print(rev("hello"))


add=lambda x,y:x+y
print(add(4,5))














