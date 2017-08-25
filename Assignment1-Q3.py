#Physics for Games Assignment 1 - Q3
#Oleksandr Kononov

#Mass of 0.5kg is actted by a force F(t)=3sin(2*pi*t) i N

from visual import *

ball = sphere(pos=(0,0,0), radius=1, color=color.red)
floor = box(pos=(0,-1,0), length=50, height=1, width=10, color=color.blue)

dt = 0.01
t = 0

while 1:
    rate(100)
    ball.pos.x = (-(3/(2*pi*pi))*(sin(2*pi*t)) + ((3*t*pi)))/pi
    t = t + dt
