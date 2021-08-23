import torch
import random

def rand_theta():
    return random.uniform(0, 3.141592*2)

def rand_arm():
    return random.uniform(50, 3.141592*2)

def forward_kinematics(thetas, arms):
    thetas = thetas.reshape(1, -1)

    thetas_acc = thetas @ torch.tri(len(arms)).T
    thetas_acc = thetas_acc.flatten()

    x = torch.cos(thetas_acc) @ arms
    y = torch.sin(thetas_acc) @ arms

    return x, y