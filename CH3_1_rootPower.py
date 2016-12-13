# -*- coding: utf-8 -*-
"""
Created on Mon Dec 12 20:06:09 2016

@author: rossm
Introduction to Computation and Programming Using Python
Finger Exercise 3.1 
Root ** Power
"""

target = input("Enter a number: ")

power = 0
root = 1

while power < 6:
    power = power + 1
    if (root**power) == target:
        power = 6
    else:
        root = (number - 1)
        

    