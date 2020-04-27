# -*- coding: utf-8 -*-
"""
Created on Mon Dec 12 18:34:54 2016

@author: rossm
Introduction to Computation and Programming Using Python
Finger Exercise 2.4
Finding Largest of 10 Odd Numbers
"""

print 'This program will receive an input of 10 numbers and return the largest odd'

numbers = [input('Enter a number: ') for i in range(10)]
           
odds = [x for x in numbers if x%2 != 0]

def find_max(odds):
    if len(odds) >= 1:
        m = len(odds)
        current_point = 0
        largest = odds[current_point]
        while m > 0:
            if odds[current_point + 1] > largest:
                largest = current_point
                m -= 1
                current_point += 1
            else:
                return largest
    else:
        print "There are no odd numbers."