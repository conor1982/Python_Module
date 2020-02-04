upper = 11
lower = 1

print("prime numbers between",lower,"and",upper,"are:")

for i in range(lower,upper):
    if i == 1:
        print("1 is not a prime number")
    else:
        if i % 2 != 0:
            print(i,"is a prime number between",lower,"and",upper)
