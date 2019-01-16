# -*- coding: utf-8 -*-
"""
Created on Mon Dec 24 10:16:01 2018

@author: harpal
"""
from pyechonest import config 
config.ECHO_NEST_API_KEY="YOUR API KEY"




from pyechonest import artist
bk = artist.Artist('bikini kill')
print ("Artists similar to: %s:" % (bk.name,))
for similar_artist in bk.similar: 
    print ("\t %s:" %(similar_artist.name,))