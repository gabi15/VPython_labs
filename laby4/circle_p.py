import random
import math
import factorial

#print (factorial.factorial(3.5))
r=1
circle=0
dimensions=5
f= open('first.txt','w')

for dim in range(2, dimensions+1):
    shot = 0
    for i in range(1, 1000001):
        square_sum = 0
        L = [random.uniform(-1,1) for i in range(dim)]
        for el in L:
            square_sum += pow(el,2)
        dist = math.sqrt(square_sum)
        if dist <= 1:
            shot += 1
    circle = 2**dim*shot/1000000
    real_val = math.pi**(dim/2)/factorial.factorial(dim/2)
    f.write(str(dim) + ') ' + str(circle) + '   ' + str(circle / real_val) + '    ' + str(shot) + '\n')


f.close()