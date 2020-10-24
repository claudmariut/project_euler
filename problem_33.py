"""
The fraction 49/98 is a curious fraction, as an inexperienced mathematician in
attempting to simplify it may incorrectly believe that 49/98 = 4/8, which is
correct, is obtained by cancelling the 9s.
We shall consider fractions like, 30/50 = 3/5, to be trivial examples.
There are exactly four non-trivial examples of this type of fraction, less than
one in value, and containing two digits in the numerator and denominator.
If the product of these four fractions is given in its lowest common terms,
find the value of the denominator.
"""
import time

start = time.time()


def fraction_generator():
    """Get possible numerator and denominator combinations under conditions."""
    denominators = [x for x in range(10, 100) if x % 10 != 0]
    for den in denominators:
        for num in range(10, 2 * den):
            if num % 10 != 0 and num < 100 and num != den:
                yield num, den


def division_comparator():
    """Compare divisions if conditions are True."""
    num_den = div.__next__()
    num = str(num_den[0])
    den = str(num_den[1])
    division1 = int(num) / int(den)
    if num[0] in den and num[1] in den:
        return False
    elif num[0] == den[0]:
        num = num[1]
        den = den[1]
    elif num[0] == den[1]:
        num = num[1]
        den = den[0]
    elif num[1] == den[0]:
        num = num[0]
        den = den[1]
    elif num[1] == den[1]:
        num = num[0]
        den = den[0]
    else:
        return False

    division2 = int(num) / int(den)
    if division1 == division2:
        return num_den


def find_den_product():
    """Find reduce den of product in digit canceling fractions."""
    list_can_frac = []
    while True:
        result = division_comparator()
        if result:
            list_can_frac.append(result)
        if len(list_can_frac) == 4:
            break

    num = 1
    den = 1
    for x in range(4):
        num *= list_can_frac[x][0]
        den *= list_can_frac[x][1]

    for x in range(den, 0, -1):
        if num % x == 0 and den % x == 0:
            print(den / x)
            break


div = fraction_generator()
find_den_product()
print(time.time() - start)

