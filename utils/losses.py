import torch

def mseloss(coord1, coord2, w=None, h=None):
    if w is None or h is None:
        return (coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2
    else:
        return ((coord1[0] - coord2[0]) / w) ** 2 + ((coord1[1] - coord2[1]) / h) ** 2

def constraint(thetas):
    return -torch.abs(thetas - 3.1415).mean()