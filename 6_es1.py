#Conor O'Riordan
#Return total amount of times a letter
#occurs in a text

#open file from directory
#this file on my desktop
#book name is The Catcher in the Rye
with open('/Users/Oriordanc/Desktop/HDip/Programming/Python_Module/Moby_Dick.txt','r') as f:
    
    #reads out the full text
    readfile = f.read()

    #variable splits white space between words in text 
    words = readfile.split()
    
    #variable loops through words variable and splits string into a list with seperate letters 
    letter =  [list(line.strip()) for line in words]
   
#input letters to main program
letter_input = input("enter letter: ").lower()


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

f.close()