#Conor O'Riordan
#secondstringtask
#to reverse the string of recieved user input"

#Ref https://www.w3schools.com/python/python_howto_reverse_string.asp
sentence = input("Please enter a sentence: ")

#negative means start at end of string at position 0 and move with step -2, which is two steps backwards
print(sentence[::-2])