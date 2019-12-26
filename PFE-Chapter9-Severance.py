####PFE (Severance) Chapter 9: Dictionaries
####
###

'''
Exercise 1: Download a copy of the file www.py3e.com/code3/words.txt

Write a program that reads the words in words.txt and stores them as 
keys in a dictionary. It doesn't matter what the values are. Then you can use the
in operator as a fast way to check whether a string is in the dictionary.
'''

dictionary = dict()

file=input('enter file name:')

fhand = open(file)
    
for line in fhand:
    words = line.split()
    for word in words:
        dictionary [word] = 'values'
        


    
'''
Exercise 2: Write a program that categorizes each mail message by which day of the 
week the commit was done. To do this look for lines that start with "From", 
then look for the third word and keep a running count of each of the days of the
week. At the end of the program print out the contents of your dictionary 
(order does not matter).
'''

dictionary = dict()

file=input('enter file name:')

fhand = open(file)


for line in fhand:            ###for every line in the file...
    
    words = line.split()      ###every word in the line is split, call it i
    for i in words:        ###for every word in the line "words"...
        if i == 'From':    ### if we see the word "from"....
            if words[2] not in dictionary:            ###the third word in the line, if it's not in the dictionary...         
                dictionary [words[2]] = 1             ###add it to the dictionary, give it a value of one.
            else:
                dictionary [words[2]] += 1          ### if the third word in the line is in the dictionary, add 1 to the existing value.
            
print (dictionary)


            
'''
Exercise 3: Write a program to read through a mail log, build a histogram using a dictionary
to count how many messages have come from each email address, and print the dictionary.
'''

dictionary = dict()

file=input('enter file name:')

fhand = open(file)


for line in fhand:            ###for every line in the file...
    
    words = line.split()      ###every word in the line is split, call it i
    for i in words:        ###for every word in the line "words"...
        if i == 'From':    ### if we see the word "from"....
            if words[1] not in dictionary:            ###the second word in the line, if it's not in the dictionary...         
                dictionary [words[1]] = 1             ###add it to the dictionary, give it a value of one.
            else:
                dictionary [words[1]] += 1          ### if the third word in the line is in the dictionary, add 1 to the existing value.
                
print (dictionary)


'''
Exercise 4: Add code to the above program to figure out who has the most messages in the file.
After all the data has been read and the dictionary has been created, look through the dictionary
using a maximum loop (see Chapter 5: Maximum and minimum loops) to find who has the most 
messages and print how many messages the person has.
'''

largest = None

for key in dictionary:

    if largest is None or dictionary[key] > largest:
        largest = dictionary[key]
        
print (key, largest)



'''
Exercise 5: This program records the domain name (instead of the address) where the message
was sent from instead of who the mail came from (i.e., the whole email address). At the 
end of the program, print out the contents of your dictionary.
'''

fname = input('Enter file name: ')

try:
	fhandle = open(fname)
except:
	print ('File cannot be opened:', fname)
	exit()

emails = dict()
for line in fhandle:
	if line.startswith('From '):
		line = line.split()
		email = line[1]
		email = email.split('@')
		domain = email[1]
		emails[domain] = emails.get(domain,0) + 1
print (emails)




