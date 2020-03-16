#Conor O'Riordan
#Return total amount of times a letter
#occurs in a text

#open file from directory
#this file on my desktop
import sys

#def hello(a,b):
 #   print("hello and that's your sum:", a + b)

#if __name__ == "__main__":
   # a = int(sys.argv[1])
   # b = int(sys.argv[2])
   # hello(a, b)


filename = sys.argv[0]

import os
import sys



with open(filename,'r') as f:
    readfile = f.read()
    words = readfile.split()
    letter =  [list(line.strip()) for line in words]

#input letters to main program
letter_input = input("enter letter: ")


#reads in input values 
letter_to_count = letter_input



#dictionary for a count of each letter 
freq = {}

#loop to return count of each letter
for line in letter:
    for char in line:    
        if char in freq:
            #adds 1 to each time a character is present
            freq[char] +=1
        else:
            #if character is only present once give it a value of 1
            freq[char] = 1

#count of charcter frequency
total_occurence = freq[letter_to_count]
print(total_occurence)

#prints out total

#print(total_occurence,letter_to_count)


#f.close()