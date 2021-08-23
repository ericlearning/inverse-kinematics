import torch
import arcade
import torch.nn as nn
from arcade.key import *
from .visualization import draw_arm

keys_inc = [Q, W, E, R, T, Y, U, I, O]
keys_dec = [A, S, D, F, G, H, J, K, L]

class Kinematics(arcade.Window):
    def __init__(self, w, h, title, all_thetas, all_arms):
        super().__init__(w, h, title)
        arcade.set_background_color(arcade.color.WHITE)
        self.w = w
        self.h = h
        self.all_thetas = all_thetas
        self.all_arms = all_arms
        self.increments = torch.zeros((len(all_thetas)))
        self.arm = None
    
    def update_arm(self):
        self.arm = draw_arm(
            self.all_thetas, self.all_arms, self.w, self.h)
    
    def setup(self):
        self.update_arm()
    
    def on_draw(self):
        arcade.start_render()
        self.arm.draw()
    
    def on_update(self, _):
        with torch.no_grad():
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