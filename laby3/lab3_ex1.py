"""You flip a coin, heads are one step forward, tails backward.
How many flips do you need to cover the distance of N steps in one way?"""

import time
import random
N = left = right = 20
counter = tries = 0
print((N-1)*' ',"START", (N-1)*' ')
print('|', left*' ', '*', right*' ', '|', counter)
a_count = 0


while abs(counter)<N:
    shot = random.randrange(-1, 2, 2)
    if shot == 1:
        left += 1
        right -= 1
    else:
        left -= 1
        right += 1
    counter += shot
    if counter > 0:
        pcounter = '+'+str(counter)
    else:
        pcounter = str(counter)
    tries += 1
    print('|', left*' ', '*', right*' ', '|', pcounter)
    time.sleep(0.1)


print('BOOM')
print("It took", tries, "coin flips")



