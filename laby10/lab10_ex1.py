from vpython import *

#constants
m=0.01
k=1
N=10
t=0
dt=0.001

scene = canvas(width=1500, height=580)

balls=[]
springs=[]
forces=[]
wallL = box(pos=vector(-4,0,0), size=vector(0.1, 2, 2), color=color.green)
wallR = box(pos=vector(4,0,0), size=vector(0.1,2,2), color=color.green)
table=label(pos=vector(1,-1.4,0), text="Energies", height=20, color=color.cyan)

distance=8

# APPENDING BALLS
balls.append(sphere(radius=0.15, pos=vector(-4+distance/(N+1),3,0), vel=vector(0,0,0)))
for ball in range(1,N-1):
    balls.append(sphere(radius=0.15, pos=vector(-4+distance/(N+1)*(ball+1),0,0), vel=vector(0,0,0)))

balls.append(sphere(radius=0.15, pos=vector(4-distance/(N+1),-1,0), vel=vector(0,0,0)))

# APPENDING HELIXES
hel_length=distance/(N+1)-balls[0].radius
for spring in range(N+1):
    springs.append(helix(pos=vector(-4+hel_length*spring,0,0),axis=vector(hel_length,0,0), radius=0.1, color=color.cyan))

#APPENDING FORCES
forces.append(k*(wallL.pos+balls[1].pos-2*balls[0].pos))

for i in range(N-2):
    forces.append(k*(balls[i].pos+balls[i+2].pos-2*balls[i+1].pos))

forces.append(k*(balls[N-2].pos+wallR.pos-2*balls[N-1].pos))

while True:
    rate(200)
    # FIRST BALL
    a_0=forces[0]/m
    balls[0].vel+=a_0*dt
    balls[0].pos+=balls[0].vel * dt
    # FIRST SPRING
    springs[0].axis=balls[0].pos-wallL.pos
    # REST OF THE BALLS
    for i in range(1,N-1):
        a_1=forces[i]/m
        balls[i].vel+=a_1*dt
        balls[i].pos+=balls[i].vel*dt

    # REST OF THE SPRINGS
    for i in range(1,N):
        springs[i].pos = balls[i - 1].pos
        springs[i].axis = balls[i].pos - balls[i - 1].pos
    # LAST BALL
    a_N= forces[N-1]/m
    balls[N-1].vel+=a_N*dt
    balls[N-1].pos+=balls[N-1].vel*dt
    # LAST SPRING
    springs[N].pos = balls[N - 1].pos
    springs[N].axis=wallR.pos-balls[N-1].pos
    # UPDATING FORCES
    forces[0] = k * (wallL.pos + balls[1].pos - 2 * balls[0].pos)
    for i in range(1,N-1):
        forces[i] = k * (balls[i - 1].pos + balls[i + 1].pos - 2 * balls[i].pos)
    forces[N - 1] = k * (balls[N - 2].pos + wallR.pos - 2 * balls[N - 1].pos)

    #Energies
    v_squared=0
    mag_squared=0
    for ball in balls:
        v_squared+=(mag(ball.vel))**2

    for helix in springs:
        mag_squared+=(mag(helix.axis))**2

    table.text = 'Ekin = '+ '%.4f'%(v_squared*m/2) +'\n'+\
        'Epot='+'%.4f'%(mag_squared*k/2) +'\n '+\
        'Ep + Ek = ' + '%.4f'%(v_squared*m/2+ mag_squared*k/2)

    t += dt
