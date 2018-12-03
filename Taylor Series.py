import sympy as sy
import numpy as np
from sympy.functions import sin,cos,tan
import matplotlib.pyplot as plt

plt.style.use("ggplot")

# Define the variable and the function to approximate and point to approximate around.
x = sy.Symbol('x')
p0 = float(input("What point would you like to approximate your function around?: "))
#f = np.e**(x)
#f = sin(x)
#f = cos(x)
f = tan(x)

# Factorial function
def factorial(n):
    if n <= 0:
        return 1
    else:
        return n*factorial(n-1)

# Taylor approximation at x0 of the function 'function'
def taylor(function,x0,n):
    i = 0
    p = 0
    while i <= n:
        p = p + (function.diff(x,i).subs(x,x0))/(factorial(i))*(x-x0)**i
        i += 1
    return p


# Plot results
def plot():
    x_lims = [p0-7,p0+7]
    x1 = np.linspace(x_lims[0],x_lims[1],800)
    y1 = []
    # Approximate up until 10 starting from 1 and using steps of 2
    for j in range(1,10,2):
        func = taylor(f,p0,j)
        print('Taylor expansion at n='+str(j),func)
        for k in x1:
            y1.append(func.subs(x,k))
        plt.plot(x1,y1,label='order '+str(j))
        y1 = []
    # Plot the function to approximate 
    #plt.plot(x1,np.e**(x1),label='e of x')
    #plt.plot(x1,np.sin(x1),label='sin of x')
    #plt.plot(x1,np.cos(x1),label='cos of x')
    plt.plot(x1,np.tan(x1),label='tan of x')
    
    plt.xlim(x_lims)
    plt.ylim([-5,5])
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.grid(True)
    plt.title('Taylor series approximation')
    plt.show()

plot()
