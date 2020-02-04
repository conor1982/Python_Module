# Write a program that asks the user to input any positive integer and outputs the successive values of the following calculation.
# At each step calculate the next value by taking the current value and
# if it is even, divide it by two, but if it is odd, multiply it by three and add one.
# Have the program end if the current value is one.

#pos_num = int(input("Please enter a positive integer:"))

pos_int = int(input("Please enter a positive integer:"))

while pos_int > 1:
    if pos_int % 2 == 0:
        print(pos_int,"is even so divide by two. This gives:",round(pos_int/2))
        pos_int = pos_int/2
    else:
        print(pos_int,"is odd so multiply by three and add one. This gives:",round((pos_int*3)+1))
        pos_int = (pos_int*3)+1

print("We have now reached 1. Programme completed")

    
    

    

  