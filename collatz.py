#Conor O'Riordan
#Task 4 collatz
# Write a program that asks the user to input any positive integer and outputs the successive values of the following calculation.
# At each step calculate the next value by taking the current value and
# if it is even, divide it by two, but if it is odd, multiply it by three and add one.
# Have the program end if the current value is one.


#while loop for error handling
#Ref: https://docs.python.org/3.1/tutorial/errors.html
#Ref  https://stackoverflow.com/questions/34244588/reject-negative-numbers-as-exceptions-in-python
#Ref: Topic 9: Errors lecture videos
while True:
    try:
        #Enter positive number 
        pos_int = int(input("Please enter a positive integer: "))
        assert pos_int > 0
        break

    #Error printed if negative number entered as input
    except AssertionError:
        print('You entered a negative number. Please enter a positive number!!')
        
    #Error printed if non number entered as input   
    except ValueError:
        print("The input was not a positive integer. Please try again!")


#While Loop
#Ref: https://www.tutorialspoint.com/python/python_while_loop.htm
#Ref: https://www.w3schools.com/python/python_while_loops.asp
while pos_int > 1:
    
    #prints post_int once greater than 1. If post_int == 1 then just prints 1 and loop finished
    print(round(pos_int), end = " ")

    #If Statement to calculate based on Odd or Even Number
    #check if num is even or odd using modulo (%)
    #if even divide by 2
    if pos_int % 2 == 0:
        pos_int = pos_int/2

    #else has to be odd
    # number multiplied by 3 and a ond added   
    else:
        pos_int = (pos_int*3)+1
        
#Prints result of the loop once post_int greater than 1
print(round(pos_int), end = " ")



    
    

    

  