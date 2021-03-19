import numpy as np
import matplotlib.pyplot as plt
plt.style.use('classic')

Y = []
Ns = [10,100,400,1000,2500,10000]
i = 0
for n in Ns:
    exp_squared = []
    for el in range(500):
        Xr = np.random.choice([-1, 1], n)
        exp_squared.append(np.sum(Xr)*np.sum(Xr))
    Y.append(np.sqrt(sum(exp_squared)/500))
    plt.plot(Ns[i], Y[i], 'o', color="red")
    i += 1

plt.plot(Ns, Y)
plt.savefig('stats.png', format="png")
plt.show()
