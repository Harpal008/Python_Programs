# -*- coding: utf-8 -*-
"""
Created on Thu Dec 27 11:00:17 2018

@author: harpal
"""
import StringIO

message = 'This is just a normal string.'
# Use StringIO method to set as file object
f = StringIO.StringIO(message)
f.read()