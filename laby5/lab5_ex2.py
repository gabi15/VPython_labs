import numpy as np

people = 366
n = 100

f = open("triplets.txt", "w")

for p in range(2, people+1):
    success = 0
    for room in range(n):
        counter = 0
        A = np.random.randint(1,365,(p))
        A.sort()
        for i in range(p-1):
            if A[i] == A[i+1]:
                counter += 1
                if counter == 2: # 2 for 3 people, 3 for 4 people etc.
                    success += 1
                    break
            else:
                counter = 0

    f.write(str(p)+") at least three (or four) people have birthday at the same day, probability: "+str(success/n)+"\n")

f.close()


