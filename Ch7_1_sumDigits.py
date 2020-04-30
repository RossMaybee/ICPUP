# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""



def sumDigits(s):
    """Assumes s is a string
        Returns the sum of the decimal digits in s
            For example, if s is 'a2b3c it returns 5'"""
    numDict = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    checkString = s[:]
    numString = []
    sumString = 0
    for c in checkString:
        if c in numDict:
            numString.append(int(c))
    
    for i in numString:
        sumString+=i
    return(sumString)


print('Returned s as: ', sumDigits('ab4th6fhfj7'))
