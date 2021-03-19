# Fermat's Last Theorem, formulated in 1637,
# states that no three distinct positive integers a, b, and c can satisfy the equation
# a^n+b^n=c^n
# if n is an integer greater than two (n > 2).

for i in range(2,7):
    print("printing for power", i, ":")
    for a in range(1,101):
        for b in range(a,101):
            c = (a**i+b**i)**(1/i)
            if c % 1 == 0:
                print(a, "^", i, '+', b, '^', i, '=', int(c), "^", i)
