#Conor O'Riordan
# Write a program that asks the user to input any positive integer and outputs the successive values of the following calculation.
# At each step calculate the next value by taking the current value and
# if it is even, divide it by two, but if it is odd, multiply it by three and add one.
# Have the program end if the current value is one.

#Version includes print text to describe number input
#Version includes print text to describe number output

#Enter positive number
pos_int = int(input("Please enter a positive integer:"))

#While Loop
#If Statement to calculate based on Odd or Even Number
 
while pos_int > 1:
    if pos_int % 2 == 0:
        print(round(pos_int),"is even so divide by two. This gives:",round(pos_int/2))
        pos_int = pos_int/2
    else:
        print(round(pos_int),"is odd so multiply by three and add one. This gives:",round((pos_int*3)+1))
        pos_int = (pos_int*3)+1

#Prints when program completes
print("We have now reached",round(pos_int),"!!!! Programme completed")