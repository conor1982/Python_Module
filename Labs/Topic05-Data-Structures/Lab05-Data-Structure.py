student = {
    "name" : "Mary",
    "modules" : [
        {
            "course name" : "Geography",
            "grade" : 78
        },
        {   "course name" : "History",
            "grade" : 67
        
        },
        {   "course name" : "Science",
            "grade" : 43
        }
    ]
}




print ("Student: {}".format(student["name"]))
for module in student["modules"]:
    print("\t {} \t: {}".format(module["course name"], module["grade"]))
