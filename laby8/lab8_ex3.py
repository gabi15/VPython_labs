"""In this program the ball is bouncing from the box's walls and changes color to the color of a touched wall"""

from vpython import *
import random

scene = canvas(width=800, height=580)

wallL = box(pos=vector(-5,0,0), size=vector(0.3, 10, 10), color=color.red)
wallR = box(pos=vector(5,0,0), size=vector(0.3,10,10), color=color.blue)
wallD = box(pos=vector(0,-5,0), size=vector(10,0.3,10), color=color.yellow)
wallU = box(pos=vector(0,5,0), size=vector(10,0.3,10), color=color.green)
wallB = box(pos=vector(0,0,-5), size=vector(10,10,0.3), color=color.magenta)


t=0
dt=0.005
N=20
balls=[]
counter = N
cx=7 # counter to position balls next to the box
cy=7 #counter to position balls next to the box

for x in range(-4,5):
    for y in range(-4,5):
        if counter <= 0:
            break
        balls.append(sphere(pos=vector(x, y, 0), radius=0.4, color=color.white,vel = vector(random.random(), random.random(), random.random())))
        counter -= 1

d = balls[0].radius + 0.15

while 1:
    rate(1000)
    for i in range(N):
        balls[i].pos = balls[i].pos + balls[i].vel *dt
        if abs(balls[i].pos.x) +d >= wallR.pos.x and balls[i].pos.x<6:
            if balls[i].pos.x > 0:
                balls[i].color = wallR.color
            else:
                balls[i].color = wallL.color
            balls[i].vel.x = -balls[i].vel.x
        elif abs(balls[i].pos.y) +d >= wallU.pos.y and balls[i].pos.x<6:
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

        for m in range(i+1,N):
            dif = balls[i].pos - balls[m].pos
            if mag(dif) <= 2*balls[0].radius:
                cy -= 2
                if cy<-5:
                    cx+=1;
                    cy=5

                balls[i].vel = vector(0,0,0)
                balls[m].vel = vector(0, 0, 0)
                balls[i].pos = vector(cx,cy, 4)
                balls[m].pos=vector(cx,cy+1,4)
        t=t+dt
