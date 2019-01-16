# -*- coding: utf-8 -*-
"""
Created on Fri Dec 21 08:44:29 2018

@author: harpal
"""

f=open('test.txt')
print(f.read())
print(f.read())

f.seek(0)
print(f.read())

print(f.readlines())

#f.seek(0)

print("for loop")
for line in open('test.txt'):
    print (line)