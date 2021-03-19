from vpython import *
import random
N = 50

scene = canvas(width=550, height=580)

N=50
balls=[]
counter=N
r=0.4
t=0
m=1
M=100
dt=0.01

circle = ring(pos=vector(0,0,0), axis=vector(0,0,1), radius=10, thickness=0.5, color=color.cyan)
big_ball=sphere(pos=vector(2,2,0), radius=1, color=color.red, mass=M, vel=vector(0,0,0))

for x in range(-5,5):
    for y in range(-5,5):
        if counter<=0:
            break
        balls.append(sphere(pos=vector(x,y,0), radius=r, color=color.green, mass=m, vel=vector(0,0,0)))
        counter = counter-1

for i in balls:
    i.vel = vector(random.random(), random.random(), 0)

balls.append(big_ball)
N+=1

#d = balls[0].radius + circle.thickness/2

while True:
    rate(1000)
    for ball in balls:
        ball.pos += ball.vel * dt
        if mag(ball.pos+ball.vel * dt)>=circle.radius - ball.radius - circle.thickness: #ball wall collision
            vr = dot(ball.vel, ball.pos/mag(ball.pos)) *(ball.pos/mag(ball.pos))
            ball.vel = ball.vel - 2*vr


    for i in range(N):
        for m in range(i+1,N):
            dif = balls[i].pos - balls[m].pos
            if mag(dif) <= balls[i].radius + balls[m].radius:
                a = mag2((balls[i].vel-balls[m].vel))
                #if a == 0:
                 #   continue
                b = -2 * dot((balls[i].pos-balls[m].pos), (balls[i].vel-balls[m].vel))
                c = (mag(balls[i].pos-balls[m].pos))**2 - (balls[i].radius + balls[m].radius)**2
                delta = b**2 - 4*a*c
                #if delta < 0:
                 #   continue
                if a!= 0 and delta > 0:
                    dt1 = (-1 * b + delta**(1/2))/(2*a)

                    newpos1=balls[i].pos - balls[i].vel *dt1
                    newpos2 = balls[m].pos - balls[m].vel * dt1
                    newvel1 = balls[i].vel - 2 * balls[m].mass/(balls[i].mass + balls[m].mass)*dot((balls[i].vel-balls[m].vel), (newpos1-newpos2)/mag(newpos1-newpos2)) * (newpos1-newpos2)/mag(newpos1-newpos2)
                    newvel2 = balls[m].vel + 2 * balls[i].mass / (balls[i].mass + balls[m].mass) * dot(
                        (balls[i].vel - balls[m].vel), (newpos1 - newpos2) / mag(newpos1 - newpos2)) * (
                                          newpos1 - newpos2) / mag(newpos1 - newpos2)
                    balls[i].pos = newpos1 + newvel1 * dt1
                    balls[m].pos = newpos1 + newvel2 * dt1
                    balls[i].vel = newvel1
                    balls[m].vel = newvel2
                else:
                    r = (balls[i].pos - balls[m].pos) / mag(balls[i].pos - balls[m].pos)
                    V1 = balls[i].vel - 2 * (balls[m].mass / (balls[i].mass + balls[m].mass)) * dot((balls[i].vel - balls[m].vel), r) * r
                    V2 = balls[m].vel + 2 * (balls[i].mass / (balls[i].mass + balls[m].mass)) * dot((balls[i].vel - balls[m].vel), r) * r
                    balls[i].vel = V1
                    balls[m].vel = V2
    t = t+dt
