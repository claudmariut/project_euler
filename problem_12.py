"""
What is the value of the first triangle number to have over
 five hundred divisors?
 """

import time
start = time.time()


def find_divisors(div):
    """Find numbers of factors of one number"""
    counter_factor = 0
    for factor in range(1, div + 1):
        if div % factor == 0:
            counter_factor += 1
    return counter_factor


def triangle_numbers(maximum_divisors):
    n = 1
    while True:
        factors = 0
        if n % 2 == 0:
            factors = find_divisors(int(n/2)) * find_divisors(n + 1)
        else:
            factors = find_divisors(n) * find_divisors(int((n + 1) / 2))
        if factors > maximum_divisors:
            print(time.time() - start)
            print(int((n * (n + 1))/2))
            break
        else:
            n += 1


triangle_numbers(500)

