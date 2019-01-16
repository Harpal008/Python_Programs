# -*- coding: utf-8 -*-
"""
Created on Fri Dec 21 07:16:13 2018

@author: harpal
"""

my_dic={'key1':'value1','key2':'value2'}
print(my_dic)
print(my_dic['key1'])
print(my_dic.keys())
print(my_dic.values())


my_dic={'key1':123,'key2':'value2'}
print(my_dic['key1']-100)

my_dic={10:'value1','key2':'value2'}
print(my_dic[10])

my_dic={'key1':123,'key2':'value2'}
print(my_dic['key1']-100)

my_dic['key1']+=200
print(my_dic['key1'])


d={}
print(d)
d['animal']='Dog'
d['answer']=42
print(d)

#nested dictonary
d={'k1':{'nestkey':{'subnestkey':'value'}}}
print(d)
print(d.keys())
print(d.values())

print(d['k1']['nestkey']['subnestkey'])

d={}
d['k1']=1
d['k2']=2
d['k3']=3
print(d)
print(d.keys())
print(d.values())
print(d.items())






















