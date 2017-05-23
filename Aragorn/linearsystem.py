import numpy as np 

class linearsystem:
    def __init__(self,
        N,M=None,R=None,
        u=None,
        A,B=None,C=None,D=None,
        initx=None):

        self.N = N
        self.M = M
        self.x = np.zeros(N)
        if R is not None:
            self.y = np.zeros(R)