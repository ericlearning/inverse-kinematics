import torch
import arcade
from utils.graphics import Kinematics

WIDTH = 800
HEIGHT = 800
COUNT = 9

all_thetas = torch.rand((COUNT,)) * (3.1415 * 2)
all_arms = torch.rand((COUNT,)) * (50) + 50

def main():
    window = Kinematics(WIDTH, HEIGHT, 'Kinematics', all_thetas, all_arms)
    window.setup()
    arcade.run()

if __name__ == '__main__':
    main()