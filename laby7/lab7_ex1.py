import numpy as np
import matplotlib.pyplot as plt
plt.style.use('classic')
plt.rcParams['lines.linewidth'] = 1

x = 100000
X=np.arange(x)

for i in range(15):
    Yr=np.random.choice([-1,1],x)
    Y=[0]
    Y[0]=Yr[0]
    for el in range(1,x):
        Y.append(Y[el-1]+Yr[el])
    plt.plot(X, Y)

plt.savefig('flip.png', format="png")
plt.show()
