# -*- coding: utf-8 -*-
"""
Created on Mon Dec 12 20:26:26 2016

@author: rossm
Introduction to Computation and Programming Using Python
Finger Exercise 3.2
Summing Input Strings
"""

counter = 0
sum = 0
reals = [1.23,2.4,3.123]

for n in range(3):
    sum = sum + reals[counter]
    counter = counter + 1

print sum