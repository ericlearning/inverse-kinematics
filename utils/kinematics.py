import torch

def forward_kinematics(thetas, arms):
    thetas = thetas.reshape(1, -1)

    thetas_acc = thetas @ torch.triu(torch.ones((len(arms), len(arms))))
    thetas_acc = thetas_acc.flatten()

    x = torch.cos(thetas_acc) @ arms
    y = torch.sin(thetas_acc) @ arms

    return x, y