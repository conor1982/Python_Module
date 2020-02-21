#Conor O'Riordan
#Take positive floating point number as input
#Outputs approx of Square Root
#Call function sqrt

#Input for Number (Float Allowed)
number_to_sqroot = float(input("Please enter a positive number:"))
#num_guess = float(input("Enter Aprroximate Square Root Value (Positive Floast Number):"))

#Squar Root Function (Not using Newton Method)
def sqrt_func_1(x):
#Variable Y = Input Number to the power of 0.5
    y = x**0.5
    ans = y
#Return Ans variable and Round to 1 place
    return round(ans,1)




#Square root function applying Newton Method
def sqrt_Func_Newton(x):
#Approx start point dividing input number by 2
    approx = x/2
#Loop while absolute of approx to the power of 2 less input number is greater or equal than 0.01
    while abs(approx**2-x) >= 0.01:
        approx = approx - (approx**2-x)/(2*approx)
#Return approx number at end of loop
    return round(approx,1)
        
        
print("The square root of",number_to_sqroot,"is approx.",sqrt_func_1(number_to_sqroot),"(not using Newton Method).")

print("The square root of",number_to_sqroot,"is approx.",sqrt_Func_Newton(number_to_sqroot),"(using Newton Method).")       



    
