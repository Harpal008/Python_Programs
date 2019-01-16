# -*- coding: utf-8 -*-
"""
Created on Fri Dec 21 16:31:25 2018

@author: harpal
"""

l=[1,2,3,4,5]

for element in l:
    print(element )
    
for element in l:
    if element%2==0:
        print(element)
    else:
        print ("Odd number!")
        
        
#list sume
list_sum=0        
for element in l:
    list_sum=list_sum+element
print("Sum of list ",list_sum)


s="This is a String"

for letter in s:
    print(letter)
    
 
tup=(1,2,3,4,5)
for t in tup:
    print (t)

l=[(2,4),(6,8),(10,12)]
print(l[0][0])

for tup in l:
    print(tup)
    
for (t1,t2) in l:
    print (t1)


d={'k1':1,'k2':2,'k3':3}
    
for item in d:
    print (item)
    
for k,v in d.items():
    print (k)
    print (v)
















    
    