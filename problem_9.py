from math import sqrt

# List with all c exponent 2.
c = [x**2 for x in range(1000)]
a = 1
b = 1
flag = True

while a <= 1000:
    while b <= 1000 and flag:
        result = ((a ** 2) + (b ** 2))
        if result in c:
            if a + b + sqrt(result) == 1000:
                print(f"a = {a}, b = {b}, c = {sqrt(result)} ")
                print(a * b * sqrt(result))
                flag = False

            else:
                b += 1
        else:
            b += 1
    a += 1
    b = 1



