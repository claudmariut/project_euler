"""
The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.
Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.
(Please note that the palindromic number, in either base, may not include leading zeros.)
"""
import time
start = time.time()


def doubleBasePalindorme(n):
    """Find palindromes bellow n number, both base 10 and base 2 of n."""
    dbPalindromes = []
    for x in range(n):
        if checkBinaryPalindrome(x) and checkBase10Palindrome(x):
            dbPalindromes.append(x)

    return dbPalindromes


def checkBase10Palindrome(n):
    """Returns true if n is palindorme"""
    sum = 0
    number = n
    while (number > 0):
        last = number % 10
        next = number // 10
        sum = (sum * 10) + last
        number = next
    if sum == n:
        return True


def checkBinaryPalindrome(n):
    """Returns true if binary form of n is palindrome."""
    if bin(n)[2:] == bin(n)[:1:-1]:
        return True


print(sum(doubleBasePalindorme(1_000_000)))
print(time.time() - start)
