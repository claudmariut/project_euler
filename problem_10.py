"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.
"""
import time
start = time.time()


# Using Sieve of Eratosthenes Algorithm.
def prime_sieve(n):
    """Returns a list with primes under a given number"""
    primes = []
    sieve = n * [True]  # [] To create a list with Trues. (BitArray)
    for prime in range(2, n):
        if sieve[prime]:
            primes.append(prime)
            for multiple in range(2 * prime, n, prime):  # Discard multiples.
                sieve[multiple] = False
    return primes


def sum_primes(bellow_n):
    """Returns the sum of the primes bellow a given number"""
    primes_sum = sum(prime_sieve(bellow_n))
    return primes_sum


print(sum_primes(2_000_000))
print(time.time() - start)






