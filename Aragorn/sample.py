# The sample data generator for complex networks

import numpy as np 
from ode import ODE

class GroundTruthSample:
    def __init__(self, adjacency_matrix):
        self.adjacency_matrix = np.array(adjacency_matrix)
        self.nx, self.ny = np.shape(self.adjacency_matrix)

    def _dydt(self,y,t):
        return self.adjacency_matrix.dot(y)

    def generate_samples_timeseries(self,n_sample, time_span=10, init_x=None):
        x = init_x
        if x is None:
            x = np.random.random(self.nx)
        ts = np.linspace(0,time_span,n_sample)
        model = ODE.FastODE(fun=self._dydt,y0=x)
        xs = model.evaluate(ts)
        data = [list(x) for x in xs]
        return data

    def generate_samples(self, n_sample, time_span=1):
        data = list()
        for _ in range(n_sample):
            x = np.random.random(self.nx)
            ts = np.linspace(0,time_span,2)
            model = ODE.FastODE(fun=self._dydt,y0=x)
            xs = model.evaluate(ts)
            data.append(list(xs[1,:]))
        return data

