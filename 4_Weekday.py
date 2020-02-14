#Conor O'Riordan
#Week 5 Problem Sheet
#Output whether today is a weekday or not

import datetime as dt

#weekend day numbers
weekend = [5,6]
Fri = 4

#is today day number in variable weekend

if dt.datetime.today().weekday() in weekend:
#if day number 4 0r 5 its the weekend    
    print("It is the weekend, yay!")

elif dt.datetime.today().weekday() == 4:
    print("Its is a weekday but it at least it is Friday!!!!")

#if day number not in weekend variable prints weekday message
else:
    print("Yes, unfortunately today is a weekday.")
  
