# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 21:16:40 2019

@author: Jerom
"""

####PFE (Severance) Chapter 2: VARIABLES, EXPRESSIONS, AND STATEMENTS. 
####
###

###Exercise 2: Write a program that uses input to prompt a user for their name and then welcomes them. 
####
#### Enter your name: Chuck
#### Hello Chuck

name = input('Enter your name:')

print ('Hello', name)

####Exercise 3: Write a program to prompt the user for hours and rate per hour to compute gross pay.
####Enter Hours: 35
####Enter Rate: 2.75
####Pay: 96.25

Hours = float(input('Enter Hours:'))
Rate = float(input('Enter Rate:'))
Pay = Hours * Rate

print('Pay:', Pay)

####Exercise 4: Assume that we execute the following assignment statements:
####
width = 17

height = 12.0

print (width//2)
print (width/2.0)
print(height/3)
print(1 + 2 * 5)


####Exercise 5: Write a program which prompts the user for a Celsius temperature, convert the temperature to Fahrenheit, and print out the converted temperature.
###
###

cels = float(input('Enter Celsius temperature: '))

Fahr = (cels * 9/5 + 32)

print (cels,' degrees Celsius = ',Fahr, 'degrees Fahrenheit')










