import random
number=random.randint(1, 20)
print("guess a number between 1 and 20")
x = 0
counter = 0

while x != number:

    x=int(input("your guess: "))
    if number == x:
        print("You won! The number was", number)
    elif number < x:
        print("too large")
    else:
        print("too small")
    counter += 1

print("it took you", counter, "shots")
