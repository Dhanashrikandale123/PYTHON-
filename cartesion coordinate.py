# -*- coding: utf-8 -*-
"""
Created on Mon Oct 25 09:27:04 2021

@author: mali-
"""
D=int(input("enter the value of direction:"))
d=int(input("enter the value of distance:"))
def quadrent(x,y):
    if(x>0 and y>0):
        print("first qua")
    elif(x<0 and y<0):
        print("sec qua")
    elif(x>0 and y>0):
        
        print("third qua")
    elif(x>0 and y<0):
        print("fourth qua")
    else:
        print("at origin")
result=("the coordinates lies bet",quadrent(x,y))