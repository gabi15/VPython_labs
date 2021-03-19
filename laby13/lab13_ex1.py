from vpython import *

scene = canvas(width=1000, height=580)
k = 3
m = 100 ** k

wallR = box(pos=vector(6, 0, 0), size=vector(0.3, 8, 8), color=color.blue)
wallD = box(pos=vector(-2, -4, 0), size=vector(16, 0.3, 8), color=color.yellow)
cube1 = box(pos=vector(0, -4 + 0.3 + 0.25, 0), size=vector(1, 1, 1), vel=vector(1, 0, 0), mass=m)
cube2 = box(pos=vector(2, -4 + 0.3 + 0.25, 0), size=vector(1, 1, 1), vel=vector(0, 0, 0), mass=1)
table=label(pos=vector(2,4,0), text="Collisions", height=20, color=color.cyan)

t = 0
dt = 0.00001
a1 = 0
a2 = 0
count=0


def collision(a, b):
    return abs(a.pos.x - b.pos.x) <= a.size.x / 2 + b.size.x / 2


while True:
    if collision(cube1, cube2):
        vel1=cube1.vel
        vel2=cube2.vel
        cube1.vel = (cube1.mass - cube2.mass) / (cube1.mass + cube2.mass) * cube1.vel + 2 * cube2.mass * cube2.vel / (
                    cube1.mass + cube2.mass)
        cube2.vel = 2 * cube1.mass / (cube1.mass + cube2.mass) * vel1 + (cube2.mass - cube1.mass) / (
                    cube1.mass + cube2.mass) * cube2.vel
        count+=1
    if collision(cube2, wallR):
        cube2.vel = -cube2.vel
        count+=1

    cube1.pos += cube1.vel * dt
    cube2.pos += cube2.vel * dt
    table.text = "collisions counter:" +str(count)
    t+=dt

