#Projectile Q1 - Oleksandr Kononov - 14/10/2016

from visual import *

autoscale=True

ball=sphere(pos=(0,0,0),radius=1, color=color.red)
floor=box(pos=(0,0,0),length=40, height=1,width=1,color=color.blue)

t=0
dt=0.01

while t<2.65:
    rate(100)
    ball.pos.x =15*cos((60*pi)/180)*t
    ball.pos.y =(15*sin((60*pi)/180)*t) - (4.9*t*t)
    t= t+dt
