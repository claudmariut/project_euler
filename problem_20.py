"""
n! means n × (n − 1) × ... × 3 × 2 × 1
For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.
Find the sum of the digits in the number 100!
"""


def factorial(number):
    """Returns factorial of a number"""
    n_factorial = 1
    for n in range(number):
        n_factorial *= (number - n)

    return n_factorial


def sum_digits(n):
    """Returns sum of individual digits of a integer"""
    n = str(n)
    sum = 0
    for digit in range(len(n)):
        sum += int(n[digit])

    return sum


print(sum_digits(factorial(100)))



