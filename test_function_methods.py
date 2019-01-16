# -*- coding: utf-8 -*-
"""
Created on Sat Dec 22 14:08:22 2018

@author: harpal
"""
'''Write a function that computes the volume of a sphere given its radius.'''

def vol(rad):
    return (4/3)*22/7*rad**3

print(vol(4))

'''Write a function that checks whether a number is in a given range (Inclusive of high and low)'''

def ran_check(num,low,high):
    if num in range(low,high+1):
        print("Given Number is in Range","Number",num)
        print("Range",low,"-",high)
    else:
        print("Number out of range")

ran_check(4,2,10)
ran_check(2,2,10)
ran_check(10,2,10)
ran_check(200,2,10)


def ran_bool(num,low,high):
    if num in range(low,high+1):
        return True
    else:
        return False

a=ran_bool(3,1,10)
print(a)

'''Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters.'''

s='Hello Mr. Rogers, how are you this fine Tuesday?'
upper_letter=0
lower_letter=0
for x in s:
    if x.isupper():
        upper_letter+=1
    elif x.islower():
        lower_letter+=1

print ("No. of Upper case characters",upper_letter)
print ("No. of Lower case characters",lower_letter)


'''Write a Python function that takes a list and returns a new list with unique elements of the first list.'''

lst=[1,1,1,1,2,2,3,3,3,3,4,5]

def unique_list(lst):
    return list(set(lst))
a=unique_list(lst)
#lst2=list(a)
#print(lst2)
print(a)

'''Write a Python function to multiply all the numbers in a list.'''

orglist=[1, 2, 3, -4]
mult=1
def multiply(numbers):
    global mult
    for x in numbers:
        mult=mult*x
        
    return mult

a=multiply([1,2,3,-4])
print(a)

'''Write a Python function that checks whether a passed string is palindrome or not.'''


def palindrome(s):
    l=len(s)
    for i in range(1,l+1):
        if s[i-1]==s[-i]:
            a=True
        else:
            a=False
    return a

a=palindrome("helleh")
a=palindrome("abba")
if a:
    print("String is Pallindrone")
else:
    print("String is not pallindrone")
    
'''Write a Python function to check whether a string is pangram or not'''


# A Python Program to check if the given 
# string is a pangram or not 

def checkPangram(s): 
	List = [] 
	# create list of 26 charecters and set false each entry 
	for i in range(26): 
		List.append(False) 
      
	#converting the sentence to lowercase and iterating 
	# over the sentence 
	for c in s.lower(): 
		if not c == " ": 
			# make the corresponding entry True 
			List[ord(c) -ord('a')]=True
           		
	#check if any charecter is missing then return False 
	for ch in List: 
		if ch == False: 
			return False
	return True

# Driver Program to test above functions 
sentence = "The quick brown fox jumps over the little lazy dog"

if (checkPangram(sentence)): 
	print ('"'+sentence+'"')
	print ("is a pangram")
else: 
	print ('"'+sentence+'"')
	print ("is not a pangram")


import string

def ispangram(str1, alphabet=string.ascii_lowercase):  
    alphaset = set(alphabet)
    return alphaset <= set(str1.lower())  

print(ispangram("The quick brown fox jumps over the lazy dog"))
print(set(string.ascii_lowercase)<=set("The quick brown fox jumps over the lazy dog"))



    





















