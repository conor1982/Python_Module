#Conor O'Riordan
#Task 8
#Program that displays the plot of functions f(x) = x, g(x) = x^2, h(x) = x^3
#in the range of [0,4] on one set of axes

#Matplotlib for plotting
#Numpy for arrays
import matplotlib.pyplot as plt
import numpy as np

#variable using Numpy to create an array
#Similar to list, last value not included, at values are increasing by 1 step
#Ref: Lecture Video
#Ref: https://docs.scipy.org/doc/numpy/reference/generated/numpy.arange.html
x = np.arange(0,4,1)

#Ref https://docs.scipy.org/doc/numpy/reference/generated/numpy.linspace.html
#Variable to smooth out X [0:4] over 500 evenly spaced steps 
x_smooth = np.linspace(x.min(),x.max(),500)

#Variables for functions to be plotted E.G g(x) = 0,4,9
#https://www.khanacademy.org/math/algebra-home/alg-radical-eq-func/alg-graphs-of-radical-functions/v/graphs-of-square-root-functions

#f(x)
fx = x_smooth

#g(x)
gx = x_smooth**2

#h(x)
hx = x_smooth**3

#Ref https://matplotlib.org/api/_as_gen/matplotlib.pyplot.plot.html
#Ref https://matplotlib.org/2.1.2/api/_as_gen/matplotlib.pyplot.plot.html (details on plot line colours, legends and other features)
#plot of each function
#black coloured dash line, line width 2 label is f(x)
plt.plot(x_smooth,fx,'--k',label = "f(x) = x",linewidth = 2)

#blue coloured dotted line, line width 3, label is g(x)
plt.plot(x_smooth,gx,':b', label = "g(x) = x^2", linewidth = 3)

#navy coloured solid line, line width 4, label = h(x)
plt.plot(x_smooth,hx, 'navy', label = 'h(x) = x^3', linewidth = 4)

#display legend - from plt.plot label function
plt.legend()

#display plot title
plt.title('Weekly Task 8')

#display x axis label
plt.xlabel('Range')

#display y axis label
plt.ylabel('Function Value')

#start x axis at 0
plt.xlim(xmin = 0)

#start y axis at 0
plt.ylim(ymin = 0)

#https://stackoverflow.com/questions/12608788/changing-the-tick-frequency-on-x-or-y-axis-in-matplotlib
#x axis tick frequency at 1
plt.xticks(np.arange(min(x), max(x)+1,1))

#Ref https://stackoverflow.com/questions/12608788/changing-the-tick-frequency-on-x-or-y-axis-in-matplotlib
#y axis tik frequency every 2, to a value of 2 past the max value of the plot
plt.yticks(np.arange(min(hx), max(hx)+2,2))

#save plt
plt.savefig("Task 8")

