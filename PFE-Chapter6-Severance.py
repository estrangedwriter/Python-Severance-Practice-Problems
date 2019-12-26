# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 13:15:08 2019

@author: Jerom
"""

####PFE (Severance) Chapter 6: STRING SLICES
####
###

#fruit = 'banana'
#index = 0

#while index < len(fruit):
    #letter = fruit[index]
    #print(letter)
#    index = index + 1

###Exercise 1: Write a whle loop that starts at the last character in the string and works its way backwards
###to the first character in the string, printing each letter on a separate line, except backwards.
###
###
fruit = 'banana'

index = len(fruit)

for i in range(index):    
    letter = fruit[index-1]
    print (letter)    
    index = index - 1


###Exercise 2: Given that fruit is a string, what does fruit[:] mean?

print(fruit[:]) # banana. fruit[:] means the entire string.



#word = 'banana'
#count = 0
#for letter in word: 
#    if letter == 'a':
#        count = count + 1
###Exercise 3: Encapsulate this code in a function named count, and generalize it so that it accepts the string and the letter as
### arguments.
 
       
def count(word, letter):
    counter = 0

    for character in word:
        if character == letter:
            counter = counter + 1
    print(counter)

input_word = input('Enter the word: ')
input_letter = input('Enter the letter: ')

count(input_word, input_letter)

    
        
        
###Exercise 5: Take the following Python code that stores a string:   
###   str = 'X-DSPAM-Confidence:0.8475'
### Use find and string slicing to extract the portion of the string after the colon
### character and then use the float function to convert the extracted string into
### a floating point number.    
    

string = 'X-DSPAM-Confidence:0.8475'
     
integ = str.find (':') 


numberz = float(string[integ+1:])

print (numberz)

















