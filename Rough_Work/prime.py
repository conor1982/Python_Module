#list variable

P = []

upper = 10


for i in range(2,upper):

    isprime = True

    for j in P:
        if i % j == 0:
            isprime = False

            break
    if isprime:
        P.append(i)

print(P)

#print(sum(P))

