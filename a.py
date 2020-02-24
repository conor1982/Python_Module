
number_to_sqroot = 14.5
#Square root function applying Newton Method
def sqrt_Func_Newton(x):
#Approx start point dividing input number by 2
    approx = x/2
    fx = x/2**2-x
    fprime = 2*x/2
        
#Loop while absolute of value of f(x) is greater or equal than 0.00001
    while abs(fx) >= 0.00001:
        approx = approx - (fx)/(fprime)

#Return approx number at end of loop
    return round(approx,11)
    

print(sqrt_Func_Newton(number_to_sqroot)) 