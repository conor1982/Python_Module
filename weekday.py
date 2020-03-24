#Conor O'Riordan
#Week 5 Task Weekday
#Output whether today is a weekday or not

#Imort Datetime module
import datetime as dt

#weekend day numbers in list
weekend = [5,6]

#variable that returns number value for current day based on time program ran 0 = Monday.... 6 = Sunday
today = dt.datetime.today().weekday()

#if statement to see if today is weekday 5 or 6 (weekend)
if today in weekend:
    print("It is the weekend, yay!")

#elif day number is 4 add message about it being Friday
elif today == 4:
    print("Its is a weekday but it at least it is Friday!!!!")

#if day number not in weekend variable prints weekday message
else:
    print("Yes, unfortunately today is a weekday.")
  
