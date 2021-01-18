# -*- coding: utf-8 -*-
"""
Created on Sat Nov 14 12:17:55 2020

@author: giris
"""

#my_list = list(range(0,440)) 
#print (my_list)

#def hellofunc(myname):
#    print('hello ',myname)    
#hellofunc('Rushi')
#def variable_test():
#    first = 10
#    second = 20
#    return first * second
#print(variable_test())    
#import sys
#print(sys.stdin.readline())
def moon_weight():
    start_weight = int(input("Put your start_weight Mr. Bob"))
    gain_per_year = int(input('Put your gain_per_year Mr. Bob'))
    number_of_years = int(input('Put your number_of_years Mr. Bob'))
    for year in range(1, number_of_years + 1):
        print ('year ', year, ", " 'weight = ', start_weight + gain_per_year * year)
        
moon_weight()






    