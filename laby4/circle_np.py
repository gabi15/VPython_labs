import numpy as np
import factorial.py
dimensions=20
f = open('second.txt','w')

for dim in range(2, dimensions+1):
    L = np.random.uniform(-1, 1, (1000000, dim))
    L_squared = L**2
    dist = L_squared.sum(axis=1)
    yes = (dist <= 1)
    no = (dist > 1)
    dist[yes] = 1
    dist[no] = 0
    shot = dist.sum()
    circle = 2 ** dim * shot / 1000000
    real_val = np.pi ** (dim / 2) / factorial.factorial(dim / 2)
    f.write(str(dim) + ') ' + str(circle) + '   ' + str(circle / real_val) + '    ' + str(int(shot)) + '\n')

f.close()
