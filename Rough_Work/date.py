import datetime
import calendar

weekdays = ("Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday")
months = ("January","February","March","April","May","June","July","August","September","October","November","December")


now = datetime.datetime.now()

date = now.day
month = now.month
year = now.year
weekday_num = now.weekday()
time = now.time()

print("Today is {} the {}th of {} {}".format(weekdays[weekday_num],date,months[month-1],year))


print(time)

