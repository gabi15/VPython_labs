import matplotlib.pyplot as plt
import random
import time
start = time.time()
X = [0]
Y = [0]
count = 0
last_x = 0
last_y = 0
while count<1000000:
    num = random.uniform(0,100)
    if num<1.0:
        x = 0
        y = 0.16*last_y
    elif num<86.0:
        x = 0.85*last_x+0.04*last_y
        y = -0.04*last_x+0.85*last_y+1.6
    elif num<93.0:
        x = 0.2*last_x-0.26*last_y
        y = 0.23*last_x+0.22*last_y+1.6
    else:
        x = -0.15*last_x+0.28*last_y
        y = 0.26*last_x+0.24*last_y+0.44
    if(x<=1.5 and x>=1.0 and y>=2.0 and y<=3.0):
        count = count+1
        X.append(x)
        Y.append(y)
    last_x = x
    last_y = y
    
print(time.time()-start)
plt.axis([1,1.5,2,3])

ax = plt.gca()
ax.set_facecolor('black')
plt.plot(X,Y,',',color = "lime",zorder=1)

plt.savefig("myfig_2.png",format='png')
plt.show()


