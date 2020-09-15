"""
n → n/2 (n is even)
n → 3n + 1 (n is odd)
13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
Which starting number, under one million, produces the longest chain?
"""
import time
start = time.time()


def chain_generator(n):
    """Generates a chain and returns its length"""
    chain = [n]
    result = 0
    while result != 1:
        if n % 2 == 0:
            n = n / 2
            chain.append(n)
            result = n
        else:
            n = (3 * n) + 1
            chain.append(n)
            result = n

    return len(chain)


def chain_comparator(maximum_number):
    """Compares the length of the different generated chains."""
    maximum_length = 0
    longest_starting = 0
    for starting_num in range(500000, maximum_number):
        if chain_generator(starting_num) > maximum_length:
            maximum_length = chain_generator(starting_num)
            longest_starting = starting_num

    print(longest_starting)
    print(time.time() - start)


chain_comparator(1000000)



