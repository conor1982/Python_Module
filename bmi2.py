def bmi(h,w):
    result = w/((h*h)/100)
    return round(result,2)

#height = float(input("Enter Height in CM: "))
#weight = float(input("Enter Weight in KG: "))

#print("Your BMI is",bmi(weight,height))


print(bmi(180,65))