#Conor O'Riordan
#Return total amount of times a letter
#occurs in a text

#open file from directory
#this file on my desktop
#book name is The Catcher in the Rye
with open('checker.txt','r') as f:
    
    #reads out the full text
    readfile = f.read()

    #variable splits white space between words in text 
    words = readfile.split()
    
    #variable loops through words variable and splits string into a list with seperate letters 
    letter =  [list(line.strip()) for line in words]
print(len(words))
print(len(letter))  
#input letters to main program
u = input("enter uppercase letter: ")
ll = input("enter lower case letter ")

#reads in input values 
upperletter = u
lowerletter = ll

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
lower = freq[lowerletter]
upper = freq[upperletter]
total_letter = lower + upper

#prints out total
print("There are a total of",total_letter,'of letter',lowerletter,"in the book. The breakdown is:",lower,"lower case and",upper,"upper case")

print(freq)

f.close()