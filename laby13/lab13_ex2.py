from vpython import *
#from vpython.graph import *

scene = canvas(width=580, height=580)
scene=graph()
pf2=gcurve(color=color.red)
pf3=gcurve(color=color.cyan)
f2=[]
f3=[]

r=0.1
g=9.8

ball1=sphere(pos=vector(0,1,0), radius=r, color=color.yellow, vel=vector(0,0,0),a=vector(0,-g,0), mass=10)
ball2=sphere(pos=vector(0,1.25,0), radius=r, color=color.red, vel=vector(0,0,0), a=vector(0,-g,0), mass=1)
ball3=sphere(pos=vector(0,1.5,0), radius=r, color=color.cyan, vel=vector(0,0,0), a=vector(0,-g,0), mass=0.1)
table=label(pos=vector(0,-4,0), text="energy", height=20, color=color.cyan)

floor=box(pos=vector(0,-0.005,0), size=vector(8,0.01,1))
balls=[ball1, ball2, ball3]

def collision(a, b):
    return abs(a.pos.y - b.pos.y) <= 2*r

t=0
dt=0.001
sleep(1)
while t<=60:
    if collision(ball1, ball2):
        vel1=ball1.vel
        vel2=ball2.vel
        ball1.vel = (ball1.mass - ball2.mass) / (ball1.mass + ball2.mass) * ball1.vel + 2 * ball2.mass * ball2.vel / (
                    ball1.mass + ball2.mass)
        ball2.vel = 2 * ball1.mass / (ball1.mass + ball2.mass) * vel1 + (ball2.mass - ball1.mass) / (
                    ball1.mass + ball2.mass) * ball2.vel
    if collision(ball2, ball3):
        vel2=ball2.vel
        vel3=ball3.vel
        ball2.vel = (ball2.mass - ball3.mass) / (ball2.mass + ball3.mass) * ball2.vel + 2 * ball3.mass * ball3.vel / (
                    ball2.mass + ball3.mass)
        ball3.vel = 2 * ball2.mass / (ball2.mass + ball3.mass) * vel2 + (ball3.mass - ball2.mass) / (
                    ball2.mass + ball3.mass) * ball3.vel
    if abs(ball1.pos.y-floor.pos.y) <= r+floor.pos.y/2:
        ball1.vel= -ball1.vel

    for ball in balls:
        ball.vel+=ball.a*dt
        ball.pos+=ball.vel*dt

    ball1e = ball1.mass * ((g * ball1.pos.y) + 0.5 * ball1.vel.y ** 2)
    ball2e = ball2.mass * ((g * ball2.pos.y) + 0.5 * ball1.vel.y ** 2)
    ball3e = ball1.mass * ((g * ball3.pos.y) + 0.5 * ball3.vel.y ** 2)
    energy = ball1e+ball2e+ball3e
    table.text = "energy: " + '%.4f' % energy + "  y3: " + '%.4f' %ball3.pos.y
    f2.append(ball2.pos.y)
    f3.append(ball3.pos.y)
    t+=dt


for x in arange(0,60,0.1):
    pf2.plot(pos=(x,f2[int(x*100)]))
    pf3.plot(pos=(x,f3[int(x*100)]))



