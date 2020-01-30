#print random fruit

import random

fruits = ('apple', 'orange', 'banana','pear')

index = random.randint(0,len(fruits)-1)

fruits = fruits[index].capitalize()

print("A random Fruit: {} ".format(fruits))