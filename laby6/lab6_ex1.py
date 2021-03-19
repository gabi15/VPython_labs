import numpy as np
import matplotlib.pyplot as plt
plt.style.use('classic')

bx = 0
by = 0
pix = 1000000

ax = plt.gca()
ax.set_facecolor("black")
X = []
Y = []

for n in range(pix):
    x = 0
    y = 0
    shot = np.random.randint(1, 100)
    if shot <= 7:
        x = 0.2 * bx - 0.26 * by
        y = 0.23*bx + 0.22*by + 1.6
    elif 7 < shot <= 14:
        x = -0.15 * bx + 0.28 * by
        y = 0.26 * bx + 0.24 * by + 0.44
    elif shot == 15:
        x = 0
        y = 0.16*by
    else:
        x = 0.85*bx+0.04*by
        y = -0.04 * bx + 0.85 * by + 1.6
    bx = x
    by = y
    X.append(x)
    Y.append(y)

plt.plot(X, Y, ',', color="lime")
plt.plot([1, 1.5], [4.5, 4.5], 'r-', lw=3)
plt.plot([1.5, 1.5],[4, 4.5], 'r-', lw=3)
plt.plot([1, 1.5],[4, 4], 'r-', lw=3)
plt.plot([1, 1], [4, 4.5], 'r-', lw=3)


plt.savefig('beautiful.png', format='png')
plt.show()

