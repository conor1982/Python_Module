#Another way of BMI calculation
#Creates a re-usable function to calculate BMI

def bmi(h,w):
    result = w/((h*h)/100)
    return round(result,2)

#function has two parameters: Height and Weight
print(bmi(180,65))