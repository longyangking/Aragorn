# Real-valued Lorentz system
import sys
sys.path.append("..")

import numpy as np 
from Aragorn.ode import ODE
import matplotlib.pyplot as plt

if __name__=='__main__':
    m0,tau = 1.0,1.0
    def circle(y,t):
        x1,x2,x3 = y
        A1 = -m0*x1 + tau*x2
        A2 = -m0*x2 + tau*x3
        A3 = -m0*x3 + tau*x1
        dydt = [A1,A2,A3]
        return dydt

    y0 = [1,0,0]
    ts = np.linspace(0,10,2001)
    my_model = ODE.FastODE(fun=circle,y0=y0)
    sol = my_model.evaluate(ts)

    plt.figure()
    plt.plot(ts, sol[:, 0], 'b', label='$x_1(t)$')
    plt.plot(ts, sol[:, 1], 'g', label='$x_2(t)$')
    plt.plot(ts, sol[:, 2], 'r', label='$x_3(t)$')
    plt.legend(loc='best')
    plt.xlabel('t')
    plt.show()