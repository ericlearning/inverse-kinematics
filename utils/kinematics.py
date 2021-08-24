import torch

def forward_kinematics(thetas, arms):
    thetas = thetas.reshape(1, -1)

    thetas_acc = thetas @ torch.triu(torch.ones((len(arms), len(arms))))
    thetas_acc = thetas_acc.flatten()

    x = torch.cos(thetas_acc) @ arms
    y = torch.sin(thetas_acc) @ arms

    return x, y

def forward_kinematics_all(thetas, arms):
    thetas = thetas.reshape(1, -1)

    thetas_acc = thetas @ torch.triu(torch.ones((len(arms), len(arms))))
    thetas_acc = thetas_acc.flatten()

    x = (torch.cos(thetas_acc) * arms).reshape(1, -1)
    y = (torch.sin(thetas_acc) * arms).reshape(1, -1)

    all_x = x @ torch.triu(torch.ones((len(arms), len(arms))))
    all_y = y @ torch.triu(torch.ones((len(arms), len(arms))))

    return all_x[0], all_y[0]