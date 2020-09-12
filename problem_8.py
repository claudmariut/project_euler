# The four adjacent digits in the 1000-digit number that have the greatest
# product are 9 × 9 × 8 × 9 = 5832.
# Find the thirteen adjacent digits in the 1000-digit number that have the
# greatest product. What is the value of this product?

# Open file with raw number
with open("text_files/problem_8.txt") as file_object:
    lines = file_object.readlines()

# Format number in a single string
string = ''
for line in lines:
    string += line.strip()

# Create a list with each digit.
list_integer = []
for x in string:
    list_integer.append(int(x))  # Append integers, not characters.

# Create new list with each 13 values product.
list_integer_1 = list_integer[:]
product_list = []
while len(list_integer_1[:]) >= 13:
    splitted = list_integer_1[:13]
    product = 1

    for digit in splitted:
        product *= digit

    product_list.append(product)

    list_integer_1.pop(0)

max_product = max(product_list)
print(max_product)

# Find the set of the thirteen numbers.
flag = True
while flag:
    splitted = list_integer[:13]
    product = 1

    for digit in splitted:
        product *= digit

        if product == 23514624000:
            print(splitted)
            flag = False

    list_integer.pop(0)

