

with open('/Users/Oriordanc/Desktop/HDip/Programming/Python_Module/The_Catcher_in_the_Rye.txt','r') as f:
    readfile = f.read()
    words = readfile.split()
    letterlower = [list(line.rstrip().lower()) for line in words]
    letter =  [list(line.rstrip()) for line in words]
    
print(letterlower)

freq = {}

for line in letter:
    for char in line:
        if char in freq:
            freq[char] +=1
        else:
            freq[char] = 1

elower = freq['e']
eupper = freq['E']
total_letter_e = elower + eupper

print(total_letter_e)

freqlowercase = {}

for lcase in letterlower:
    for lower in lcase:
        if lower in freqlowercase:
            freqlowercase[lower] +=1
        else:
            freqlowercase[lower] = 1

print(freqlowercase['e'])
