#Physics for Games Assignment 1 - Q4
#Oleksandr Kononv

#Body moving along x-axis
#a(t) = -4x(t) m/s/s
#v(0) = 0.5 m/s
#x(0) = 0m

from visual import *

ball = sphere(pos=(0,0,0), radius=0.5, color=color.red)
floor = box(pos=(0,-1,0), length=2, height=1, width=10, color=color.blue)

dt = 0.01
vt = 0.5

while 1:
    rate(100)
    at = -4*ball.x
    vt = vt + at*dt
    ball.x = ball.x + vt*dt
