students = []

def displayMenu():

    print("What would you like to do?")
    print("\t(a) Add new student: ")
    print("\t(v) View students: ")
    print("\t(q) Quit: ")
    choice = input("Type one letter (a/v/q): ").strip()
    return choice
#test the function

def doAdd():
    currentstudent = {}
    currentstudent["name"]=input("Enter Name: ")
    currentstudent["modules"]= readmodules()
    students.append(currentstudent)

def readmodules():
    modules = []
    modulesName = input("\tEnter the first module name (blank to quit): ").strip()

    while modulesName != "":
        module = {}
        module["name"] = modulesName
        module["grade"] = int(input("Enter Grade: "))
        modules.append(module)

        modulesName = input("\tEnter next module name (blank to quit: )").strip()

    return modules 

def displayModules(modules):
     print("\tName     \tGrade")
     for module in modules:
         print("\t{}\t{}".format(module["name"], module["grade"]))

def doView():
    for currentstudent in students:
        print(currentstudent["name"])
        displayModules(currentstudent["modules"])
    

choice = displayMenu()
while (choice != 'q'):
    if choice == 'a':
        doAdd()
    elif choice == 'v':
        doView()
    elif choice != 'q':
        print("\n\nPlease select a, v or q")
    choice = displayMenu()



print(students)
