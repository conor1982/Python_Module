#Conor O'Riordan
#Weekly Task 2 BMI calculator

#while loop for error handling
#Ref: https://docs.python.org/3.1/tutorial/errors.html
#Ref: Topic 9: Errors lecture videos
while True:
    try:
        #Enter Height - user input 
        weight = float(input("Enter Weight (in KG): "))
        break

    #Error printed if non number entered as input   
    except ValueError:
        print("The input was not a valid number. Please try again!")


#while loop for error handling
#Ref: https://docs.python.org/3.1/tutorial/errors.html
#Ref: Topic 9: Errors lecture videos
while True:
    try:
        #Enter Weight - user input
        height = float(input("Enter Height (in CM): "))/100
        break

    #Error printed if not a number entered as input
    except ValueError:
        print("The input was not a valid number. Please try again!")
   
#Below takes input from variables above and does calculation
bmi = round((weight/(height*height)),2)

#prints answer
print("BMI is",bmi)

