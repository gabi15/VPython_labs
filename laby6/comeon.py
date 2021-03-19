import numpy as np
import matplotlib.pyplot as plt
plt.style.use('classic')

bx = 0
by = 0
pix = 100000
X=[]
Y=[]
count = 0

ax = plt.gca()
ax.set_facecolor("black")


while count <= pix:
    x=0
    y=0
    shot = np.random.randint(1, 100)
    if shot<=7:
        x = 0.2*bx - 0.26 * by
        y = 0.23*bx + 0.22*by + 1.6
    elif shot > 7 and shot <= 14:
        x= -0.15 *bx + 0.28 * by
        y= 0.26 * bx + 0.24 * by + 0.44
    elif shot == 15:
        x=0
        y=0.16*by
    else:
        x = 0.85*bx+0.04*by
        y = -0.04 * bx + 0.85 * by + 1.6
    if x < 1.5 and x > 1 and y < 4.5 and y > 4:
        count += 1
        X.append(x)
        Y.append(y)
    bx = x
    by = y


plt.plot(X, Y, ',', color="lime")
plt.plot([1,1.5],[4.5,4.5],'r-',lw=3)
plt.plot([1.5,1.5],[4,4.5],'r-',lw=3)
plt.plot([1,1.5],[4,4],'r-',lw=3)
plt.plot([1,1],[4,4.5],'r-',lw=3)

plt.axis([1,1.5,4,4.5])
plt.savefig('beautiful_part1.png', format='png')
plt.show()