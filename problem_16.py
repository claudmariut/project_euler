"""
215 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
What is the sum of the digits of the number 21000?
"""


def sum_digits_power_base_2(n):
    """Returns sum of digits of a number, 2 to the n power"""
    number = pow(2, n)
    sum = 0
    while number > 0:
        last = number % 10
        sum += last
        number = number // 10

    return sum


print(sum_digits_power_base_2(1000))
