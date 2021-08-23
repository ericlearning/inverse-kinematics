import torch
# import pygame
import numpy as np

def rand_theta():
    return np.random.uniform(0, np.pi*2)

def rand_arm():
    return np.random.uniform(0, 10)

thetas = [
    rand_theta(),
    rand_theta(),
    rand_theta()
]
arms = [
    rand_arm(),
    rand_arm(),
    rand_arm()
]

thetas = np.array(thetas).reshape(1, -1)
arms = np.array(arms).reshape(1, -1)