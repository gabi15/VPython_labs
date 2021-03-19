x=int(input("type an integer number "))

if x%2==0:
    print("your number is even")
else:
    print("your number is odd")

check=0
for i in range(2,x):
    if x%i==0:
        break
    else:
        check+=1

if check == x-2:
    print("your number is also prime")