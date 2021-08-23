import torch
# import pygame
import numpy as np

def rand_theta():
    return np.random.uniform(0, np.pi*2)

def rand_arm():
    return np.random.uniform(0, 10)

all_thetas = [
    rand_theta(),
    rand_theta(),
    rand_theta()
]
all_arms = [
    rand_arm(),
    rand_arm(),
    rand_arm()
]

def forward_kinematics(thetas, arms):
    thetas = np.array(thetas).reshape(1, -1)
    arms = np.array(arms)

    thetas_acc = thetas @ np.tri(len(arms)).T
    thetas_acc = thetas_acc.flatten()

    x = np.cos(thetas_acc) @ arms
    y = np.sin(thetas_acc) @ arms

    return x, y

print(forward_kinematics(all_thetas[:1], all_arms[:1]))
print(forward_kinematics(all_thetas[:2], all_arms[:2]))
print(forward_kinematics(all_thetas[:3], all_arms[:3]))