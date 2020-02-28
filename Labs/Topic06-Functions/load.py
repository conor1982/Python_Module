import json

filename = '/Users/Oriordanc/Desktop/HDip/Programming/Python_Module/students.json'

def readdict():
    with open (filename) as f:
        return json.load(f)

somedict = readdict()

print(somedict)