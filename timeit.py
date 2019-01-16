# -*- coding: utf-8 -*-
"""
Created on Thu Dec 27 06:33:04 2018

@author: harpal
"""

import timeit

print( "-".join(str(n) for n in range(100))

print(%timeit "-".join([str(n) for n in range(100)]))

a=timeit.timeit('"-".join(str(n) for n in range(100))', number=10000)