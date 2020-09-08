# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see
# that the 6th prime is 13.
# What is the 10 001st prime number?
def problem_7(n):
    primes = []
    flag = True
    number = 2
    while flag:
        count = 0
        for x in range(2, number):
            if number % x == 0:
                count += 1
        if count == 0:
            primes.append(number)
        if len(primes) == n:
            flag = False
        else:
            number += 1

    print(primes[-1])


problem_7(10001)

