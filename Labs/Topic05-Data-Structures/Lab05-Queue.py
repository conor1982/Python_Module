#Lab5
#Queue to reduces 10 random numbers
#Pop command

import random
queue = []
numberOfnumbers = 10
rangeto = 100

for n in range(0,numberOfnumbers):
    queue.append(random.randint(0,rangeto))

print("Queue is",queue)

while len(queue) != 0:
    current_number = queue.pop(0)
    print("current number is:",current_number,"and the queue is",queue)

