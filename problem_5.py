# 2520 is the smallest number that can be divided by each of the numbers from 1
# to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the
# numbers from 1 to 20?
number = 1
flag = True
while flag:
    count = 0
    for x in range(1, 14):
        if number % x != 0:
            count += 1
    if count == 0:
        print(number)
        flag = False
    else:
        number += 1
