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
    return round(ans,10)




#Square root function applying Newton Method
def sqrt_Func_Newton(x):
#Approx start point dividing input number by 2
    approx = x/2
#Loop while absolute of value of f(x) is greater or equal than 0.00001
    while abs(approx**2-x) >= 0.00001:
        approx = approx - (approx**2 - x)/(2*approx)
#Return approx number at end of loop
        
    return round(approx,10)
        
        
print("The square root of",number_to_sqroot,"is approx.",sqrt_func_1(number_to_sqroot),"(not using Newton Method).")

print("The square root of",number_to_sqroot,"is approx.",sqrt_Func_Newton(number_to_sqroot),"(using Newton Method).")       



    
