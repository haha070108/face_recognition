#!/usr/bin/env python
#-*- coding:utf-8 -*-
s = u"""
---------------------------------------------------------------
author:simpleness
Date: 2018/3/24 0:15
python verison:2.7.13
Effect：
need lib：
---------------------------------------------------------------
"""

import pyfpgrowth
import operator
from shuju import shuju_list

transactions = [[2, 4, 5, 2],
                [2,4],
                [2,3],
                [1, 2, 4],
                [9, 2, 3],
                [3,4],
                [10, 2, 23, 4, 6],
                [12, 2, 13, 4, 5],
                [11, 2, 13, 4]]

print (len(shuju_list))
patterns = pyfpgrowth.find_frequent_patterns(shuju_list, 2)
#print patterns
n = sorted(patterns.items(),key = operator.itemgetter(1),reverse=True)
max_n = n[0][0][0]
#print n

# for k,v in patterns.items():
#     print k, v
rules = pyfpgrowth.generate_association_rules(patterns, 0.2)
for k,v in rules.items():
    #print k,v
    if max_n in k:
        print( k,v)