from vpython import *
import random

scene = canvas(width=550, height=580)

ball = sphere()
ball1 = sphere(radius=0.00001,color=color.white)

wallL = box(pos=vector(-4,0,0), size=vector(0.3, 8, 8), color=color.red)
wallR = box(pos=vector(4,0,0), size=vector(0.3,8,8), color=color.blue)
wallD = box(pos=vector(0,-4,0), size=vector(8,0.3,8), color=color.yellow)
wallU = box(pos=vector(0,4,0), size=vector(8,0.3,8), color=color.green)
wallB = box(pos=vector(0,0,-4), size=vector(8,8,0.3), color=color.magenta)

t = 0
dt = 0.005
d = ball.radius + 0.15

ball.vel = vector(random.random(), random.random(), random.random())


while t < 200:
    rate(1000)
    ball.pos = ball.pos + ball.vel * dt
    if abs(ball.pos.x) + d >= wallR.pos.x:
        if ball.pos.x > 0:
            ball.color = wallR.color
        else:
            ball.color = wallL.color
        ball.vel.x = -ball.vel.x
    elif abs(ball.pos.y) + d >= wallU.pos.y:
        if ball.pos.y > 0:
            ball.color = wallU.color
        else:
            ball.color = wallD.color
        ball.vel.y = -ball.vel.y
    elif abs(ball.pos.z) + d >= abs(wallB.pos.z):
        if ball.pos.z < 0:
            ball.color = wallB.color
        else:
           ball.color = color.white
        ball.vel.z = -ball.vel.z
    else:
        print(":C")
    t=t+dt