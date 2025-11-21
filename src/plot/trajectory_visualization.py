import matplotlib.pyplot as plt
import numpy as np 

def visualize_1d_trajectory(traj_x):
    plt.plot(np.arange(len(traj_x)), traj_x)
    plt.xlabel("Timestep")
    plt.ylabel("x")
    plt.show()

def visualize_2d_trajectory(traj_x):
    traj_x = np.array(traj_x)
    plt.plot(traj_x[:, 0], traj_x[:, 1], '-o', markersize=0, linewidth=1)
    plt.xlabel("$x_1$")
    plt.ylabel("$x_2$")
    plt.axis('equal')
    plt.show()

def visualize_3d_trajectory(traj_x):
    traj_x = np.array(traj_x)
    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')
    ax.plot(traj_x[:, 0], traj_x[:, 1], traj_x[:, 2], '-o', markersize=0, linewidth=1)
    ax.set_xlabel("$x_1$")
    ax.set_ylabel("$x_2$")
    ax.set_zlabel("$x_3$")
    plt.show()
