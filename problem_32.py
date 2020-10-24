"""
We shall say that an n-digit number is pandigital if it makes use of all the
digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1
through 5 pandigital. The product 7254 is unusual, as the identity,
39 × 186 = 7254, containing multiplicand, multiplier, and product is
1 through 9 pandigital. Find the sum of all products whose
multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.
HINT: Some products can be obtained in more than one way so be sure to only
include it once in your sum.
"""


def get_length_identity(multiplicand, multiplier, product):
    """Get length of identity, return True if 9"""
    len_iden = len(str(multiplicand)) + len(str(multiplier)) + \
               len(str(product))
    if len_iden == 9:
        return True
    else:
        return False


def get_pandigital(multiplicand, multiplier, product):
    """Return True is n is pandigital"""
    check_set = set()
    identity_string = str(multiplicand) + str(multiplier) + str(product)
    identity_int = int(identity_string)
    while identity_int > 0:
        last = identity_int % 10
        check_set.add(last)
        identity_int = identity_int // 10
    check_set.discard(0)
    if len(check_set) == 9:
        return True
    else:
        return False


def get_set_pandigitals():
    """Return set of pandigital identities'product 1 to 9."""
    pandigital_set = set()
    max_range = 10000
    for multiplicand in range(2, 100):
        for multiplier in range(multiplicand, max_range//multiplicand):
            product = multiplicand * multiplier
            if get_length_identity(multiplicand, multiplier, product):
                if get_pandigital(multiplicand, multiplier, product):
                    pandigital_set.add(product)
    return pandigital_set


def get_sum_pandigitals():
    """Return sum of pandigital_set"""
    return sum(get_set_pandigitals())


print(get_sum_pandigitals())
