import torch
# import pygame
import numpy as np

def rand_theta():
    return np.random.uniform(0, np.pi*2)

def rand_arm():
    return np.random.uniform(0, 10)