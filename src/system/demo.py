from system.linear_system import LinearSystem
from plot.trajectory_visualization import (visualize_1d_trajectory, 
                                        visualize_2d_trajectory, 
                                        visualize_3d_trajectory)
import numpy as np 
from scipy.signal import cont2discrete

def one_dimensional_system_test():
    # Create our 1D system 
    a = np.array([[1.1 ]])
    b = np.array([[0.5 ]])
    sigma = np.array([[1]])
    x0 = np.array([1])
    syst = LinearSystem(a, b, sigma, x0)

    # Simulate system for T steps
    T = 50
    for t in range(T):
        syst.step(np.array([0]))

    # Visualize trajectory 
    visualize_1d_trajectory(syst.traj_x)

def two_dimensional_system_test():
    # Compute sampled matricies
    # Inverted pendulum parameters
    g = 9.81
    l = 1.0
    m = 1.0
    
    A_cont = np.array([[0, 1], 
                       [g/l, -0.1]])
    B_cont = np.array([[0], 
                       [1/(m*l**2)]])
    delta_t = 0.01
    sys_d = cont2discrete((A_cont, B_cont, np.zeros((1, 2)), np.zeros((1, 1))), delta_t, method='zoh')
    A_disc, B_disc = sys_d[0], sys_d[1]
    Sigma = np.array([[0,0],[0,0.01]])
    x0 = np.array([0,0])
    # Create system 
    syst = LinearSystem(A_disc, B_disc, Sigma, x0)

    # Simulate system for T steps 
    T = 1000
    K = -np.array([20,10])
    for t in range(T):
        u = K @ syst.x
        # u = 0
        syst.step(np.array([u]))
    
    # Visualize trajectory 
    visualize_2d_trajectory(syst.traj_x)

def three_dimensional_system_test():
    # Define system
    A = np.array([[0.99, 0.01, 0.00],
                  [0.01, 0.95, 0.01],
                  [0.50, 0.14, 0.97]])
    B = np.array([[1.0, 0.1],
                  [0.0, 0.2],
                  [1.1, 0.7]])

    Sigma = np.array([[0.30, 0.00, 0.00],
                      [0.00, 0.15, 0.00],
                      [0.00, 0.00, 0.10]])
    x0 = np.array([0,0,0])
    syst = LinearSystem(A, B, Sigma, x0)

    # Simulate system for T steps
    T = 100
    for t in range(T):
        syst.step(np.array([0,0]))
    
    # Visualize trajectory 
    visualize_3d_trajectory(syst.traj_x)

one_dimensional_system_test()
two_dimensional_system_test()
three_dimensional_system_test()

