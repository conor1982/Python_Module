import math

def isprime(i):
  # Loop through all values j from 2 up to but not including i.
  for j in range(2, math.floor(math.sqrt(i))):
    # See if j divides i.
    if i % j == 0:
      # If it does, i isn't prime so exit the loop and indicate it's not prime.
      return False
  return True


print(isprime(100))

def KM_Converter(x):
    km = x * .621371
    return km

def Miles_Converter(x):
    miles = x / .621371
    return miles

print(KM_Converter(5))
print(Miles_Converter(5))

