#This program generates 10 random numbers
#prints them out
#then prints the top 3

#List used to store and
#manipulate numbers

import random

howmany = 00
tophowmany = 3
rangefrom = 0
rangeto = 100

numbers = []

for i in range(0,10):
    numbers.append(random.randint(rangefrom,rangeto))

print("{} random numbers\t {}".format(howmany,numbers))
print(howmany,"random numbers\t",numbers)

topones = numbers.copy()
topones.sort(reverse = True)
bottomones = numbers.copy()
bottomones.sort(reverse = False)

print(topones)
print(bottomones)

print("The top",tophowmany,"are:\t",topones[:3])
print("The bottom",tophowmany,"are:\t",bottomones[:3])