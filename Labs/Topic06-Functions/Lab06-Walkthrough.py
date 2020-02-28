
import json

students = []
filename = "/Users/Oriordanc/Desktop/HDip/Programming/Python_Module/students.json"

def writedict(obj):
    with open(filename,'wt') as f:
        json.dump(obj,f)

def readdict():
    with open(filename) as f:
        return json.load(f)

def displaymenu():
    print("MENU")
    print("\ta) Add Student")
    print("\tv) View Student")
    print("\ts) Save Student")
    print("\tl) Load File")
    print("\tq) Quit")
    choice = input("Select One:")
    return choice
def readmodules():
    modules = []
    currentname = input("\t\tEnter Module Name: ")
    while currentname != " ":
        module = {}
        module["Name"] = currentname
        module["Grade"] = int(input("\t\tEnter Grade: "))
        modules.append(module) 
    
        currentname = input("\t\tEnter new Module Name: (Blank to Quit)")
    
    return modules

def doAdd():
    student = {}
    student["Name"] = input("Enter Student name: ")
    student["Modules"] = readmodules()
    students.append(student)

def displaymodules(modules):
    print("\t\tName \tGrade")
    for module in modules:
        print("\t\t{}\t{}".format(module['Name'],module['Grade']))
    

def doView():
    print("All Students")
    for student in students:
        print("\t{}".format(student["Name"]))
        displaymodules(student["Modules"])

def doSave():
    writedict(students)
    print("students saved")

def doload():
    global students
    students = readdict()
    print("Students Loaded")


#main
choice = displaymenu()
while choice != "q":
    if choice == "a":
        doAdd()
    elif choice == "v":
        doView()
    elif choice == "s":
        doSave()
    elif choice == "l":
        doload()
    elif choice == "q":
        pass
    else:
        print("please select a, v or q")
    
    choice = displaymenu()

print(students)

