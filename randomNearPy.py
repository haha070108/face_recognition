#!/usr/bin/env python
#-*- coding:utf-8 -*-
from nearpy import Engine
from nearpy.hashes import RandomBinaryProjections
import  numpy
import  time
# Dimension of our vector space

dimension = 128
# Create a random binary hash with 10 bits
rbp = RandomBinaryProjections('rbp', 10)

# Create engine with pipeline configuration
engine = Engine(dimension, lshashes=[rbp])

# Index 1000000 random vectors (set their data to a unique string)
for index in range(100000):
 v = numpy.random.randn(dimension)
 #print('data_%d' % index)
 engine.store_vector(v, 'data_%d' % index)

# Create random query vector
query = numpy.random.randn(dimension)
print("query=",query.shape)
# Get nearest neighbours
start =time.time()
N = engine.neighbours(query)
print(N)
print(len(N))
end =time.time()
print("spend time %f"% (end-start))