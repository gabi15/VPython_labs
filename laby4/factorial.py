import math
import numpy as np


def factorial(num):
    if num == 1:
        return 1
    elif num % 1 != 0:
        base = math.sqrt(math.pi)/2
        x = np.linspace(1.5, num, num)
        for i in x:
            base = base*i
        return base
    else:
        basei = 1
        for i in range(2,int(num+1)):
            basei = basei*i
        return basei