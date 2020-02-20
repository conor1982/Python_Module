#Function to square brackets

def power(x ,y):
    ans = x
    y = y -1
    while y > 0:
        ans = ans * x
        y = y-1
    return ans


print(power(2,3))

def f(x):
    #ans = (100*power(x,2) + 10*power(x,3)) //100 - power(x,3) //10
    ans = power(x,2)
    return ans


f(2)

print(f(2))

import math

x = 14.5
print("The approx square root of",x,"is",round(math.sqrt(x),2))

print(math.floor(9.99))

import numpy

