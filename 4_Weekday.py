#Conor O'Riordan
#Week 5 Problem Sheet
#Output whether today is a weekday or not

import datetime as dt

#weekend day numbers
weekend = [4,5]

#is today day number in variable weekend

if dt.datetime.today().weekday() in weekend:
#if day number 4 0r 5 its the weekend    
    print("It is the weekend, yay!")

#if day number not in weekend variable prints weekday message
else:
    print("Yes, unfortunately today is a weekday.")
  
