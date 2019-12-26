####PFE (Severance) Chapter 10: Tuples
####
###

'''
txt = 'but soft what light in yonder window breaks'
words = txt.split()         ###split the string into individual words
t = list()                 ### t is a list
for word in words:          ###for every word in line of words
    t.append((len(word), word))   ###put the length of the word, and the word
    
t.sort (reverse = True)      ###put it in decreasing order

print (t)                   ###prints the list

res = list()
for length, word in t: ###for each item in the list including length of the word and the word itself
    res.append(word)  ###add the word to the list 'res'

print (res)          ###this function removes the number associated with each word in the list 't'
'''

''' Exercise 1: Revise a previous program as follows: Read and parse the "From" lines and pull
out the addresses from the line. Count the number of messages from each person using a dictionary.
After all the data has been read, print the person with the most commits by creating a list of 
(count, email) tuples from the dictionary. Then sort the list in reverse order and print out
the person who has the most commits.'''


dictionary = dict()

file=input('enter file name:')

fhand = open(file)


for line in fhand:            ###for every line in the file...
    
    words = line.split()      ###every word in the line is split, call it i
    for i in words:        ###for every word in the line "words"...
        if i == 'From':    ### if we see the word "from"....
            if words[1] not in dictionary:            ###the second word in the line aka email address, if it's not in the dictionary...         
                dictionary [words[1]] = 1             ###add it to the dictionary, give it a value of one.
            else:
                dictionary [words[1]] += 1          ### if the third word in the line is in the dictionary, add 1 to the existing value.

ls = list(dictionary.items())              ###ls is the list of the dictionary, in tuple form
l = list()                              ### l is the list we will add the values to

for key, val in ls:                     ###for each tuple in ls...
    l.append(key)                       ###add the email address of each tuple to the list 'l'

l.sort(reverse=True)                   ####sor the list in descending order from highest to lowest
print (l[:1])                         ###print the first email address in the list. It will be the email address with the most emails sent from the initial text file.


'''Exercise 2: This program counts the distribution of the hour of the day for each of the messages. 
You can pull the hour from the "From" line by finding the time string and then splitting that
string into parts using the colon character. Once you have accumulated the counts for each hour,
print out the counts, one per line, sorted by hour as shown below.'''


dictionary = dict()
file=input('enter file name:')

try:
    fhand = open(file)
except:
    print ('File cannot be found:', file)
    exit()

for line in fhand:            ###for every line in the file...    
    words = line.split()      ###every word in the line is split, call it i
    for i in words:        ###for every word in the line "words"...
        if i == 'From':    ### if we see the word "from"....
            email = words[5]        ###email is the fifth word in the line aka the time 
            email = email.split(':')  ###split the fifth word at the colon
            hour = email[0]         ### hour is equal to the first word after the split
            dictionary[hour] = dictionary.get(hour,0) + 1    ###concise function that adds 1 to the dictionary value
            
l = []                               ###new list we will add to

for hours, count in dictionary.items():         ###for key and value in the dictionary that is converted to list of tuples '.items' 
    l.append((hours, count))                  ###add the key and value to the list 'l'

l.sort()                                ###sort is by ascending order of keys aka hour email sent

for hours, count in l:                 ##print it as according to the text
    print (hours, count)


'''Exercise 3: Write a program that reads a file and prints the letters in decreasing order
of frequency. Your program should convert all the input to lower case and only counter the letters
a-z. Your program should not count spaces, digits, punctuation, or anything other than the letters 
a-z. Find text samples from several different languages and see how letter frequency varies between langauges.
Compare your results with the tables at https://wikipedia.org/wiki/Letter_frequencies.'''

import string 

letters = dict()
file=input('enter file name:')

try:
    fhand = open(file)
except:
    print ('File cannot be found:', file)
    exit()

for line in fhand:             
    line = line.translate((None, string.punctuation)) ###removes punctuation
    line = line.translate((None, string.digits))    ###removes numbers
    line = line.lower()                       ###everything is lower case
    line = line.split()                      ##splits the line into individual words
    for t in line:                       ###for every word in the line
        word = list(t)                 ####word is the list of all the words in the line
        for letter in word:           ###for every letter in the word
            letters[letter] = letters.get(letter,0) + 1

letterlist = []
for letter, count in letters.items():
    letterlist.append((count, letter))
    
letterlist.sort (reverse = True)
for count, letter in letterlist:
    print (letter, count)
    
    

    