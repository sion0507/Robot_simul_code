import math
from .kinematics import R, L

class Odom:
    def __init__(self):
        self.x = 0.0; self.y = 0.0; self.th = 0.0
    def reset_heading(self, yaw):
        self.x = 0.0; self.y = 0.0; self.th = yaw
    def step_from_wheels(self, wl, wr, dt):
        v_l = wl * R
        v_r = wr * R
        v = 0.5*(v_l+v_r)
        w = (v_r - v_l)/L
        self.x += v*math.cos(self.th)*dt
        self.y += v*math.sin(self.th)*dt
        self.th += w*dt
