with open('input_day13.txt', 'r') as myfile:
    lines = myfile.read().strip().split("\n\n")

true_counter = 0

def Check_Comp(x, y):

    if isinstance(x, list) and isinstance(y, int):
        y = [y]

    if isinstance(x, int) and isinstance(y, list):
        x = [x]

    if isinstance(x, int) and isinstance(y, int):
        if x < y:
            return True
        if x == y:
            return "equal"
        if y < x:
            return False

    if isinstance(x, list) and isinstance(y, list):
        element = 0
        length_first = len(x)
        length_second = len(y)
        while element < length_first and element < length_second:
            result = Check_Comp(x[element], y[element])
            if result == True:
                return True
            if result == False:
                return False

            element += 1

        if element == length_first and element != length_second:
            return True
        if length_first == length_second:
            return "equal"
        if element == length_second and element != length_first:
            return False


for k, tocompare in enumerate(lines):
    x, y = map(eval, tocompare.split("\n"))
    if Check_Comp(x, y):
        true_counter += k + 1

print(true_counter)

# Part 2

from functools import cmp_to_key

with open("input_day13.txt") as myfile:
    lines = myfile.read().strip().replace("\n\n", "\n")


def Check_Comp(x, y):

    if isinstance(x, list) and isinstance(y, int):
        y = [y]

    if isinstance(x, int) and isinstance(y, list):
        x = [x]

    if isinstance(x, int) and isinstance(y, int):
        if x < y:
            return 1
        if x == y:
            return 0
        if y < x:
            return -1

    if isinstance(x, list) and isinstance(y, list):
        element = 0
        length_first = len(x)
        length_second = len(y)
        while element < length_first and element < length_second:
            result = Check_Comp(x[element], y[element])
            if result == 1:
                return 1
            if result == -1:
                return -1

            element += 1

        if element == length_first and element != length_second:
            return 1
        if length_first == length_second:
            return 0
        if element == length_second and element != length_first:
            return -1



data_array = list(map(eval, lines.split("\n")))

data_array.append([[2]])
data_array.append([[6]])


data_array = sorted(data_array, key=cmp_to_key(Check_Comp), reverse=True)

for items, divider_to in enumerate(data_array):
    if divider_to == [[2]]:
        first_divider = items + 1
    if divider_to == [[6]]:
        second_divider = items + 1

result=first_divider * second_divider
print(result)