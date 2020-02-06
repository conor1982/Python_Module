#Input out student percentage
#and return and print grade
#according to result

percentage = float(input("Enter student percentage result: "))

if round(percentage) < 0 or round(percentage) > 0:
    print("Please enter number between 0 and 100")

elif round(percentage) < 40:
    print("Fail")

elif round(percentage) < 50:
    print("Pass")

elif round(percentage) < 60:
    print("Merit 2")

elif round(percentage) < 70:
    print("Merit 1")

else:
    print("Distinction")
