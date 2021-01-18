# -*- coding: utf-8 -*-
"""
Created on Sun May 24 11:54:05 2020

@author: rushi 
"""

print("Hello World")

N = input ("How many times do you want to print?\n")
N = int (N)
for index in range (1,N+1):
    print ("Happy birthday Saina!!")   
N = input ("I can find sum of numbers up to N. Please type N and press enter") 
N = int (N)
Sum = 0
for index in range(1,N+1):
    Sum = Sum + index    
print("Sum is ", Sum)





      