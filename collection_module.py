# -*- coding: utf-8 -*-
"""
Created on Tue Dec 25 17:30:57 2018

@author: harpal
"""


#counter is dictonay sub class
from collections import Counter
l=[1,1,1,1,1,12,2,2,2,2,2,2,33,3,3,3,3,4,4,4,4,555,5,5,5,5,5]
print(Counter(l))


s='asasbvdcvbcdvccdsvc'
print(Counter(s))

s='How amny times does each word show up in this sentence word word shoe up up '
print(Counter(s))
a=s.split()
print(Counter(a))

#method with counter 
c=Counter(a)
print("##### methods of counter#######")
print(sum(c.values()))
print(c.most_common(3))
print(list(c))
print("############")
print(c.most_common()[::-1])


print("###########default dict ############")
      
      

from collections import defaultdict

d=defaultdict(object)
print("fisrt o/p",d['one'])

for item in d:
    print(item)
    
d=defaultdict(lambda : 0)
print("third o/p",d['one']) 
d['two']=2
print("value",d['two']) 
print(d)
    

print("###########order  dict ############")
      
d={}
d['a']=1
d['b']=2
d['c']=3
d['d']=4
d['e']=5 

for k,v in d.items():
    print (k,v)
     
print("##########################")    
from collections import OrderedDict    
      
d=OrderedDict()
d['a']=1
d['b']=2
d['c']=3
d['d']=4
d['e']=5 

for k,v in d.items():
    print (k,v)

print("#####Named Tuple#####################")       
      
from collections import namedtuple
Dog=namedtuple('Dog','age breed name') 
sam=Dog(age=2,breed='lab',name='ram')
print(sam)
print(sam.age)
print(sam.count)
print(sam[0])
      
      
print("#####python debugger#####################") 
import pdb
#x=[1,3,4]
y=2
z=3
#result=y+z
#print(result)

#pdb.set_trace()
#result2=y+x
#print (result2)
      
      
print("########Date time module###############")      
import datetime
t=datetime.time(5,25,1)      
print(t) 

print(datetime.time.min)
print(datetime.time.max)

today=datetime.date.today()
print(today)
print(today.timetuple())
print(today.month)

      