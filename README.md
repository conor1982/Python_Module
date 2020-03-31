# Python_Module
Tasks and Assignments

All Assignments created using Python Programming Language

# Description

This is a Readme file for the Programming and Scripting Module 2020. This Repository contains the Weekly Task code for the various assignments for this Module. 

In total there are 7 different tasks. The student is required to write a program for each of these tasks in Python. Each program can be looked at in more detail in the Table of Contents below.

# Table of Contents

1. [BMI Calculator](#bmi-calculator)
2. [Second String](#second-string)
3. [Collatz](#collatz)
4. [Weekday](#weekday)
5. [Square Root](#square-root)
6. [Es](#es)
7. [Plot](#plot)

      
# BMI Calculator
This program asks the user to input their Weight (in KG) and Height (in Cm). The program then caluclates their BMI from these inputs and prints the result to 2 decimal places.

Error handling in place for user input
* input of negative values
* input of string values 

Example of error handling

![image](https://user-images.githubusercontent.com/60179438/77441489-6521bb00-6de1-11ea-957b-d29ea9f4ec5c.png)

Program Code: https://github.com/conor1982/Python_Module/blob/master/bmi.py

To Run: python bmi.py -> Complete input requirements (weight and height)

### References
- https://docs.python.org/3.1/tutorial/errors.html
- https://stackoverflow.com/questions/34244588/reject-negative-numbers-as-exceptions-in-python
- https://www.w3schools.com/python/python_while_loops.asp


# Second String
This program asks the user to input a sentence and will output every second letter of that input in reverse order.

Program Code: https://github.com/conor1982/Python_Module/blob/master/secondstring.py 

To Run: python secondstring.py --> > Complete input requirement

### References
- https://www.w3schools.com/python/python_howto_reverse_string.asp


# Collatz
This program asks the user to input a positive integer. If the integer is even it will divide it by 2. If it is odd it will multiply the integer by 3 and add 1.

The program will then loop through the numbers until in reaches a value of 1 and exits the loop.

A while loop is used in this program for:

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

Using the weekday numbers as reference where 0 = Monday and 6 = Sunday, a weekend variable was created i.e weekend = [5,6]

If ran when the weekday is 5 or 6 will print the weekend meassage, 4 will print the Friday message and 0, 1, 2, 3 prints the weekday message 

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
* f'(x) = 2*x i.e derivative
* new approx = x-(f(x)/f'(x)

The input is used as a parameter of the function created in the program.
The function:
* takes the input and divides by 2, this  "approx" in the Newton Method
* uses a while loop to loop through the Newton method formula (see above) once the absolute value of f(x) is > than 0.01 
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


# Es
This program reads in a text file from a command line argument and counts the amount of times a letter appears in that file. This programs has user input which allows user input what specfic letter they want a count for. The input value is case sensitive.

The sys python module is used in the program so the file name must be entered on the command line.

If no file is entered, there program will print 'No File entered on command line'
If the incorrect filename is entered or file can't be found the program will print  'File not Found'

The program takes in the file, reads and splits the words out and then creates a list for each word. Each letter/charcter is then stripped into its own list.

Example Below

![image](https://user-images.githubusercontent.com/60179438/77667510-33902780-6f7a-11ea-84a3-ef728ad7343e.png)

Using a nested for loop, a dictionary is created which counts every time each charcter appears in the file.

Example Below

![image](https://user-images.githubusercontent.com/60179438/77667648-66d2b680-6f7a-11ea-825d-4cd40aa055f1.png)

Program Code: https://github.com/conor1982/Python_Module/blob/master/es.py

To Run python es.py Enter_filename.txt
* Ensure text file is on the same directory from where you run the program

Example Below

![image](https://user-images.githubusercontent.com/60179438/77668596-828a8c80-6f7b-11ea-9c9a-ab84a8c37541.png)

### References
- http://hplgit.github.io/primer.html/doc/pub/input/._input-solarized007.html
- https://docs.python.org/3.3/tutorial/inputoutput.html
- https://www.w3schools.com/python/ref_string_strip.asp
- https://stackoverflow.com/questions/41970992/appending-values-to-dictionary-in-for-loop
- https://www.tutorialspoint.com/python/python_command_line_arguments.htm


# Plot
This program plots three functions in a give range (0-4) on one set of axes. The functions are:
* f(x) = x
* g(x) = x^2
* h(x) = x^3

### Python packages and sub-packages:
* Matplotlib.pyplot
* Numpy

Creating an array using the arange() function from Numpy, the variable x was created.

x = np.arange(0,4,1) It started from 0 up to and NOT INCLUDING 4 in steps of 1. 

Another variable called x_smooth was created by referencing the min and max values of variable x using the numpy linspace function. This variable then forms the basis for:
* f(x)
* g(x)
* h(x)

Matplotlib is used to plot each variable. Each line has a different color, line style, legend label and linewidth

Example Below

![image](https://user-images.githubusercontent.com/60179438/77670913-bd41f400-6f7e-11ea-8ec2-a03de2fe29bb.png)

Other Matplotlib features such as Title, Lengend, X and Y labels aslo used in the plot. The x and y limit is at 0 while the x axis ticks are linked to the variable x, the y axis ticks are linked to the maximum value in the h(x) variable.

The plot is then save with a specific name.

Program Code: https://github.com/conor1982/Python_Module/blob/master/plot.py

To Run python plot.py

Example of Plot

![image](https://user-images.githubusercontent.com/60179438/77671685-dd25e780-6f7f-11ea-8804-4d0e27ca3343.png)


## References
- https://www.khanacademy.org/math/algebra-home/alg-radical-eq-func/alg-graphs-of-radical-functions/v/graphs-of-square-root-functions
- https://stackoverflow.com/questions/5283649/plot-smooth-line-with-pyplot
- https://matplotlib.org/2.1.2/api/_as_gen/matplotlib.pyplot.plot.html
- https://docs.scipy.org/doc/numpy/reference/generated/numpy.linspace.html
- https://docs.scipy.org/doc/numpy/reference/generated/numpy.arange.html









