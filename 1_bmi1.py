#bmi calculator
#Enter Height: 

Weight = float(input("Enter Weight (in KG): "))
Height = float(input("Enter Height (in CM): "))/100

#Below takes input from variables above and does calculation
bmi = round((Weight/(Height*Height)),2)

#prints answer
print("BMI is",bmi)

