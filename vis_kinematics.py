import arcade
import numpy as np
from arcade.key import *
from pyglet import window
from kinematics import rand_theta, rand_arm, forward_kinematics

WIDTH = 800
HEIGHT = 800
COUNT = 9

all_thetas = np.array([rand_theta() for _ in range(COUNT)])
all_arms = np.array([rand_arm() for _ in range(COUNT)])

keys_inc = [Q, W, E, R, T, Y, U, I, O]
keys_dec = [A, S, D, F, G, H, J, K, L]

class Arm(arcade.Sprite):
    def update(self):
        self.x, self.y = forward_kinematics(
            self.all_thetas, self.all_arms)

def draw_arm(thetas, arms):
    prev_x, prev_y = 0, 0
    shapes = arcade.ShapeElementList()
    for i in range(1, len(thetas)+1):
        joint = arcade.create_ellipse_filled(
            prev_x+WIDTH//2, prev_y+HEIGHT//2, 5, 5, arcade.color.BLACK)
        x, y = forward_kinematics(thetas[:i], arms[:i])
        line = arcade.create_line(
            x+WIDTH//2, y+HEIGHT//2, prev_x+WIDTH//2, prev_y+HEIGHT//2,
            arcade.color.RED, 3)
        prev_x, prev_y = x, y
        shapes.append(joint)
        shapes.append(line)
    return shapes

class Kinematics(arcade.Window):
    def __init__(self, w, h, title, all_thetas, all_arms):
        super().__init__(w, h, title)
        arcade.set_background_color(arcade.color.WHITE)
        self.all_thetas = all_thetas
        self.all_arms = all_arms
        self.increments = np.zeros((len(all_thetas)))
        self.arm = None
    
    def update_arm(self):
        self.arm = draw_arm(self.all_thetas, self.all_arms)
    
    def setup(self):
        self.update_arm()
    
    def on_draw(self):
        arcade.start_render()
        self.arm.draw()
    
    def on_update(self, _):
        self.all_thetas += self.increments
        if self.increments.any():
            self.update_arm()
    
    def set_increment(self, symbol, values):
        if symbol in keys_inc:
            idx = keys_inc.index(symbol)
            if idx < len(self.increments):
                self.increments[idx] = values[0]
        if symbol in keys_dec:
            idx = keys_dec.index(symbol)
            if idx < len(self.increments):
                self.increments[idx] = values[1]

    def on_key_press(self, symbol, _):
        self.set_increment(symbol, [0.1, -0.1])
    
    def on_key_release(self, symbol, _):
        self.set_increment(symbol, [0, 0])

def main():
    window = Kinematics(WIDTH, HEIGHT, 'Kinematics', all_thetas, all_arms)
    window.setup()
    arcade.run()

if __name__ == '__main__':
    main()