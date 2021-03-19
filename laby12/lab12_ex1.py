from vpython import *
import math
scene = canvas(width=800, height=800)
rad = 0.2
L = 1
dt = 0.001
alpha=calpha = math.pi
beta=cbeta = math.pi - 0.1
wa = wb =0 # angular velocity
cwa = cwb = 0 # angular aceleration
g = 9.8
cg = 9.80000000000001

#copy pendulum
cbar_1 = cylinder(radius=0.01, pos=vector(0, 0, 0), axis=vector(0, 1, 0), color=color.yellow, length=L)
cball_1 = sphere(radius=rad, pos=vector(L * sin(calpha), -L * cos(calpha), 0), color=color.red, vel=0)
cball_2 = sphere(radius=rad, pos=vector(L * (sin(cbeta) + sin(calpha)), -L * (cos(cbeta) + cos(calpha)), 0), color=color.red)
cbar_2 = cylinder(radius=0.01, pos=cball_2.pos, axis=vector(cball_1.pos-cball_2.pos), color=color.yellow, length=L)

#front pendulum
bar_1 = cylinder(radius=0.01, pos=vector(0, 0, 0), axis=vector(0, 1, 0), color=color.yellow, length=L)
ball_1 = sphere(radius=rad, pos=vector(L * sin(calpha), -L * cos(calpha), 0), color=color.blue, vel=0)
ball_2 = sphere(radius=rad, pos=vector(L * (sin(cbeta) + sin(calpha)), -L * (cos(cbeta) + cos(calpha)), 0), color=color.blue)
bar_2 = cylinder(radius=0.01, pos=cball_2.pos, axis=vector(cball_1.pos-cball_2.pos), color=color.yellow, length=L)

#table
table=label(pos=vector(2,-1.4,0), text="Energies", height=20, color=color.cyan)


t=0
while True:
    rate(800)
    caa = (-cg / L * (2 * sin(calpha) - sin(cbeta) * cos(calpha - cbeta)) - wa ** 2 * sin(
        2 * calpha - 2 * cbeta) / 2 - wb * wb * sin(calpha - cbeta)) / (1 + sin(calpha - cbeta) ** 2)
    cab = (-cg / L * (2 * sin(cbeta) - 2 * sin(calpha) * cos(calpha - cbeta)) + wb * wb * sin(
        2 * calpha - 2 * cbeta) / 2 + 2 * wa * wa * sin(calpha - cbeta)) / (1 + sin(calpha - cbeta) ** 2)
    cwa = cwa+caa*dt
    cwb = cwb+cab*dt
    calpha += cwa * dt
    cbeta += cwb * dt
    cball_1.pos=vector(L * sin(calpha), -L * cos(calpha), 0)
    cball_2.pos=vector(L * (sin(calpha) + sin(cbeta)), -L * (cos(calpha) + cos(cbeta)), 0)
    cbar_1.axis=cball_1.pos
    cbar_2.pos=cball_2.pos
    cbar_2.axis= vector(cball_1.pos-cball_2.pos)

    aa = (-g / L * (2 * sin(alpha) - sin(beta) * cos(alpha - beta)) - wa **2 * sin(
        2 * alpha - 2 * beta) / 2 - wb * wb * sin(alpha - beta))/(1+sin(alpha-beta)**2)
    ab = (-g / L * (2 * sin(beta) - 2 * sin(alpha) * cos(alpha - beta)) + wb * wb * sin(
        2 * alpha - 2 * beta) / 2 + 2 * wa * wa * sin(alpha - beta))/(1+sin(alpha-beta)**2)
    wa = wa+aa*dt
    wb = wb+ab*dt
    alpha += wa*dt
    beta += wb*dt
    ball_1.pos=vector(L*sin(alpha), -L*cos(alpha), 0)
    ball_2.pos=vector(L*(sin(alpha)+sin(beta)), -L*(cos(alpha)+cos(beta)), 0)
    bar_1.axis=ball_1.pos
    bar_2.pos=ball_2.pos
    bar_2.axis= vector(ball_1.pos-ball_2.pos)

    energy = g*(ball_1.pos.y+ball_2.pos.y)+0.5*L**2*(2*wa**2 + wb**2+2*wb*wa*cos(alpha-beta))
    table.text = 'Energy= ' + '%.4f' % energy
    t += dt

