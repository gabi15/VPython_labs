import math
f=open('third','w')
L=[x*2*math.pi/50 for x in range(51)]
for i in L:
    y=50*math.sin(i)
    yy=int(y)
    if yy>0:
        f.write(yy*'+'+'\n')
    elif yy<0:
        f.write(abs(yy)*'-'+'\n')
    else:
        f.write('0\n')

f.close()