# -*- coding: utf-8 -*-
"""
Created on Sun Sep 27 04:48:53 2020

@author: Robbi
"""

#Introduce the program
print('Let\'s change a list of integers')

#Defining a list
testList = [3, 8, 2, 5, 30, 7, 9]

#Defining the function
def changeList(myList):

    #For loop to do the replacement
    for index in range(len(myList)):

        if (myList[index] % 3 == 0) and (myList[index] % 5 == 0):
            myList[index] = 'best'

        elif myList[index] % 5 == 0:
            myList[index] = 'better'

        elif myList[index] % 3 == 0:
            myList[index] = 'good'

    return myList

#Spacer
print()

#Print the original list
print(testList)

changeList(testList)

print(testList)