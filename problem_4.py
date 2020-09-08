# A palindromic number reads the same both ways. The largest palindrome made
# from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.
palindrome = []
x = 100

while x <= 999:
    for y in range(100, 1000):
        product = x * y
        rev = 0
        number = product
        while number > 0:
            last = number % 10
            rev = (rev * 10) + last
            number = number // 10
        if product == rev:
            palindrome.append(product)
    x += 1

print(max(palindrome))


