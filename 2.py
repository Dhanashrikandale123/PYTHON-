# -*- coding: utf-8 -*-
"""
Created on Sun Dec 12 12:00:53 2021

@author: mali-
"""
'''Write a python program that displays a message as follows for a given number:

If it is a multiple of three, display "Zip"
If it is a multiple of five, display "Zap".
If it is a multiple of both three and five, display "Zoom".
If it does not satisfy any of the above given conditions, display "Invalid".'''

#lex_auth_01269363490743091290
def display(Num):
    message=""
    if Num % 3 == 0 and Num % 5 == 0 :
        print("Zoom")
        
    elif Num % 3 == 0 :
        print("Zip")
    
    elif Num % 5 == 0 :
        print("Zap")
        
    else :
        print("Invalid")
    return message
message=display(9)
print(message)


#Provide different values for num and test your program
