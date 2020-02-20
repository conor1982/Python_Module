#Conor O'Riordan
#Take positive floating point number as input
#Outputs approx of Square Root
#Call function sqrt

import math
#formula test

#num_to_sqroot = 14.5
#approx_num = 3.8078865529319543

#formula_attempt = (num_to_sqroot/approx_num+approx_num)/2
    

#print(formula_attempt)

def sqrt_function(x):
    approx = x ** 0.5
    return round(approx,1)

print(sqrt_function(10544.5))

print(round(math.sqrt(10544.5),1))
