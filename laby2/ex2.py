import math
f=open('second.txt','w')
L=[4*(1/x*(-1)**(x//2)) for x in range(1,20000001,2)]
suma=0
for i,value in enumerate(L,1):
    suma+=value
    if(i<=100 or i==1000 or i==10000 or i==100000 or i==1000000 or i==10000000):
        f.write(str(i)+') '+str(suma)+' '+str(suma/math.pi)+'\n')

f.close()
