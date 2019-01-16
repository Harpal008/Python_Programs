# -*- coding: utf-8 -*-
"""
Created on Fri Dec 21 12:08:36 2018

@author: harpal
"""

print(2/3)
print(4*(6+5))
print(4*6+5)
print(4+6*5)
print(3+1.5+4)

print(25**0.5)
print(5**2)
s='hello'
print(s[1])
print(s[::-1])
print(s[-1])
print(s[4])

#lists
l1=[0,0,0]
print(l1)

l1=[]
l1.append(0)
l1.append(0)
l1.append(0)
print(l1)

l = [1,2,[3,4,'hello']]
l[2][2]='goodbye'
print(l)

l=[5,3,4,6,1]
l.sort()
print(l)

d={'simple_key':'hello'}
print(d['simple_key'])

d={'k1':{'k2':'hello'}}
print(d['k1']['k2'])

d = {'k1':[{'nest_key':['this is deep',['hello']]}]}
print(d['k1'][0]['nest_key'][1])


d = {'k1':[1,2,{'k2':['this is tricky',{'tough':[1,2,['hello']]}]}]}
print(d['k1'][2]['k2'][1]['tough'][2])


#print(d['k1']['nest_key']['this is deep'][2])

l=(1,2,3)
print(l)

x=set()
x.add(1)
print(x)

l = [1,2,2,33,4,4,11,22,3,3,2]

print(set(l))

print(2 > 3)
print(3 == 2.0)
print(2 == 2.0)
print(4**0.5 != 2)

l_one = [1,2,[3,4]]
l_two = [1,2,{'k1':4}]

print(l_one[2][0] >= l_two[2]['k1'])

















