#Conor O'Riordan
#Week 5 Problem Sheet
#Output whether today is a weekday or not
#Weekday function

import datetime as dt

def PartofWeek():
    #weekend day numbers
    weekend = [5,6]
    weekdays = ("Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday")
    weekdaynum = dt.datetime.now().weekday()

    if weekdaynum in weekend:
        print("Today is",weekdays[weekdaynum],"It is the weekend, yay!")
    
    elif weekdaynum == 4:
        print("Today is",weekdays[weekdaynum],"It's a weekday but it at least it is Friday!!!!")
    
    else:
        print("Today is",weekdays[weekdaynum],"and yes unfortunately today is a weekday.")

    


PartofWeek()

