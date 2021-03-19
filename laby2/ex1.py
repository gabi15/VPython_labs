import math
import random
r=1
circle=0
f= open('first.txt','w')
for i in range(1,1000001):
    x =random.uniform(-1,1)
    y = random.uniform(-1, 1)
    d=math.sqrt(abs(x)**2+abs(y)**2)
    if d<=r:
        circle+=1
    cpi=4*circle/i
    if(i<=100 or i==1000 or i==10000 or i==100000 or i==1000000):
        f.write(str(i)+') '+ str(cpi)+'   '+str(cpi/math.pi)+'\n')

f.close()




