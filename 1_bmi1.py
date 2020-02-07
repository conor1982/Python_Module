#bmi calculator
#Enter Height: 

Height = float(input("Enter Height in CM: "))/100
Weight = float(input("Enter Weight in KG: "))

#Below takes input from variables above and does calculation
bmi = round((Weight/(Height*Height)),2)

#prints answer
print("Your BMI is",bmi)

