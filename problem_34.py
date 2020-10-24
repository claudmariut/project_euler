"""
145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.
Find the sum of all numbers which are equal to the sum of the
factorial of their digits.
Note: As 1! = 1 and 2! = 2 are not sums they are not included.
In particular, note that the largest 7-digit number maps to 2540160,
which while it is also a 7-digit number is significantly less than the
corresponding integer 9999999. The 8-digit equivalent doesn’t even reach an
8-digit factorial sum. To summarise, 7×9! can be considered an upper-bound in
a search as anything higher can be seen to exceed the sum of the digit
factorials of that number. Max number < 10_000_000
"""
import time
import math
import os

duration = 0.25  # seconds
freq = 440  # Hz
start = time.time()


def get_sum_digit_factorial(n):
    """Return sum of factorials of digit."""
    sum = 0
    while n != 0:
        last = n % 10
        sum += math.factorial(last)
        n //= 10

    return sum


def sum_num():
    """Return sum of numbers that pass condition."""
    sum = 0
    for num in range(3, 2_540_161):
        if num == get_sum_digit_factorial(num):
            sum += num

    return sum


print(sum_num())
print(time.time() - start)
os.system(f'play -nq -t alsa synth {duration} sine {freq}')
