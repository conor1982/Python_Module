#Conor O'Riordan
#Weekly Task 2 BMI calculator

#while loop for error handling
#Ref: https://docs.python.org/3.1/tutorial/errors.html
#Ref: https://stackoverflow.com/questions/34244588/reject-negative-numbers-as-exceptions-in-python
#Ref: Topic 9: Errors lecture videos
while True:
    try:
        #Enter Height - user input 
        weight = float(input("Enter Weight (in KG): "))
        assert weight > 0
        break
    
    #Error printed if negative number entered as input
    except AssertionError:
        print('You entered a negative number. Please enter a positive number!!')

    #Error printed if non number entered as input   
    except ValueError:
        print("The input was not a valid number. Please try again!")


#while loop for error handling
#Ref: https://docs.python.org/3.1/tutorial/errors.html
#Ref: https://stackoverflow.com/questions/34244588/reject-negative-numbers-as-exceptions-in-python
#Ref: Topic 9: Errors lecture videos
while True:
    try:
        #Enter Weight - user input
        height = float(input("Enter Height (in CM): "))/100
        assert height > 0
        break

    #Error printed if negative number entered as input
    except AssertionError:
        print('You entered a negative number. Please enter a positive number!!')

    #Error printed if not a number entered as input
    except ValueError:
        print("The input was not a valid number. Please try again!")
   
#Below takes input from variables above and does calculation
bmi = round((weight/(height*height)),2)

#prints answer
print("BMI is",bmi)

