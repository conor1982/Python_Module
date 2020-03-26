# Python_Module
Tasks and Assignments

All Assignments created using Python Programming Language

# Description

This is a Readme file for the tasks and assignments in the Programming and Scripting Module 2020. This Repository contains the Weekly Task code for the various assigments from the Programming and Scripting Course. 

In total there are 7 different tasks. The student is required to write a program for each of these tasks in Python. Each program can be looked at in more detail in the Table of Contents below.

# Table of Contents

1. [BMI Calculator](#bmi-calculator)
2. [Second String](#second-string)
3. [Collatz](#collatz)
4. [Weekday](#weekday)
5. [Square Root](#square-root) 
      
# BMI Calculator
This program asks the user to input their Weight (in KG) and Height (in Cm). The program then caluclates the BMI from these inputs and prints the result to 2 decimal places.

Error handling in place for user input
* input of negative values
* for input of string values 

Example of error handling

![image](https://user-images.githubusercontent.com/60179438/77441489-6521bb00-6de1-11ea-957b-d29ea9f4ec5c.png)

Program Code: https://github.com/conor1982/Python_Module/blob/master/bmi.py

To Run: python bmi.py -> Complete input requirements

User will then be asked to input Weight and Height

### References
- https://docs.python.org/3.1/tutorial/errors.html
- https://stackoverflow.com/questions/34244588/reject-negative-numbers-as-exceptions-in-python
- https://www.w3schools.com/python/python_while_loops.asp


# Second String
This program asks the user to input a sentence and will output every second letter of the input in reverse order

Program Code: https://github.com/conor1982/Python_Module/blob/master/secondstring.py 

To Run: python secondstring.py --> > Complete input requirement

### References
- https://www.w3schools.com/python/python_howto_reverse_string.asp


# Collatz
This program asks the user to input a positive integer. If the integer is even it will divide it by 2. If it is odd it will multiply the integer by 3 and add 1.

The program will loop through the numbers until in reaches a value of 1 and the loop ends.

While loop is used in this program for:

 a) looping through the numbers

 b) for error handling if a positive integer or is not entered by the user.

Program Code: https://github.com/conor1982/Python_Module/blob/master/collatz.py

To Run: python collatz.py -> Complete input requirement

Example Below

![image](https://user-images.githubusercontent.com/60179438/77440811-a06fba00-6de0-11ea-8282-e368f522eb0b.png)

### References
- https://www.tutorialspoint.com/python/python_while_loop.htm
- https://www.w3schools.com/python/python_while_loops.asp

# Weekday
When this program is ran from the command line it will output whether the timestamp at time the program is run falls on a weekday or weekend.
There is also a different meassge if ran on a Friday.

The Datetime libary is used in this program. The key variable is created from taking the current datetime and extracting the weekday number e.g  today = dt.datetime.today().weekday()

Using the weekday numbers as reference where 0 = Monday and 6 = Sunday, a weekend variable was created.

If ran when weekday is 5 or 6 will print the weekend meassage, 4 will print the Friday message and 0, 1, 2, 3 prints the weekday message 

If, Elif and Else statements are used to print out the message.

Program Code: https://github.com/conor1982/Python_Module/blob/master/weekday.py

To Run: python weekday.py No user input required to complete the program

Example Below

![image](https://user-images.githubusercontent.com/60179438/77449534-f137e080-6de9-11ea-9fa5-31a48ddacaad.png)

# Square Root
This program asks the user to input a positive number (integer or floating point) and outputs the approximate square root using the Newton method.

There are two error handling elements to the program to ensure a postitve value is entered.


The Newton method formula is as follows: (see video in references)
* x = approx
* f(x) = x^2 -2
* f'(x) = 2x i.e derivative
* new approx = x-(f(x)/f'(x)

The input is used as a parameter of the function created in the program.
The function:
* takes the input and divides by 2, this  "approx" in the Newton Method
* uses a while loop to loop through the Newton method formula (see above) once the absolute value of f(x) is > that 0.01 
* returns the number at the end of the loop to 1 decimel place

Function Code:

![image](https://user-images.githubusercontent.com/60179438/77664150-d4301880-6f75-11ea-9b1f-ab4cb4a743ca.png)


Program Code: https://github.com/conor1982/Python_Module/blob/master/squareroot.py

To Run: python squareroot.py

Example Below

![image](https://user-images.githubusercontent.com/60179438/77663868-726fae80-6f75-11ea-9081-64b20da37ea6.png)

### References
- https://www.w3schools.com/python/python_functions.asp
- https://www.youtube.com/watch?v=2158QbsunA8


