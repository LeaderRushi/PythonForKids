# -*- coding: utf-8 -*-
"""
Created on Sun Nov 29 19:22:48 2020

@author: giris
"""

## Problem 1 ## 
def print_rectangle (length, width):
    area = length * width
    perimeter = length * 2 + width * 2
    print ('Area = ', area, ', Perimeter = ', perimeter)
    
def print_rect():
    length = int(input('Please enter length '))
    width = int (input('Please enter width '))
    area = length * width
    perimeter = length * 2 + width * 2
    print ('Area = ', area, ', Perimeter = ', perimeter)
## Problem 2 ## 
def print_circle():
    import math
    radius = int (input('Please enter radius '))
    Area = math.pi * radius**2
    Perimeter = 2 * math.pi * radius
    print (f'Area = {Area:.2f}, Perimeter = {Perimeter:.2f}')

#Problem 3

def print_sum(n):
    sum = 0
    for x in range(1, n+1):
        sum = sum + x
    print ('Sum from 1 to ', n,'= ', sum)

def print_summation():
    n = int (input('Please enter n '))
    sum = 0
    for x in range(1, n+1):
        sum = sum + x
    print('Sum from 1 to ', n, '= ', sum)

##Problem 4

def print_factorial(n):
    factorial = 1
    for x in range(1, n+1):
        factorial = factorial * x
    print (n ,'! = ', factorial)

def print_fact():
    n = int (input('Enter a random number. NOW '))
    factorial = 1
    for x in range(1, n+1):
        factorial = factorial * x
    print (n ,'! = ', factorial)

#Problem 5
def print_sum_from_a_to_b(from_a, to_b):
    sum = 0
    for x in range (from_a, to_b + 1):
        sum = sum + x 
    print ('sum from', from_a,' to ', to_b, ' = ', sum)

def sum_from_a_to_b():
    from_a = int (input('Enter point a number'))
    to_b = int (input('Enter point b number'))
    sum = 0
    for x in range(from_a, to_b + 1):
        sum = sum + x
    print ('sum from', from_a, ' to ', to_b, ' = ', sum)

def sum_check_from_a_to_b():
    from_a = int (input('Enter point a number: '))
    to_b = int (input('Enter point b number: '))
    while (from_a > to_b):
        print ('Error: Please enter a < b : ')
        from_a = int (input('Enter point a number '))
        to_b = int (input('Enter point b number '))
    sum = 0
    for x in range(from_a, to_b + 1):
        sum = sum + x
    print ('sum from', from_a, ' to ', to_b, ' = ', sum)

#Problem 6
def print_product_from_a_to_b():
    from_a = int (input('PLEASE ENTER THE NUMERIC VALUE OF A'))
    to_b = int (input('PLEASE ENTER THE NUMERIC VALUE OF B'))
    product = 1
    for x in range (a, b + 1):
        product = product * x
    print('Product equals', product, '!')  




## Function calls ##

# print_rectangle (5, 10)
# print_rect()
# print_circle()    
# print_sum(5)
# print_factorial(5)
# print_fact()
# print_sum_from_a_to_b(100, 200)
# sum_from_a_to_b()
# sum_check_from_a_to_b()
print_product_from_a_to_b(5, 7)

