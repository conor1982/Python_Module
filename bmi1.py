#bmi calculator

Height = float(input("Enter Height in CM: "))/100
Weight = float(input("Enter Weight in KG: "))

bmi = round((Weight/(Height*Height)),2)

print("Your BMI is",bmi)

