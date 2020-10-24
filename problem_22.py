"""
Using names.txt (right click and 'Save Link/Target As...'), a 46K text file
containing over five-thousand first names, begin by sorting it into
alphabetical order. Then working out the alphabetical value for each name,
multiply this value by its alphabetical position in the list to obtain a name score.
For example, when the list is sorted into alphabetical order, COLIN, which is
worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list.
So, COLIN would obtain a score of 938 × 53 = 49714.
What is the total of all the name scores in the file?
"""


def sum_string_alpha_number(string):
    """Transforms a string in numbers alphabetically and adds them"""
    sum = 0
    for character in string:
        if character == "A":
            sum += 1
        elif character == "B":
            sum += 2
        elif character == 'C':
            sum += 3
        elif character == 'D':
            sum += 4
        elif character == 'E':
            sum += 5
        elif character == 'F':
            sum += 6
        elif character == 'G':
            sum += 7
        elif character == 'H':
            sum += 8
        elif character == 'I':
            sum += 9
        elif character == 'J':
            sum += 10
        elif character == 'K':
            sum += 11
        elif character == 'L':
            sum += 12
        elif character == 'M':
            sum += 13
        elif character == 'N':
            sum += 14
        elif character == 'O':
            sum += 15
        elif character == 'P':
            sum += 16
        elif character == 'Q':
            sum += 17
        elif character == 'R':
            sum += 18
        elif character == 'S':
            sum += 19
        elif character == 'T':
            sum += 20
        elif character == 'U':
            sum += 21
        elif character == 'V':
            sum += 22
        elif character == 'W':
            sum += 23
        elif character == 'X':
            sum += 24
        elif character == 'Y':
            sum += 25
        elif character == 'Z':
            sum += 26

    return sum


def sum_name_scores(names):
    """Returns the sum of all the names scores"""
    sum = 0
    for index in range(len(names)):
        sum += (sum_string_alpha_number(names[index]) * (index + 1))

    return sum


filename = "text_files/names.txt"
with open(filename) as f:
    names_string = f.read()

names_string = names_string.replace('"', "")
names_list = names_string.split(",")
names_list.sort()

print(sum_name_scores(names_list))

