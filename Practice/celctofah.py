
def to_Fahrenheit(c):
    FH = (c*9)/5+32
    return round(FH,2)

def to_Celcius(f):
    C = (f-32)*5/9
    return round(C,2)

print(to_Fahrenheit(21))
print(to_Celcius(60))  