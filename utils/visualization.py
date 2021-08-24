import torch
import arcade
from skimage.color import hsv2rgb
from .kinematics import forward_kinematics, forward_kinematics_all

@torch.no_grad()
def draw_arm_naive(thetas, arms, w, h):
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

def draw_arm(thetas, arms, w, h):
    prev_x, prev_y = 0, 0
    shapes = arcade.ShapeElementList()
    all_x, all_y = forward_kinematics_all(thetas, arms)
    for i, cur_theta in enumerate(thetas):
        joint = arcade.create_ellipse_filled(
            prev_x+w//2, prev_y+h//2, 5, 5, arcade.color.BLACK)
        x, y = all_x[i], all_y[i]
        x = int(x)
        y = int(y)
        color = int(abs(float(cur_theta) - 3.1415) / 3.1415 * 255)
        line = arcade.create_line(
            x+w//2, y+h//2, prev_x+w//2, prev_y+h//2, (color, 0, 0), 3)
        prev_x, prev_y = x, y
        shapes.append(joint)
        shapes.append(line)
    return shapes, (all_x[-1], all_y[-1])