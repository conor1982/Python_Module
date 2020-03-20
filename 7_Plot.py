import matplotlib.pyplot as plt
import numpy as np
x = np.arange(0,4.0)

fx = x
gx = x**2
hx = x**3

#https://matplotlib.org/api/_as_gen/matplotlib.pyplot.plot.html

plt.plot(x,fx,'--k',label = "f(x)",linewidth = 2)
plt.plot(x,gx,'--b', label = "g(x)", linewidth = 3)
plt.plot(x,hx, '--r', label = 'h(x)', linewidth = 4)
plt.legend()
plt.title('Weekly Task 8')
plt.xlabel('Range')
plt.ylabel('Function Value')
plt.savefig("Task 8")
