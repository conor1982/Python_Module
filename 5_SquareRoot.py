#Conor O'Riordan
#Take positive floating point number as input
#Outputs approx of Square Root
#Call function sqrt

num_to_sqroot = float(input("Enter positive Float Number:"))
num_guess = float(input("Enter Aprroximate Square Root Value (Positive Floast Number):"))


def sqrt_func(x):
    y = x**0.5
    ans = y
    return ans

#print(sqrt_func(14.5))

#newton_method = (num_to_sqroot/num_guess+num_guess)/2
#print(newton_method)

while abs(num_guess**2-num_to_sqroot) >= 0.01:
    num_guess = num_guess - (num_guess**2-num_to_sqroot)/(2*num_guess)
    print(num_guess)
    
