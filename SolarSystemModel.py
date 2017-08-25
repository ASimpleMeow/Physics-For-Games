#Earth testing - 23/09/2016 - Oleksandr Kononov
#Testing different materials, specifically Earth

from visual import *
from math import cos
from math import sin

scene.forward = vector(-0.019,-0.5,-0.85)

earth = sphere(pos=(0,0,100), radius=5, material=materials.earth, make_trail=True, trail_type="curve")
moon = sphere (pos=(0,0,106), radius=1, color=color.white)
sun = sphere(pos=(0,0,0), radius=50, color=color.yellow, material=materials.emissive)
dt = 0.0005
t = 0

while 1:
    rate(100)
    earth.rotate(angle=pi/420, axis=(0,1,0), orgin=earth.pos)
    moon.rotate(angle=pi/420, axis=(1,1,0), orgin=moon.pos)
    xt= 100*math.sin(2*pi*t)
    zt= 100*math.cos(2*pi*t)

    moonXt = 6*math.sin(2*pi*t)+earth.x
    moonZt = 6*math.cos(2*pi*t)+earth.z
    
    earth.pos = (xt,0,zt)
    moon.pos = (7*math.cos(10*pi*t)+earth.x,0,7*math.sin(10*pi*t)+earth.z)

    t = t + dt
