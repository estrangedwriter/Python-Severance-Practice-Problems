####PFE (Severance) Chapter 8: LISTS
####
###

''' Exercise 1: write a function called chop that takes a list and modifies it, removing the first and last elements, and returns None.
Then write a function called middle that takes a list and returns a new list that contains all but the first and last elements.'''



def chop():
    
    counter = 0
    a = input('Please enter your list:')
    s = a.split()
    for i in s:
        counter = counter + 1        
    
    s[0] = None
    s[counter-1] = None
    print (s)
     
chop()


def middle():
    
    counter = 0 
    a = input('Please enter your list:')
    s = a.split()
    
    for i in s: 
        counter = counter + 1
        
        
    s.pop(0)
    s.pop(counter-2)
    print (s)

middle()



'''Exercise 4: Download a copy of the file www.py4e.com/code3/romeo.txt. Write a program to open the file romeo.txt and read it line by line.
For each line, split the line into a list of words using the split function. For each word, check to see if the word is already in a list. If the 
word is not in the list, add it to the list. When the program completes, sort and print the resulting words in alphabetical order.'''

###file name: romeo.txt




file=input("ENTER FILE : ")

fhand = open(file)

t = list()

for line in fhand:
        words = line.split()
        for word in words:
            if word not in t:
                t.append(word)

t.sort()
print(t)



'''Exercise 5: Write a program to read through the mail box data and when you find line that starts with "From", you will split the line 
into words using the split function. We are interested in who sent the message, which is the second word on the From line". '''



file = input('Enter file name:')

fhand = open(file)

counter = 0

for line in fhand:                    ###for every line in the file....
    
    words = line.split()             ### words is equal to a line that is split
        
    for word in words:               ### for every word in 'words' (each line)
        if word == 'From':           ###if a word is equal to 'From'
            print (words[1])         ###print the second word of each line ('words')
            counter = counter + 1   ###if there is a 'From' in the line, add 1 to the counter
    
print ('There were ', counter,' lines in the file with From as the first word')



'''Exercise 6: Rewrite the program the prompts the user for a list of numbers and prints out the maximum and minimum of the numbers
at the end when the user enters "done". Write the program to store the numbers the user enters in a list and use the max()
and min() functions to computer the maximum and minimum numbers after the loop completes.'''

    
t = []
counter = 0
    
while True:
    a = input('Enter a number:')
    t.append(a)
    counter = counter + 1
    
    if a == "done":
        t.pop(counter-1)
        print ('Maxmum: ',max(t))
        print ('Minimum: ',min(t))
        break
        

