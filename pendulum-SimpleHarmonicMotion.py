#Olkesandr Kononov
#Swinging Pendulum - Simple Harmonic Motion

from visual import *
from math import *

l = 0.6125
w = 4
O = 0.4
A = 0.4
B = 0.125

autoscale = True
top = box(pos=(0,3,0),length=5,height=0.5,width=0.5,color=color.blue)
ball= sphere(pos=(l*O,(l/2)*(O*O), 0), radius=0.5,color=color.red)
string = arrow(pos=top.pos,axis=(0,0,0), shaftwidth=0.025,color=color.white)

t = 0
dt = 0.01

while 1:
    rate(100)
    O = A*cos(w*t) + B*sin(w*t)
    ball.pos = (l*O,(l/2)*(O*O),0)
    string.axis = (ball.pos.x-string.pos.x,ball.pos.y-string.pos.y,0)
    t = t + dt
