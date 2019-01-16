# -*- coding: utf-8 -*-
"""
Created on Sat Dec 22 07:42:55 2018

@author: harpal
"""
  
def my_add(arg1,arg2):
    """
    Here is my docString!
    """
    #print(arg1+arg2)
    pass
  
my_add(1,2)
print(help(my_add))

def add_num(num1,num2):
    return num1+num2

a=add_num(1,2)
print(a)


def add_num(num1,num2):
    return num1+num2

a=add_num('one ','two')
print(a)


'''check number is prime'''

def is_prime(num):
    """
    This functions check for prime numbers
    """
    for n in range(2,num):
        if num %n==0:
            print ("Not Prime")
            break
        else:
            print ("Number os prime")
    
    pass

is_prime(12)


import math

def is_prime(num):
    '''
    Better method of checking for primes. 
    '''
    if num % 2 == 0 and num > 2: 
        return False
    for i in range(3, int(math.sqrt(num)) + 1, 2):
        if num % i == 0:
            return False
    return True

print(is_prime(14))














