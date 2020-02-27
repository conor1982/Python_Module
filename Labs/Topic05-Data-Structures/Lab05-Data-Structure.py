student = {
    "name" : "Mary",
    "secondname": 'spencer',
    "modules" : [
        {
            "course name" : "Geography",
            "grade" : 78,
            "level" : 'h'
            
        },
        {   "course name" : "History",
            "grade" : 67,
            "level" : "h"
            
        },
        {   "course name" : "Science",
            "grade" : 43,
            "level" : 'o'
        },
        {   "course name" : "English",
            "grade" : 85,
            "level" : 'h'
        }
    ]
}




print ("Student: {} {}".format(student["name"],student['secondname']))
for module in student["modules"]:
    print("\t {} \t {} \t{} :".format(module["course name"], module["grade"],module["level"]))
for fname in student['name']:
    print(fname, end ='')
