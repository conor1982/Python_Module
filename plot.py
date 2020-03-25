import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import splev, splrep

x = np.arange(0,4,1)

fx = x
gx = x**2
hx = x**3

#https://matplotlib.org/api/_as_gen/matplotlib.pyplot.plot.html

fxspl = splrep(x,fx)
gxspl = splrep(x,gx)
hxspl = splrep(x,hx)

x2 = np.linspace(x.min(),x.max(),300, endpoint= False)

fx2 = splev(x2,fxspl)
gx2 = splev(x2,gxspl)
hx2 = splev(x2,hxspl)


plt.plot(x2,fx2,'--k',label = "f(x)",linewidth = 2)
plt.plot(x2,gx2,':b', label = "g(x)", linewidth = 3)
plt.plot(x2,hx2, 'navy', label = 'h(x)', linewidth = 3)
plt.legend()
plt.title('Weekly Task 8')
plt.xlabel('Range')
plt.ylabel('Function Value')
plt.xlim(xmin = 0)
plt.ylim(ymin = 0)
plt.savefig("Task 8")

plt.show()