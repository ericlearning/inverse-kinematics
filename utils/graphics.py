import torch
import arcade
import torch.nn as nn
import torch.optim as optim
from arcade.key import *
from .visualization import draw_arm
from .losses import mseloss, constraint

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
        self.arm, self.cur_coord = draw_arm(
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
            loss = mseloss(self.cur_coord, self.target_coord, self.w, self.h)
            loss.backward()
            self.optim.step()

class InvKinematicsConstraint(Kinematics):
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
            loss_mse = mseloss(self.cur_coord, self.target_coord, self.w, self.h)
            loss_con = constraint(self.all_thetas[1:])
            loss = loss_mse + loss_con * 1.0
            loss.backward()
            self.optim.step()