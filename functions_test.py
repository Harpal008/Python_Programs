# -*- coding: utf-8 -*-
"""
Created on Mon Dec 24 17:14:48 2018

@author: harpal
"""

print("*****************************************************")
'''Use map to create a function which finds the length of each word in the phrase (broken by spaces) and return the values in a list.'''
def word_lengths(phrase):
    a=phrase.split()
    return list(map(lambda x:len(x),a))
        
print(word_lengths('How long are the words in this phrase'))

'''Use reduce to take a list of digits and return the number that they correspond to. Do not convert the integers to strings!'''

print("*****************************************************")
'''Use filter to return the words from a list of words which start with a target letter.'''
def filter_words(word_list, letter):
    return list(filter(lambda x:x.startswith(letter),word_list))

l = ['hello','are','cat','dog','ham','hi','go','to','heart']
print(filter_words(l,'h'))
print("*****************************************************")

'''Use zip and list comprehension to return a list of the same length where each value is the two strings from L1 and L2 concatenated together with connector between them. Look at the example output below:'''

def concatenate(L1, L2, connector):
    #return list(zip((x+connector for x in L1),L2))
    return list(x+connector+y for (x,y) in zip(L1,L2))    
print(concatenate(['A','B'],['a','b'],'-'))

'''Use enumerate and other skills to return a dictionary which has the values of the list as keys and the index as the value. You may assume that a value will only appear once in the given list'''
def d_list(L):
    return {key:value for value,key in enumerate(L) }
print(d_list(['a','b','c']))


'''Use enumerate and other skills from above to return the count of the number of items in the list whose value equals its index.'''
def count_match_index(L):
    match=0
    for count,item in enumerate(L):
        if count==item:
            match+=1
    return match

print(count_match_index([0,2,2,1,5,5,6,10]))












