import math
import torch
import arcade
import torch.nn as nn
from utils.graphics import InvKinematicsConstraint

WIDTH = 800
HEIGHT = 800
COUNT = 20

all_thetas = torch.rand((COUNT,)) * (3.1415 * 2)
all_arms = torch.rand((COUNT,)) * (15) + 5

all_thetas = torch.full((COUNT,), 0, dtype=torch.float32)
all_arms = torch.full((COUNT,), 15, dtype=torch.float32)

all_arms = torch.linspace(20, 1, COUNT, dtype=torch.float32)

all_arms = 10 ** torch.linspace(
    math.log(40, 10), math.log(10, 10),
    COUNT, dtype=torch.float32)

all_arms = 10 ** torch.linspace(
    math.log(10, 10), math.log(40, 10),
    COUNT, dtype=torch.float32)

print(all_arms)

def main():
    window = InvKinematicsConstraint(
        w=WIDTH,
        h=HEIGHT,
        title='Kinematics',
        all_thetas=all_thetas,
        all_arms=all_arms
    )
    window.setup()
    arcade.run()

if __name__ == '__main__':
    main()