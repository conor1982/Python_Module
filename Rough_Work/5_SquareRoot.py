#Conor O'Riordan
#Take positive floating point number as input
#Outputs approx of Square Root
#Call function sqrt

num_to_sqroot = float(input("Enter positive Float Number:"))

def sqrt_func(x):
    ans = x ** 0.5
    return ans

#print(sqrt_func(num_to_sqroot))
#
num_guess = float(input("Enter Aprroximate Square Root Value (Positive Floast Number):"))

newton_method = (num_to_sqroot/num_guess+num_guess)/2

#print(newton_method)

while num_guess != sqrt_func(num_to_sqroot):
    if num_guess != sqrt_func(num_to_sqroot):
        print(newton_method)
        
    else:
        newton_method = (0.5 * (num_guess+num_to_sqroot/num_guess))
        
    
        
    
    