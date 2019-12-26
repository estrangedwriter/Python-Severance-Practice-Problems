####PFE (Severance) Chapter 11: Regular Expressions
####
###

'''Exercise 1: Write a simple program to simulate the operation of the grep command on Unix. Ask
the user to enter a regular expression and count the number of lines that matched the regular expression.'''

def grep():    
    import re

    try:
        ls = []
        counter = 0
        file=input('enter file name:')
        fhand = open(file)
        R = input('Enter expression:')    

        for line in fhand:
            line = line.rstrip()
            if re.search(R, line):
                ls.append(line)
                counter = counter + 1
                print (file,'had', counter, 'lines that matched the expression',R,'.' )      

    except: 
        print ('Cannot find file. Please try again.')


'''Exercise 2: Write a program to look for lines of the form: 
    
    New Revision: 39772

Extract the number from each of the lines using a regular expression and the findall() method. 
Compute the average of the numbers and print out the average.'''

def ex():      
    import re
    ls = []
    try:
        file=input('Enter file name:')
        fhand = open(file)
        for line in fhand:
            line = line.rstrip()
            x = re.findall('Revision:.([0-9.]+)',line)
            if len(x) > 0: 
                for number in x:
                    number = float(number)
                    ls.append(number)                    
        print ('The average of the file is as follows:',sum(ls)/len(ls))                
    except: 
        print ('Cannot find file. Please try again.')
        
        
        