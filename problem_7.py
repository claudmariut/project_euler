# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see
# that the 6th prime is 13.
# What is the 10 001st prime number?


# Using Sieve of Eratosthenes Algorithm.
def prime_sieve_position(position):
    """Returns the value of a prime in a given index"""
    n = 200000
    primes = []
    sieve = n * [True]  # [] To create a list with Trues. (BitArray)
    for prime in range(2, n):
        if sieve[prime]:
            primes.append(prime)
            if len(primes) == position:
                print(primes[-1])
                break
            for multiple in range(2 * prime, n, prime):  # Discard multiples.
                sieve[multiple] = False


prime_sieve_position(10001)





