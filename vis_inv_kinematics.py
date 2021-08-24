import torch
import arcade
import torch.nn as nn
import torch.optim as optim
from utils.graphics import Kinematics
from utils.kinematics import forward_kinematics

def mseloss(coord1, coord2):
    return (coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2

class InvKinematics(Kinematics):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.all_thetas = nn.Parameter(self.all_thetas)
        self.optim = optim.Adam([self.all_thetas], 0.1)
        self.target_coord = None

    def on_mouse_motion(self, x, y, _, __):
        self.target_coord = (x-self.w/2, y-self.h/2)

    def on_update(self, _):
        with torch.no_grad():
            self.all_thetas += self.increments
            self.all_thetas %= (3.1415 * 2)
        self.update_arm()
        if not self.increments.any() and self.target_coord is not None:
            self.optim.zero_grad()
            loss = mseloss(self.cur_coord, self.target_coord)
            loss.backward()
            self.optim.step()

WIDTH = 800
HEIGHT = 800
COUNT = 20

all_thetas = torch.rand((COUNT,)) * (3.1415 * 2)
all_arms = torch.rand((COUNT,)) * (15) + 5

all_thetas = torch.full((COUNT,), 0, dtype=torch.float32)
all_arms = torch.full((COUNT,), 15, dtype=torch.float32)

all_arms = torch.linspace(20, 1, COUNT, dtype=torch.float32)

print(all_arms)

def main():
    window = InvKinematics(
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