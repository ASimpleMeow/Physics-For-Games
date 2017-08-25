#Ball Circling Motion - 23/09/2016 - Oleksandr Kononov
#The ball will move in a cricular motion

from visual import *
from math import *

autoscale = True
ball = sphere(pos=(-10*math.cos(0),0,0), radius=2, color=color.red,make_trail=True, trail_type="curve")
orgin = sphere(pos=(0,0,0),radius=0.5,color=color.white)
ballAcceleration = arrow(pos=ball.pos,axis=(-ball.pos.x+orgin.pos.x,-ball.pos.y+orgin.pos.y,0), shaftwidth=0.25)
ballAngularVel = arrow(pos=ball.pos,axis=(-ball.pos.x+orgin.pos.x,-ball.pos.y-orgin.pos.y,0),shaftwidth=0.25)

dt = 0.01
t = 0

while 1:
    rate(50)
    w = 2*math.pi
    xt = -10*math.cos(w*t)
    yt = 10*math.sin(w*t)
   # ball.pos = (xt,yt,0)#ball.pos.z+0.05)
    #orgin.pos.z = orgin.pos.z+0.05
    ballAcceleration.pos = ball.pos
    ballAcceleration.axis=((-ball.pos.x+orgin.pos.x)*0.75,(-ball.pos.y+orgin.pos.y)*0.75,0)

    wx = (w * (-ball.pos.x+orgin.pos.x))
    
    ballAngularVel.pos = ball.pos
    ballAngularVel.axis=(wx,wx,0)
    t = t + dt
