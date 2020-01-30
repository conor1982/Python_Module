#divide 2 numbers

x = int(input("Enter first number :"))
y = int(input("Enter second number :"))

answer = int(x/y)
remainder = x % y

print("{} divided by {} is {} with a remainder of {}".format(x,y,answer,remainder))

