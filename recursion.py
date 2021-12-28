# -*- coding: utf-8 -*-
"""
Created on Tue Dec 28 21:28:35 2021

@author: mali-
"""
'''A 10-substring of a number is a substring of its digits that sum up to 10.

For example, the 10-substrings of the number 3523014 are:
3523014, 3523014, 3523014, 3523014

Write a python function, find_ten_substring(num_str) which accepts a string and returns the list of 10-substrings of that string.

Handle the possible errors in the code written inside the function.

Sample Input

Expected Output

'3523014'

['5230', '23014', '523', '352']

 

Code in Python 3'''

def getsum(num):
    Sum=0
    for n in num:
        Sum+=int(n)
    return Sum
def getstring(num_str):
    l=[]
    for i in range(2,len(num_str)):
        for j in range(0,len(num_str)):
            if getsum(num_str[j:j+i])==10:
                l.append(num_str[j:j+i])
    return l
num_str="5055"
result=getstring(num_str)
print(result)
    