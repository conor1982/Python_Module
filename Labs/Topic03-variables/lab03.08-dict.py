currentbook = {"Title": "Harry Potter", "Author": "JK Rowling", "Price": 12}

print(currentbook)

print(currentbook["Author"])

currentbook["ISBN"] = "1234"

print("the current book has these values:") 
for value in currentbook.values():
      print(" => {}".format(value))