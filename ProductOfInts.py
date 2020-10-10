# -*- coding: utf-8 -*-
"""
Created on Sat Sep 26 20:23:03 2020

@author: Robbi
"""
#Import Statements
import math

#Introduce the program
print('Let\'s calculate the product of ANY number of integers')

#Defining the product function
def product(*args):
    """This function calculates the product of any number integers"""

    if len(args) == 0:
        return 0

    else:
        return math.prod(args)

#Spacer
print()

#Calling the product function multiple times
print(product(1,2,3,4,5))
print(product(10,20,40,50))
print(product(7,12,34))
print(product(87,6))
print(product(45612345600))
print(product())