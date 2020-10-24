"""
The Fibonacci sequence is defined by the recurrence relation:
Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
What is the index of the first term in the Fibonacci sequence to
contain 1000 digits?
"""


def fibonacci_generator():
    """Generates fibonacci_sequence"""
    fib_2 = 0
    fib_1 = 1
    yield fib_1
    while True:
        fib_seq = fib_1 + fib_2
        yield fib_seq
        fib_2 = fib_1
        fib_1 = fib_seq


def count_digits_number(number):
    """Return the number of digits of a number"""
    return len(str(number))


def find_index_ndigit_term(n):
    """Return index of first fibonacci term with n digits"""
    gen_object = fibonacci_generator()
    index = 1
    while True:
        index_len = count_digits_number(gen_object.__next__())
        if index_len == n:
            return index
        else:
            index += 1


print(find_index_ndigit_term(1000))


