#numbers divisible by 7 and 5
#between a range
#return nums

L = []

for i in range (1500,2701):
    if (i % 7 == 0) and (i % 5== 0):
        L.append(i)

print(L)


