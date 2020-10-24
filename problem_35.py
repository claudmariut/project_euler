"""
The number, 197, is called a circular prime because all rotations of
the digits: 197, 971, and 719, are themselves prime.
There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.
How many circular primes are there below one million?
"""
import os
import time
start = time.time()


def find_primes_sieve():
    """Return list with primes bellow 1_000_000"""
    n = 1_000_000
    sieve = [True] * n
    primes_list = []
    for prime in range(2, n):
        if sieve[prime]:
            primes_list.append(prime)
            for multiple in range(prime * 2, n, prime):
                sieve[multiple] = False

    return primes_list


def get_num_circular_primes():
    """Return size of circular primes list."""
    circular_primes = []
    primes_list = find_primes_sieve()
    for prime in primes_list:
        size = len(str(prime))
        exponent = pow(10, size - 1)
        condition = True
        for rotation in range(size):
            last = prime % 10
            front = prime // 10
            circular = (last * exponent) + front
            if circular not in primes_list:
                condition = False
                break
            else:
                prime = circular
        if condition:
            circular_primes.append(prime)

    return len(circular_primes)


print(get_num_circular_primes())
print(time.time() - start)
duration = 0.25  # seconds
freq = 440  # Hz
os.system(f'play -nq -t alsa synth {duration} sine {freq}')
