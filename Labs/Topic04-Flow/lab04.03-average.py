#Read in Numbers until 0 entered
#0 ends the program
#print all previous inputs
#print average

#use list [] 

num_list = []

#first number
number = int(input("Enter Number (0 to Quit Program) "))

while number != 0:
    num_list.append(number)
 
 #Loop for 2nd number
    number = int(input("Enter Number (0 to Quit Program) "))

for value in num_list:
    print(value)

#average of numbers entered
average = float(sum(num_list))/len(num_list)
print("The average is: ",average)
#print("the average is {}".format(average))

#sum of numbers entered:
sum_num = float(sum(num_list))
print("The total sum is:",sum_num)

#Max number
#Min number
#Print practice
max_num = max(num_list)
min_num = min(num_list)

print("The biggest number entered is",max_num,"and the smallest number entered is",min_num)
#,"This gives a range from",range(min_num,max_num))
