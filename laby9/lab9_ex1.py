"""In this program the solar system is presented, but from the different perspective"""
from vpython import *

# constants
G = 6.7 * 10 ** -11
M = 2 * 10 ** 30
dt = 3600 * 0.2
year = 365*24 * 5 * dt

scene = canvas(width=550, height=580)

sun = sphere(radius=10**10, pos=vector(0, 0, 0), color=color.yellow, vel=vector(0, 0, 0))
mercury = sphere(radius=5*10**9, pos=vector(70 * 10 ** 9, 0, 0), color=color.green, vel=vector(0, 47 * 10 ** 3, 0),
                 make_trail=True)
venus = sphere(radius=5*10**9, pos=vector(110 * 10 ** 9, 0, 0), color=color.orange, vel=vector(0, 35 * 10 ** 3, 0),
               make_trail=True)
earth = sphere(radius=5* 10**9, pos=vector(150 * 10 ** 9, 0, 0), color=color.blue, vel=vector(0, 30 * 10 ** 3, 0),
               make_trail=True)
mars = sphere(radius=5*10**9, pos=vector(250 * 10 ** 9, 0, 0), color=color.red, vel=vector(0, 24 * 10 ** 3, 0),
              make_trail=True)

planets = [mercury, venus, earth, mars]

def acceleration(planet):
    a = (-G * M * planet.pos) / (mag(planet.pos) ** 3)
    return a

t=0

while t<year:
    rate(10000)
    for planet in planets:
        planet.vel = planet.vel + acceleration(planet)*dt
        planet.pos = planet.pos + planet.vel * dt
    t = t+dt





