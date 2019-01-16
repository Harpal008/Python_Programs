# -*- coding: utf-8 -*-
"""
Created on Mon Dec 24 14:07:14 2018

@author: harpal
"""
import functools

temp=[0,22,5,40,100]
print(list(map(lambda T:((9.0/5)*T+32),temp))) 
lambda x,y:x+y
a=[1,2,3]
b=[4,5,6]
c=[7,8,9]


z=list(map(lambda x,y,z:x+y+z, a,b,c ))
print(z)

lst=[47,11,42,13,233,44,66,88,999]
print(max(lst))

max_find=(lambda x,y:x if (x>y) else y,lst)
print(max_find)
'''functools.reduce(max_find,lst)'''
 
def even_check(num):
    if num%2==0:
        return True
    else:
        return False
    
print(even_check(35))

lst=range(10)
print(list(filter(even_check,lst)))



x=[1,2,3]
y=[4,5,6]

print(list(zip(x,y)))

a=[1,2,3,4,5]
b=[2,2,10,1,1]

d1={'a':1,'b':2}
d2={'c':1,'d':2}

print(list(zip(d1,d2)))


l=['a','b','c']
count=0
for item in l:
    print (count)
    print(item)
    count+=1

for count,item in enumerate(l):
    print(count)
    print(item)


l=[True,True,False,False]
print(all(l))
print(any(l))

print("#########complex #########")
      
print(complex(2,3))
print(complex(10,1))
print(complex('10+2j'))























