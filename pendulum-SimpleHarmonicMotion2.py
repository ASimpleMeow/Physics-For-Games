#Olkesandr Kononov
#Swinging Pendulum - Simple Harmonic Motion

from visual import *
from math import *

l1 = 0.6125
l2 = 0.5
w1 = sqrt(9.8/l1)
w2 = sqrt(9.8/l2)
O1 = 0.4
O2 = O1
A1 = 0.4
B1 = 0.125
A2 = 0.12
B2 = 0.2

autoscale = True
top = box(pos=(0,3,0),length=5,height=0.5,width=0.5,color=color.blue)
ball1= sphere(pos=(0,0,0), radius=0.5,color=color.red)
ball2= sphere(pos=(0,0,0), radius=0.5,color=color.red)

t = 0
dt = 0.01

while 1:
    rate(100)
    O1 = A1*cos(w1*t) + B1*sin(w1*t)
    O2 = A2*cos(w2*t) + B2*sin(w2*t)
    ball1.pos = ((l1*O1),(l1/2)*(O1*O1),0)
    ball2.pos = (ball1.pos.x+(l2*O2),(ball1.pos.y+((l2/2)*(O2*O2))),0)
    t = t + dt
