import numpy as np
import matplotlib.pyplot as plt
import math
plt.style.use('classic')
plt.rcParams['lines.linewidth'] = 0.1

steps = 100000
colors = ['#DC143C','#8B0000', '#FFD700', '#FF8C00', '#FF6347', '#7CFC00', '#32CD32', '#228B22', '#00FF7F', '#3CB371',
          '#556B2F', '#008080', '#483D8B', '#000080', '#FF1493']


for i in range(15):
    deg = np.random.uniform(0, 2 * np.pi, steps)
    Y = [0]
    X = [0]
    for el in range(1,steps):
        X.append(X[el - 1] + math.cos(deg[el]))
        Y.append(Y[el-1] + math.sin(deg[el]))
    plt.plot(X, Y, color=colors[i])
    plt.plot(X[steps-1], Y[steps-1], 'o', color=colors[i], ms=12),

plt.savefig('spin.png', format="png")
plt.show()
