# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?
def problem_3(n):

    prime_factors = []
    factor = 2

    while n != 1:
        if n % factor == 0:
            prime_factors.append(factor)
            n = n / factor

        else:
            factor += 1

    print(max(prime_factors))


problem_3(600851475143)
