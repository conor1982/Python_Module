filename = 'checker.txt'

def readnumber():
    with open(filename) as f:
        number = int(f.read())
        return number

def writenumber(number):
    with open(filename, 'wt') as f:
        f.write(str(number))

#main
num = readnumber()
num += 1
print("We have run this program",num,'times')
writenumber(num)