

def pnrange(x):
    lower = 2
    upper = x

    P = []

    for i in range(lower,x+1):

        isprime = True
        for j in P:
            if i % 2 != 0:
                isprime = True
            else: isprime = False    

            

        if isprime:
            P.append(i)
            
    return P

print(pnrange(11))

def pn(x):
    if x % 2 != 0:
        y = True
    else:
        y = False

    return print("yes",x,"is prime =",y)
            
pn(67)