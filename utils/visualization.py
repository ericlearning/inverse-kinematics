import torch
import arcade
from .kinematics import forward_kinematics

@torch.no_grad()
def draw_arm(thetas, arms, w, h):
    prev_x, prev_y = 0, 0
    shapes = arcade.ShapeElementList()
    for i in range(1, len(thetas)+1):
        joint = arcade.create_ellipse_filled(
            prev_x+w//2, prev_y+h//2, 5, 5, arcade.color.BLACK)
        x, y = forward_kinematics(thetas[:i], arms[:i])
        x = int(x)
        y = int(y)
        line = arcade.create_line(
            x+w//2, y+h//2, prev_x+w//2, prev_y+h//2,
            arcade.color.RED, 3)
        prev_x, prev_y = x, y
        shapes.append(joint)
        shapes.append(line)
    return shapes