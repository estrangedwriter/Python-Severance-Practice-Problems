# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 23:09:02 2019

@author: Jerom
"""

####PFE (Severance) Chapter 5: ITERATIONS
####
###
###Exercise 1: Write a program which repeatedly reads numbers until the user enters "done". Once "done" is entered, print out the total, count, 
###and average of the numbers. If the user enters anything other than a number, detect their mistake using try and except and print an error 
###message and skip to the next number.



def iterations():

    count = 0
    total = 0  
    average = 0


    while True:        
            line = input('Enter a number: ')
        
            if line == 'done':   
               print (count, total, average)
               break
            try:   
                count = count + 1
                line1 = float(line)
                total = line1 + total
                average = total / count
        
            except:
                print('invalid input')
            
iterations()   

###Exercise 2: Write another program that prompts for a list of numbers as above and at the end prints out
###the maximum and minimum of the numbers instead of the average.

def iterations2():

    largest = 0
    smallest = 0


    while True:        
            line = input('Enter a number: ')
            if line == 'done':   
                print (smallest, largest)
                break
           
            try: 
                value = float(line)              
                
                if value > largest:
                    largest = value
                
                elif smallest == 0 or value < smallest:
                    smallest = value        
                
            except:
                print('invalid input')


iterations2()






