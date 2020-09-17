"""
What is the greatest product of four adjacent numbers in the same
direction (up, down, left, right, or diagonally) in the 20×20 grid?
"""

# Format the number in an array of 20x20.
with open("text_files/problem_11.txt") as file_object:
    temp_array_string = []
    temp_array_int = []
    array = []
    for line in file_object:
        # Array of strings with each number in line.
        temp_array_string = line.split()
        # Array with integers of each line.
        temp_array_int = list(map(int, temp_array_string))
        array.append(temp_array_int)

products = []
# Check Left/Right.
for r in range(20):
    for c in range(17):
        temp_prod = array[r][c]*array[r][c+1]*array[r][c+2]*array[r][c+3]
        products.append(temp_prod)

# Check Up/Down.
for c in range(20):
    for r in range(17):
        temp_prod = array[r][c]*array[r+1][c]*array[r+2][c]*array[r+3][c]
        products.append(temp_prod)

# Check Diagonally. (UpLeft - DownRight)
for c in range(17):
    for r in range(17):
        temp_prod = array[c][r]*array[c+1][r+1]*array[c+2][r+2]*array[c+3][r+3]
        products.append(temp_prod)

# Check Diagonally. (DownLeft to UpRight)
for c in range(3, 20):
    for r in range(0, 17):
        temp_prod = array[c][r]*array[c-1][r+1]*array[c-2][r+2]*array[c-3][r+3]
        products.append(temp_prod)


print(max(products))




