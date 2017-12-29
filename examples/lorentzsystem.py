# Real-valued Lorentz system
import sys
sys.path.append("..")

import numpy as np 
from Aragorn.ode import ODE
import matplotlib.pyplot as plt

if __name__=='__main__':
    a,b,c = 10,8/3.0,8.0
    def lorentz(y,t):
        x1,x2,x3 = y
        A1 = a*(x2-x1)
        A2 = c*x1 - x2 - x1*x3
        A3 = x1*x2 - b*x3
        dydt = [A1,A2,A3]
        return dydt

    y0 = [0.1, 0.3, 1]
    ts = np.linspace(0,20,2001)
    sim = ODE.FastODE(fun=lorentz,y0=y0)
    sol = sim.evaluate(ts)

    plt.figure()
    plt.scatter(sol[:, 0], sol[:,1])
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Lorentz system')
    plt.show()
