#Conor O'Riordan
#Task 6 square root (Newton Method)
#Take positive floating point number as input
#Outputs approx of Square Root
#Call function sqrt


#while loop for error handling
#Ref: https://docs.python.org/3.1/tutorial/errors.html
#Ref: https://stackoverflow.com/questions/34244588/reject-negative-numbers-as-exceptions-in-python
#Ref: Topic 9: Errors lecture videos
while True:
    try:
        #Input for Number (Float Allowed)
        number_to_sqroot = float(input("Please enter a positive number:"))
        assert number_to_sqroot > 0
        break

    #Error printed if negative number entered as input
    except AssertionError:
        print('You entered a negative number. Please enter a positive number!!')

    #Error printed if non number entered as input   
    except ValueError:
        print("The input was not a positive integer. Please try again!")

#Square root function applying Newton Method
#Ref https://www.w3schools.com/python/python_functions.asp 
def sqrt_Func_Newton(x):

    #Approx start point dividing input number by 2
    approx = x/2
        
    #Loop while absolute of value of f(x) is greater or equal than 0.01
    #Ref https://www.youtube.com/watch?v=2158QbsunA8
    while abs(approx**2-x) >= 0.01:
        approx = approx - (approx**2 - x)/(2*approx)

    #Return approx number at end of loop rounded to 1 decimel place
    return round(approx,1)
    
#Print output message        
print("The square root of",number_to_sqroot,"is approx.",sqrt_Func_Newton(number_to_sqroot),"(using Newton Method).")       
