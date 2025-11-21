from copy import deepcopy
import numpy as np 

class LinearSystem:
    def __init__(self, A, B, Sigma, x0):
        self.A = np.array(A)
        self.B = np.array(B)
        self.Sigma = np.array(Sigma)
        self.x = np.array(x0)
        self.traj_x = [deepcopy(self.x)]
        self.traj_u = []
        
        self.d = self.Sigma.shape[1] if self.Sigma.ndim > 1 else 1

    def sample_noise(self):
        return np.random.randn(self.d)

    def step(self, u, noise=True):
        self.x = np.dot(self.A, self.x) + np.dot(self.B, u)
        if noise: 
            self.x += np.dot(self.Sigma, self.sample_noise())
        self.traj_x.append(deepcopy(self.x))
        self.traj_u.append(u)
