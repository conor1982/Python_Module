#Conor O'Riordan
#Week 5 Problem Sheet
#Output whether today is a weekday or not

#Imort Datetime module
import datetime as dt

#weekend day numbers in list
weekend = [5,6]

#is today day number in variable weekend

if dt.datetime.today().weekday() in weekend:
#if day number 5 0r 6 its the weekend    
    print("It is the weekend, yay!")

#if day number is 4 add message about it being Friday
elif dt.datetime.today().weekday() == 4:
    print("Its is a weekday but it at least it is Friday!!!!")

#if day number not in weekend variable prints weekday message
else:
    print("Yes, unfortunately today is a weekday.")
  