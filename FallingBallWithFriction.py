#Oleksandr Kononov
#Mass 10kg falling from 500m, g=10m/s/s with air friction

from visual import *

ball=sphere(pos=(0,500,0),radius=6,color=color.red)
floor=box(pos=(0,0,0),length=100,height=6,width=10,color=color.blue)

ball.velocity = vector(0,0,0)
dt=0.01
t=0

while ball.y-ball.radius>3:
    rate(100)
    
    ball.velocity.y = dt - 0.9993*(10*t)
    
    ball.pos.y = ball.pos.y + ball.velocity.y*dt
    t = t + dt
