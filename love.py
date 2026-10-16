import.turtle
import math
import random
screen=turtle.screen()
screen.setup(widh=900,heght=90)
screen.titl("grow heart")
screen.bgcolor("#030303")
screen.tracer(1)
t=turtle.Turtle()
t.hideturtle()
t.speed(0)
vortex_t=turtle.Turtle()
vortex_t.hideturtle()
vortex_t.speed(0)
portcles=[]
for-in range(150):
    particles.appen({
        'angle':randome.uniform(0,2*math.pi)
        'radius':randome.uniform(50,400)
        'speed':randome.uniform(0.01,0.03)
        'size':randome.uniform(1.3)
        'color':randome.choice("#ff0055","#ff99ee","#f00ff","#00ffcc,"#ffcc00")
    })
    color palettes=[
        ["#ff0055","#ff3399","#f66cc","#ff99ee"]
       ["#00foff","#0088ff","#700ff","#fccooff"]
        ["#00ffcc","#33ff33","#fff00","#ff9900"]
         ["#ff2a6d","#d1f7f","#05d9e8","#f007f"]
    ]
