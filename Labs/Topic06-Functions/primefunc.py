

def pnrange(x):
    lower = 2
    upper = x

    L = []

    for i in range(lower,x):

        isprime = True
        for j in L:
            if i % 2 != 0:
                isprime = True

                break

        if isprime:
            L.append(i)
            
    return L

print(pnrange(10))

def pn(x):
    if x % 2 != 0:
        x = True
    else:
        x = False

    return x
            
print(pn(4))