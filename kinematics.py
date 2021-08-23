import numpy as np

def rand_theta():
    return np.random.uniform(0, np.pi*2)

def rand_arm():
    return np.random.uniform(50, 100)

def forward_kinematics(thetas, arms):
    thetas = thetas.reshape(1, -1)

    thetas_acc = thetas @ np.tri(len(arms)).T
    thetas_acc = thetas_acc.flatten()

    x = np.cos(thetas_acc) @ arms
    y = np.sin(thetas_acc) @ arms

    return x, y