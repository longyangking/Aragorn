# Controll network demo 1
import sys
sys.path.append("..")

import numpy as np 
from Aragorn.ode import ODE
import matplotlib.pyplot as plt

if __name__=='__main__':
    a21, a31, a41, a34 = 0.5, 0.2, 0.6, 0.8
    b1, b2 = 1.2, 0.5

    def u(x,t):
        u1 = np.sin(0.8*np.pi*t)
        u2 = np.cos(1.2*np.pi*t)
        return np.array([u1,u2,0,0])

    def network(x,t):
        x1,x2,x3,x4 = x
        A1 = 0
        A2 = a21*x1
        A3 = a31*x1 + a34*x4
        A4 = a41*x1
        dxdt = np.array([A1,A2,A3,A4]) + u(x,t)
        return dxdt

    x0 = [1.0,0.2,-0.9,0.7]
    ts = np.linspace(0,5,2001)
    my_model = ODE.FastODE(network,x0)
    sol = my_model.evaluate(ts)

    plt.figure()
    plt.plot(ts, sol[:, 0], 'b', label='$x_1(t)$')
    plt.plot(ts, sol[:, 1], 'g', label='$x_2(t)$')
    plt.plot(ts, sol[:, 2], 'r', label='$x_3(t)$')
    plt.plot(ts, sol[:, 3], 'y', label='$x_4(t)$')
    plt.legend(loc='best',fontsize=18)
    plt.xlabel('t')
    plt.show()