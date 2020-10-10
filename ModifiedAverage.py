# -*- coding: utf-8 -*-
"""
Created on Sat Sep 26 19:56:09 2020

@author: Robbi
"""

#Introduce the program
print('Let\'s redefine the average function!')

#Defining the average function
def average(someArgument, *args):
    """This function has an extra parameter to not have a divide by zero error with zero arguments"""

    someArgument = 0

    if len(args) == 0:
        print('There was no list!')
        return someArgument

    else:
        return sum(args) / len(args)

#Spacer
print()

#Calling the average function multiple times
print(average(-8, 10, 17, 12, 19))
print(average(50, 64, 78, 29))
print(average(789_456, 235, 685))
print(average(-13, 690_000))
print(average(9, 10))
print(average())