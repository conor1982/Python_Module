#Program that reads in students
#unitl ther user enters blank
#and then prints them out again

students = []

firstname = input("Enter first name (enter blank to quit): ").strip()
while firstname != "" :
    student = {}
    student["firstname"] = firstname
    lastname = input("enter lastname: ").strip()
    student["lastname"] = lastname
    students.append(student)
    #next studentg
    firstname = input("Enter first name (enter blank to quit): ").strip()

print("Here are the students you entered")
for i in students:
    print(i["firstname"],i["lastname"])

