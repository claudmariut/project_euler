"""
For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55
and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71
and 142; so d(284) = 220.
Evaluate the sum of all the amicable numbers under 10000.
"""


def amicable_checker(n):
    """Returns if a number amicable and if so, its pair."""
    amicable_01 = 0
    for divisor in range(1, n):
        if n % divisor == 0:
            amicable_01 += divisor
    amicable_02 = 0
    if n == amicable_01:
        return False
    for divisor in range(1, amicable_01):
        if amicable_01 % divisor == 0:
            amicable_02 += divisor
    if n == amicable_02:
        return amicable_01 and n  # To return them separately
    else:
        return False


def sum_amicable(n):
    """Returns the sum of all the amicable numbers under given n"""
    set_amicable = set()
    for x in range(1, n):
        if amicable_checker(x):  # If is True, or not False
            set_amicable.add(amicable_checker(x))

    return sum(set_amicable)


print(sum_amicable(10_000))
