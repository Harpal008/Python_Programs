# -*- coding: utf-8 -*-
"""
Created on Sat Dec 22 06:53:17 2018

@author: harpal
"""
'''need verifcation'''
st = 'Print only the words that start with s in this sentence'
l=st.split(" ")
print(l)

'''to print all even no from 0 to 10'''
l=[x**2 for x in range(11) if x %2==0]
print(l)

range(0,11,2)

'''Use List comprehension to create a list of all numbers between 1 and 50 that are divisible by 3.'''
l=[x for x in range(1,51) if x %3==0]
print(l)

'''Go through the string below and if the length of a word is even print "even!"'''
st = 'Print every word in this sentence that has an even number of letters'
lst=st.split(' ')

for x in lst:
    if len(x)%2==0:
        print("Even",x)
        
l=["Even word  "+x for x in lst if len(x)%2==0]
print(l)

''''''''''''''''''''''''''''''''''''''''''''''''''''''''

for x in range(1,101):
    if x%3==0:
        print("Fizz")
    elif x%5==0:
        print ("Buzz")
    else:
        print(x)

''''''''''''''''''''''''''''''''''''''''''''''''''''''''

'''Use List Comprehension to create a list of the first letters of every word in the string below:
'''
st = 'Create a list of the first letters of every word in this string'

lst=st.split(" ")
print("I an in new loop")
l=[x[0] for x in lst]
print(l)













        
        
        
        