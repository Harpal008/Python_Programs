# -*- coding: utf-8 -*-
"""
Created on Fri Dec 21 19:16:12 2018

@author: harpal
"""
l=[]
for letter in "word":
    l.append(letter)
    
print(l)


lst=[x for x in 'word']
print(lst)

y=[x**2 for x in range(0,10)]
print(y)

lst=[number for number in range(11) if number %2==0]
print(lst)


celsius=[0,10,20.1,34.5]

fahrenheit=[ (temp*(9/5)+32) for temp in celsius ]

print(fahrenheit)

'''Nested list Comprehensive'''


lst=[x**2 for x in [x**2 for x in range(11)]]
print(lst)