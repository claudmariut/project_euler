"""
Work out the first ten digits of the sum of the following
one-hundred 50-digit numbers.
"""

with open("text_files/problem_13.txt") as file_object:
    lines = file_object.readlines()

sum_number = 0
for line in lines:
    sum_number += int(line)  # Discards whitespace.

result = str(sum_number)
print(result[:10])


