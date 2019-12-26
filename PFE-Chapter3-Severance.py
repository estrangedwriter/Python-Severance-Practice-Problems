# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 21:32:58 2019

@author: Jerom
"""

####PFE (Severance) Chapter 3: CONDITIONAL EXECUTION
####
###

###Exercise 1: Rewrite your pay computation to give the employee 1.5 times the hourly rate for hours worked above 40 hours
####
###

Hours = float(input('Enter Hours:'))
Rate = float(input('Enter Rate:'))

if Hours < 40: 
    Pay = Hours * Rate

else:
    Overtime = 1.5*Rate
    Pay = (40 * Rate) + (Overtime * (Hours - 40))

print('Pay:', Pay)


###Exercise 2: Rewrite your pay program using try and except so that your program handles non-numeric input gracefully by printing a message and exiting
###the program. The following shows two executions of the program:
###
#

try:

    Hours = float(input('Enter Hours:'))
    Rate = float(input('Enter Rate:'))


    if Hours < 40: 
        Pay = Hours * Rate
        print('Pay:', Pay)

    else:
        Overtime = 1.5*Rate
        Pay = (40 * Rate) + (Overtime * (Hours - 40))
        print('Pay:', Pay)


except ValueError:
    print('Error, please enter numeric input')

###Exercise 3: Write a program to prompt for a score between 0.0 and 1.0. If the score is out of range, print an error message. If the score is between 0.0
###and 1.0, print a grade using the following table: 

print ('>= 0.9     A\n>= 0.8     B\n>= 0.7     C\n>= 0.6     D\n < 0.6     F')

    
try:
    score = float(input('Enter score:'))
    
    if score >1:
        print('Bad score')
    
    elif score >=0.9:
        print ('A')
            
    elif score >=0.8:
        print('B')
        
    elif score>=0.7:
       print('C')
            
    elif score>=0.6:
        print('D')
            
    elif score <0.6:
        print('F')
            
    elif score < 0:
        print('Bad score')    

except ValueError:
    print('Bad score')
    











