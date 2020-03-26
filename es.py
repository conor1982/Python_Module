#Conor O'Riordan
#Weekly Task 7
#Read in a file from a Command line argument
#Return total amount of times a letter (case sensitive) appears in a file
#Program has an input option to select which letter the user wants a return for 


# SYS module used for command line arguments
#Ref https://www.tutorialspoint.com/python/python_command_line_arguments.htm
import sys

#error handling - more detail in comments above exceptions 
#Ref http://hplgit.github.io/primer.html/doc/pub/input/._input-solarized007.html

try:
    #takes an argument from the command line at position 2 i.e Filename
    filename = sys.argv[1]
    
    #opens file in readmode
    #using with means no nead to have f.close() at the end
    with open(filename,'r') as f:
         
         #splits file into individual words
         #Ref https://docs.python.org/3.3/tutorial/inputoutput.html
         readfile = f.read().split()

         #for loop to create variable that splits the individual words into a list with letters/characters split
         #Ref https://www.w3schools.com/python/ref_string_strip.asp
         letter =  [list(line.strip()) for line in readfile]


#Ref http://hplgit.github.io/primer.html/doc/pub/input/._input-solarized007.html
#error handling if command line argument left blank
except IndexError:
    print('No File entered on command line')
    
    #system exit when an exception or error  occurs
    sys.exit(1)

#both the following needed for readfile and letter variables above
#error handling if incorrect filename with extension entered on command line
except NameError:
    print('File not Found')
    sys.exit(1)

#error handling if incorrect name entered on command line    
except FileNotFoundError:
    print('File not Found')
    sys.exit(1)

#input letters to main program
letter_input = input("enter letter: ")

#dictionary for a count of each letter and charcter in file
# Ref https://stackoverflow.com/questions/41970992/appending-values-to-dictionary-in-for-loop
freq = {}

#for loop for each list in letter
for line in letter:
    #loops through characters in each list from letter variable
    for char in line:
        if char in freq:
            #adds 1 to each time a character is present
            freq[char] +=1
        else:
            #if character is only present once give it a value of 1
            freq[char] = 1


#print count of charcter frequency by passing input value to dictionary 
print(freq[letter_input])


