#normalisig string

rawstring = input("Please input a string:")
normalisedstring = rawstring.strip().lower()

lenofrawstring = len(rawstring)
lenofnormalisedstring = len(normalisedstring)

print("That string normalised is: {}".format(normalisedstring))
print("We reduced the input string from {} to {} charcters".format(lenofrawstring,lenofnormalisedstring))



