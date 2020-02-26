

with open('/Users/Oriordanc/Desktop/HDip/Programming/Python_Module/The_Catcher_in_the_Rye.txt','r') as f:
    readfile = f.read()
    words = readfile.split()
    #letterlower = [list(line.rstrip().lower()) for line in words]
    letter =  [list(line.rstrip()) for line in words]
    
#print(letterlower)
upperletter = 'E'
lowerletter = 'e'

freq = {}

for line in letter:
    for char in line:
        if char in freq:
            freq[char] +=1
        else:
            freq[char] = 1

lower = freq[lowerletter]
upper = freq[upperletter]
total_letter = lower + upper

#print(total_letter_e)

#freqlowercase = {}

#for lcase in letterlower:
    #for lower in lcase:
    #    if lower in freqlowercase:
   #         freqlowercase[lower] +=1
  #      else:
 #           freqlowercase[lower] = 1

#total_e = freqlowercase[lowerletter]


print("There are a total of",total_letter,"in the book. The breakdown is:",lower,"lower case and",upper,"upper case")

#print("Both methods returning same value:",total_letter == total_e)
