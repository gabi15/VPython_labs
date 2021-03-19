import numpy as np

people = 366
n = 500

f = open("pairs.txt", "w")

for p in range(2,people+1):
    success=0
    for room in range(n):
        A = np.random.randint(1,365,(p))
        B = A.reshape(p,1)
        C = A==B
        found = C.sum()-p
        if found>0:
            success += 1
    f.write(str(p)+") at least two people have birthday the same day, probability: "+str(success/n)+"\n")

f.close()
