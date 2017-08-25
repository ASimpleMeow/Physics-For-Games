#Projectile Q2 - Oleksandr Kononov - 14/10/2016

from visual import *

autoscale=True

ball=sphere(pos=(0,30,0),radius=1, color=color.red)
floor=box(pos=(0,0,0),length=100, height=1,width=1,color=color.blue)

t=0
dt=0.01

while ball.pos.y>0:
    rate(100)
    ball.pos.x =30*cos((80*pi)/180)*t
    ball.pos.y =(30*sin((80*pi)/180)*t) - (4.9*t*t) + 30
    t= t+dt
