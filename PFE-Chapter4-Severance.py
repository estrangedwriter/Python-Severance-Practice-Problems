# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 22:06:17 2019

@author: Jerom
"""

####PFE (Severance) Chapter 4: FUNCTIONS
####
###
###Exercise 1: Run the program on your system and see what numbers you get. Run the program more than once and see what numbers you get.

#import random
#for i in range (10):
#    x=random.random()
#    print (x)
        



#Exercise 6: Rewrite your pay computation with time-and-a-half for over-time and create a function called computepay which takes two parameters, (Hours and Rate)        


Hours = 0
Rate = 0    

def computepay(Hours, Rate):

    if Hours  <=40: 
        Pay = Hours * Rate

    else:
        Overtime = 1.5*Rate
        Pay = (40 * Rate) + (Overtime * (Hours - 40))

    print('Pay:', Pay)


#Exercise 7: Rewrite the grade program from the previous chapter using a function called computegrade that takes a score as its parameter and 
#returns a grade as a string.

def computegrade(score):  
    print ('>= 0.9     A\n>= 0.8     B\n>= 0.7     C\n>= 0.6     D\n < 0.6     F')
    try:
       if score >1:
            print('Bad score')
    
       elif score >=0.9:
            print (str('A'))
            
       elif score >=0.8:
            print(str('B'))
        
       elif score>=0.7:
            print(str('C'))
            
       elif score>=0.6:
            print(str('D'))
            
       elif score <0.6:
            print(str('F'))
            
       elif score < 0:
            print('Bad score')    
            
    except NameError:
            print('Bad score')
        
      
        