n=10000
for i in range(1,n):
    sum=0
    for e in range(1,i):
        if i%e == 0:
            sum+= e
    if sum == i:
        print(i)