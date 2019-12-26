# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 16:54:06 2019

@author: Jerom
"""

####PFE (Severance) Chapter 7: FILES
####
###


'''Exercise 1: Write a program to read through a file and print the contents of the 
### file (line by line) all in upper case. Executing the program will look as follows:


###mbox-short.txt'''


fname = input('Enter file name:')

fhand = open (fname)

count = 0

for line in fhand:
    count = count + 1
    
    line = line.rstrip()
    
    line1= str(line)
    line2 = str.upper(line1)
    
    print (line2)
        
    if count > 4:
        break    
    

'''Exercise 2: Write a program to prompt for a file name, and then read through the file and look for lines of the form:
    

    X-DSPAM-Confidence: 0.8475
    
    When you encounter a line that starts with "X-DSPAM-Confidence" pull apart the line to extract the floating-point number on the line.
    Count these lines and then compute the total of the spam confidence values from these lines. When you reach the end of the file,
    print out the average spam confidence. '''
    
    

fname = input('Enter file name:')

fhand = open (fname)

total = 0
count = 0

for line in fhand:
    
    if line.startswith('X-DSPAM-Confidence:'):
        line=line.rstrip()
        
        if line.find(': 0.') == -1: continue
        
        integ = line.find (':')     
        numberz = float(line[integ+1:])
        total = numberz + total
        count = count + 1
        average = total / count
        

print ('Average spam confidence:', average)
        

'''Exercise 3: Sometimes when programmers get bored or want to have a bit of fun, they add a harmless Easter Egg to their program.
Modify the program that prompts the user for the file name so that it prints a funny message when the user types in the exact file name
"na na boo boo". The program should behave normally for all other files which exist and don't exist. Here is a sample execution of the program:'''

try:
    fname = input('Enter file name:')

    if fname == ('na na boo boo'):
        print ("NA NA BOO BOO TO YOU - You have been punk'd!")
    
    else:    
        fhand = open (fname)

        count = 0
    
        for line in fhand:
            count = count + 1
        
        print ('There were', count, 'subject lines in', fname)

except: 
    print ('File cannot be opened:', fname)
    
