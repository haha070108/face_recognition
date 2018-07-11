#!/usr/bin/env python
#-*- coding:utf-8 -*-
from nearpy.distances import *
from nearpy import Engine
import numpy as np
import  numpy.matlib
list =[1,2,3,4]
list1 =[1,2,3.1,4]
a =np.asarray(list)
b =np.asarray(list1)
engine =Engine(4,distance=EuclideanDistance)
engine.store_vector(a)
engine.store_vector(b)
# print(engine.candidate_count())

print(np.random.randn(10))