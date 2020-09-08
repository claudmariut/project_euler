# Find the difference between the sum of the squares of the first one hundred
# natural numbers and the square of the sum.
squares = [x * x for x in range(1, 101)]
sum_squares = (sum(squares))

add = [x for x in range(1, 101)]
sum_add = (sum(add))**2

print(sum_add - sum_squares)

# 2 Way. Shortest and smartest.
sum = 0
sqrt = 0
for x in range(1, 101):
    sum = sum + x
    sqrt = sqrt + x**2

print(sum**2 - sqrt)


