#Bouncing Ball.py - 23/09/2016 - Oleksandr Kononov
#Slightly altered version to the notes sheet
#Here the ball will bounce a bit more realistically

from visual import *

autoscale = True

floor = box(pos=(0,0,0), length=100, height=5, width=100, color=color.yellow)
ball = sphere(pos=(-50,60,0), radius=2, color=color.red, make_trail=True, trail_type="curve")

ball.velocity = vector(1,-1,0)
g = 9.81
e = 0.45
dt = 0.01
t = 0

while t<120:
    rate(1000)
    ball.pos = ball.pos + ball.velocity*dt
    if (ball.y-ball.radius)<(floor.pos.y+(floor.height/2)):
        ball.velocity.y = -e*(ball.velocity.y+(ball.velocity.y/2))
    else:
        ball.velocity.y = ball.velocity.y - g*dt
    t=t+dt
