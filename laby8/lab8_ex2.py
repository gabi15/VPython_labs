from vpython import *
import random

scene = canvas(width=550, height=580)

wallL = box(pos=vector(-4,0,0), size=vector(0.3, 8, 8), color=color.red)
wallR = box(pos=vector(4,0,0), size=vector(0.3,8,8), color=color.blue)
wallD = box(pos=vector(0,-4,0), size=vector(8,0.3,8), color=color.yellow)
wallU = box(pos=vector(0,4,0), size=vector(8,0.3,8), color=color.green)
wallB = box(pos=vector(0,0,-4), size=vector(8,8,0.3), color=color.magenta)
#walls = [wallR, wallL, wallU, wallD, wallB]


t=0
dt=0.005
N=30
balls=[]
counter = N

for x in range(-3,4):
    for y in range(-3,4):
        if counter <= 0:
            break
        balls.append(sphere(pos=vector(x, y, 0), radius=0.4, color=color.white))
        counter -= 1



for i in balls:
    i.vel = vector(random.random(), random.random(), random.random())

d = balls[0].radius + 0.15

while 1:
    rate(1000)
    for i in range(N):
        balls[i].pos = balls[i].pos + balls[i].vel *dt
        if abs(balls[i].pos.x) +d >= wallR.pos.x:
            if balls[i].pos.x > 0:
                balls[i].color = wallR.color
            else:
                balls[i].color = wallL.color
            balls[i].vel.x = -balls[i].vel.x
        elif abs(balls[i].pos.y) +d >= wallU.pos.y:
            if balls[i].pos.y > 0:
                balls[i].color = wallU.color
            else:
                balls[i].color = wallD.color
            balls[i].vel.y = -balls[i].vel.y
        elif abs(balls[i].pos.z) +d >= abs(wallB.pos.z):
            if balls[i].pos.z < 0:
                balls[i].color = wallB.color
            else:
                balls[i].color = color.white
            balls[i].vel.z = -balls[i].vel.z
        t = t + dt
