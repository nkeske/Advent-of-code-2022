import re

with open('input_day11.txt', 'r') as myfile:
    lines = myfile.read().strip().split()
data_list = []

for line in lines:
    new_line = (re.sub(",", "", line))
    data_list.append(new_line)
result_list = []
monkey_0 = []
monkey_1 = []
monkey_2 = []
monkey_3 = []
monkey_4 = []
monkey_5 = []
monkey_6 = []
monkey_7 = []

for i in range(0, data_list.index('1:')):
    if data_list[i].isdigit():
        monkey_0.append(data_list[i])
    elif data_list[i] == 'Operation:':
        break
for i in range(data_list.index('1:'), data_list.index('2:')):
    if data_list[i].isdigit():
        monkey_1.append(data_list[i])
    elif data_list[i] == 'Operation:':
        break
for i in range(data_list.index('2:'), data_list.index('3:')):
    if data_list[i].isdigit():
        monkey_2.append(data_list[i])
    elif data_list[i] == 'Operation:':
        break
for i in range(data_list.index('3:'), data_list.index('4:')):
    if data_list[i].isdigit():
        monkey_3.append(data_list[i])
    elif data_list[i] == 'Operation:':
        break
for i in range(data_list.index('4:'), data_list.index('5:')):
    if data_list[i].isdigit():
        monkey_4.append(data_list[i])
    elif data_list[i] == 'Operation:':
        break
for i in range(data_list.index('5:'), data_list.index('6:')):
    if data_list[i].isdigit():
        monkey_5.append(data_list[i])
    elif data_list[i] == 'Operation:':
        break
for i in range(data_list.index('6:'), data_list.index('7:')):
    if data_list[i].isdigit():
        monkey_6.append(data_list[i])
    elif data_list[i] == 'Operation:':
        break
for i in range(data_list.index('7:'), len(data_list)):
    if data_list[i].isdigit():
        monkey_7.append(data_list[i])
    elif data_list[i] == 'Operation:':
        break

inspect_counter0 = 0
inspect_counter1 = 0
inspect_counter2 = 0
inspect_counter3 = 0
inspect_counter4 = 0
inspect_counter5 = 0
inspect_counter6 = 0
inspect_counter7 = 0

for round in range(0, 20):
    # For monkey 0
    for item in monkey_0:
        for i in range(0, data_list.index('1:')):
            if data_list[i] == '=':
                if data_list[i + 1] == 'old':
                    to_operate1 = int(item)
                else:
                    to_operate1 = int(data_list[i + 1])
                if data_list[i + 3] == 'old':
                    to_operate2 = int(item)
                else:
                    to_operate2 = int(data_list[i + 3])
                if data_list[i + 2] == '+':
                    result = to_operate1 + to_operate2
                    result_after_bored = result // 3
                    result_list.append(result_after_bored)
                elif data_list[i + 2] == '*':
                    result = to_operate1 * to_operate2
                    result_after_bored = result // 3
                    result_list.append(result_after_bored)

    for item2 in result_list:
        for i in range(0, data_list.index('1:')):
            if data_list[i] == 'by':
                division = int(data_list[i + 1])
                if item2 % division == 0:
                    throw_monkey = int(data_list[i + 7])
                    inspect_counter0 += 1
                    if throw_monkey == 0:
                        monkey_0.append(item2)

                    elif throw_monkey == 1:
                        monkey_1.append(item2)

                    elif throw_monkey == 2:
                        monkey_2.append(item2)

                    elif throw_monkey == 3:
                        monkey_3.append(item2)

                    elif throw_monkey == 4:
                        monkey_4.append(item2)

                    elif throw_monkey == 5:
                        monkey_5.append(item2)

                    elif throw_monkey == 6:
                        monkey_6.append(item2)

                    elif throw_monkey == 7:
                        monkey_7.append(item2)

                else:

                    throw_monkey = int(data_list[i + 13])
                    inspect_counter0 += 1
                    if throw_monkey == 0:
                        monkey_0.append(item2)

                    elif throw_monkey == 1:
                        monkey_1.append(item2)

                    elif throw_monkey == 2:
                        monkey_2.append(item2)

                    elif throw_monkey == 3:
                        monkey_3.append(item2)

                    elif throw_monkey == 4:
                        monkey_4.append(item2)

                    elif throw_monkey == 5:
                        monkey_5.append(item2)

                    elif throw_monkey == 6:
                        monkey_6.append(item2)

                    elif throw_monkey == 7:
                        monkey_7.append(item2)

    monkey_0.clear()
    result_list.clear()

    # For monkey 1
    for item in monkey_1:
        for i in range(data_list.index('1:'), data_list.index('2:')):
            if data_list[i] == '=':
                if data_list[i + 1] == 'old':
                    to_operate1 = int(item)
                else:
                    to_operate1 = int(data_list[i + 1])
                if data_list[i + 3] == 'old':
                    to_operate2 = int(item)
                else:
                    to_operate2 = int(data_list[i + 3])
                if data_list[i + 2] == '+':
                    result = to_operate1 + to_operate2
                    result_after_bored = result // 3
                    result_list.append(result_after_bored)
                elif data_list[i + 2] == '*':
                    result = to_operate1 * to_operate2
                    result_after_bored = result // 3
                    result_list.append(result_after_bored)

    for item2 in result_list:
        for i in range(data_list.index('1:'), data_list.index('2:')):
            if data_list[i] == 'by':
                division = int(data_list[i + 1])
                if item2 % division == 0:
                    throw_monkey = int(data_list[i + 7])
                    inspect_counter1 += 1
                    if throw_monkey == 0:
                        monkey_0.append(item2)

                    elif throw_monkey == 1:
                        monkey_1.append(item2)

                    elif throw_monkey == 2:
                        monkey_2.append(item2)

                    elif throw_monkey == 3:
                        monkey_3.append(item2)

                    elif throw_monkey == 4:
                        monkey_4.append(item2)

                    elif throw_monkey == 5:
                        monkey_5.append(item2)

                    elif throw_monkey == 6:
                        monkey_6.append(item2)

                    elif throw_monkey == 7:
                        monkey_7.append(item2)

                else:
                    throw_monkey = int(data_list[i + 13])
                    inspect_counter1 += 1
                    if throw_monkey == 0:
                        monkey_0.append(item2)

                    elif throw_monkey == 1:
                        monkey_1.append(item2)

                    elif throw_monkey == 2:
                        monkey_2.append(item2)

                    elif throw_monkey == 3:
                        monkey_3.append(item2)

                    elif throw_monkey == 4:
                        monkey_4.append(item2)

                    elif throw_monkey == 5:
                        monkey_5.append(item2)

                    elif throw_monkey == 6:
                        monkey_6.append(item2)

                    elif throw_monkey == 7:
                        monkey_7.append(item2)

    monkey_1.clear()
    result_list.clear()

    # For monkey 2
    for item in monkey_2:
        for i in range(data_list.index('2:'), data_list.index('3:')):
            if data_list[i] == '=':
                if data_list[i + 1] == 'old':
                    to_operate1 = int(item)
                else:
                    to_operate1 = int(data_list[i + 1])
                if data_list[i + 3] == 'old':
                    to_operate2 = int(item)
                else:
                    to_operate2 = int(data_list[i + 3])
                if data_list[i + 2] == '+':
                    result = to_operate1 + to_operate2
                    result_after_bored = result // 3
                    result_list.append(result_after_bored)
                elif data_list[i + 2] == '*':
                    result = to_operate1 * to_operate2
                    result_after_bored = result // 3
                    result_list.append(result_after_bored)

    for item2 in result_list:
        for i in range(data_list.index('2:'), data_list.index('3:')):
            if data_list[i] == 'by':
                division = int(data_list[i + 1])
                if item2 % division == 0:
                    throw_monkey = int(data_list[i + 7])
                    inspect_counter2 += 1
                    if throw_monkey == 0:
                        monkey_0.append(item2)

                    elif throw_monkey == 1:
                        monkey_1.append(item2)

                    elif throw_monkey == 2:
                        monkey_2.append(item2)

                    elif throw_monkey == 3:
                        monkey_3.append(item2)

                    elif throw_monkey == 4:
                        monkey_4.append(item2)

                    elif throw_monkey == 5:
                        monkey_5.append(item2)

                    elif throw_monkey == 6:
                        monkey_6.append(item2)

                    elif throw_monkey == 7:
                        monkey_7.append(item2)

                else:

                    throw_monkey = int(data_list[i + 13])
                    inspect_counter2 += 1
                    if throw_monkey == 0:
                        monkey_0.append(item2)

                    elif throw_monkey == 1:
                        monkey_1.append(item2)

                    elif throw_monkey == 2:
                        monkey_2.append(item2)

                    elif throw_monkey == 3:
                        monkey_3.append(item2)

                    elif throw_monkey == 4:
                        monkey_4.append(item2)

                    elif throw_monkey == 5:
                        monkey_5.append(item2)

                    elif throw_monkey == 6:
                        monkey_6.append(item2)

                    elif throw_monkey == 7:
                        monkey_7.append(item2)

    monkey_2.clear()
    result_list.clear()

    # For monkey 3
    for item in monkey_3:
        for i in range(data_list.index('3:'), data_list.index('4:')):
            if data_list[i] == '=':
                if data_list[i + 1] == 'old':
                    to_operate1 = int(item)
                else:
                    to_operate1 = int(data_list[i + 1])
                if data_list[i + 3] == 'old':
                    to_operate2 = int(item)
                else:
                    to_operate2 = int(data_list[i + 3])
                if data_list[i + 2] == '+':
                    result = to_operate1 + to_operate2
                    result_after_bored = result // 3
                    result_list.append(result_after_bored)
                elif data_list[i + 2] == '*':
                    result = to_operate1 * to_operate2
                    result_after_bored = result // 3
                    result_list.append(result_after_bored)

    for item2 in result_list:
        for i in range(data_list.index('3:'), data_list.index('4:')):
            if data_list[i] == 'by':
                division = int(data_list[i + 1])
                if item2 % division == 0:
                    throw_monkey = int(data_list[i + 7])
                    inspect_counter3 += 1
                    if throw_monkey == 0:
                        monkey_0.append(item2)

                    elif throw_monkey == 1:
                        monkey_1.append(item2)

                    elif throw_monkey == 2:
                        monkey_2.append(item2)

                    elif throw_monkey == 3:
                        monkey_3.append(item2)

                    elif throw_monkey == 4:
                        monkey_4.append(item2)

                    elif throw_monkey == 5:
                        monkey_5.append(item2)

                    elif throw_monkey == 6:
                        monkey_6.append(item2)

                    elif throw_monkey == 7:
                        monkey_7.append(item2)

                else:

                    throw_monkey = int(data_list[i + 13])
                    inspect_counter3 += 1
                    if throw_monkey == 0:
                        monkey_0.append(item2)

                    elif throw_monkey == 1:
                        monkey_1.append(item2)

                    elif throw_monkey == 2:
                        monkey_2.append(item2)

                    elif throw_monkey == 3:
                        monkey_3.append(item2)

                    elif throw_monkey == 4:
                        monkey_4.append(item2)

                    elif throw_monkey == 5:
                        monkey_5.append(item2)

                    elif throw_monkey == 6:
                        monkey_6.append(item2)

                    elif throw_monkey == 7:
                        monkey_7.append(item2)

    monkey_3.clear()
    result_list.clear()

    # For monkey 4
    for item in monkey_4:
        for i in range(data_list.index('4:'), data_list.index('5:')):
            if data_list[i] == '=':
                if data_list[i + 1] == 'old':
                    to_operate1 = int(item)
                else:
                    to_operate1 = int(data_list[i + 1])
                if data_list[i + 3] == 'old':
                    to_operate2 = int(item)
                else:
                    to_operate2 = int(data_list[i + 3])
                if data_list[i + 2] == '+':
                    result = to_operate1 + to_operate2
                    result_after_bored = result // 3
                    result_list.append(result_after_bored)
                elif data_list[i + 2] == '*':
                    result = to_operate1 * to_operate2
                    result_after_bored = result // 3
                    result_list.append(result_after_bored)

    for item2 in result_list:
        for i in range(data_list.index('4:'), data_list.index('5:')):
            if data_list[i] == 'by':
                division = int(data_list[i + 1])
                if item2 % division == 0:
                    throw_monkey = int(data_list[i + 7])
                    inspect_counter4 += 1
                    if throw_monkey == 0:
                        monkey_0.append(item2)

                    elif throw_monkey == 1:
                        monkey_1.append(item2)

                    elif throw_monkey == 2:
                        monkey_2.append(item2)

                    elif throw_monkey == 3:
                        monkey_3.append(item2)

                    elif throw_monkey == 4:
                        monkey_4.append(item2)

                    elif throw_monkey == 5:
                        monkey_5.append(item2)

                    elif throw_monkey == 6:
                        monkey_6.append(item2)

                    elif throw_monkey == 7:
                        monkey_7.append(item2)

                else:

                    throw_monkey = int(data_list[i + 13])
                    inspect_counter4 += 1
                    if throw_monkey == 0:
                        monkey_0.append(item2)

                    elif throw_monkey == 1:
                        monkey_1.append(item2)

                    elif throw_monkey == 2:
                        monkey_2.append(item2)

                    elif throw_monkey == 3:
                        monkey_3.append(item2)

                    elif throw_monkey == 4:
                        monkey_4.append(item2)

                    elif throw_monkey == 5:
                        monkey_5.append(item2)

                    elif throw_monkey == 6:
                        monkey_6.append(item2)

                    elif throw_monkey == 7:
                        monkey_7.append(item2)

    monkey_4.clear()
    result_list.clear()

    # For monkey 5
    for item in monkey_5:
        for i in range(data_list.index('5:'), data_list.index('6:')):
            if data_list[i] == '=':
                if data_list[i + 1] == 'old':
                    to_operate1 = int(item)
                else:
                    to_operate1 = int(data_list[i + 1])
                if data_list[i + 3] == 'old':
                    to_operate2 = int(item)
                else:
                    to_operate2 = int(data_list[i + 3])
                if data_list[i + 2] == '+':
                    result = to_operate1 + to_operate2
                    result_after_bored = result // 3
                    result_list.append(result_after_bored)
                elif data_list[i + 2] == '*':
                    result = to_operate1 * to_operate2
                    result_after_bored = result // 3
                    result_list.append(result_after_bored)

    for item2 in result_list:
        for i in range(data_list.index('5:'), data_list.index('6:')):
            if data_list[i] == 'by':
                division = int(data_list[i + 1])
                if item2 % division == 0:
                    throw_monkey = int(data_list[i + 7])
                    inspect_counter5 += 1
                    if throw_monkey == 0:
                        monkey_0.append(item2)

                    elif throw_monkey == 1:
                        monkey_1.append(item2)

                    elif throw_monkey == 2:
                        monkey_2.append(item2)

                    elif throw_monkey == 3:
                        monkey_3.append(item2)

                    elif throw_monkey == 4:
                        monkey_4.append(item2)

                    elif throw_monkey == 5:
                        monkey_5.append(item2)

                    elif throw_monkey == 6:
                        monkey_6.append(item2)

                    elif throw_monkey == 7:
                        monkey_7.append(item2)

                else:

                    throw_monkey = int(data_list[i + 13])
                    inspect_counter5 += 1
                    if throw_monkey == 0:
                        monkey_0.append(item2)

                    elif throw_monkey == 1:
                        monkey_1.append(item2)

                    elif throw_monkey == 2:
                        monkey_2.append(item2)

                    elif throw_monkey == 3:
                        monkey_3.append(item2)

                    elif throw_monkey == 4:
                        monkey_4.append(item2)

                    elif throw_monkey == 5:
                        monkey_5.append(item2)

                    elif throw_monkey == 6:
                        monkey_6.append(item2)

                    elif throw_monkey == 7:
                        monkey_7.append(item2)

    monkey_5.clear()
    result_list.clear()

    # For monkey 6
    for item in monkey_6:
        for i in range(data_list.index('6:'), data_list.index('7:')):
            if data_list[i] == '=':
                if data_list[i + 1] == 'old':
                    to_operate1 = int(item)
                else:
                    to_operate1 = int(data_list[i + 1])
                if data_list[i + 3] == 'old':
                    to_operate2 = int(item)
                else:
                    to_operate2 = int(data_list[i + 3])
                if data_list[i + 2] == '+':
                    result = to_operate1 + to_operate2
                    result_after_bored = result // 3
                    result_list.append(result_after_bored)
                elif data_list[i + 2] == '*':
                    result = to_operate1 * to_operate2
                    result_after_bored = result // 3
                    result_list.append(result_after_bored)

    for item2 in result_list:
        for i in range(data_list.index('6:'), data_list.index('7:')):
            if data_list[i] == 'by':
                division = int(data_list[i + 1])
                if item2 % division == 0:
                    throw_monkey = int(data_list[i + 7])
                    inspect_counter6 += 1
                    if throw_monkey == 0:
                        monkey_0.append(item2)

                    elif throw_monkey == 1:
                        monkey_1.append(item2)

                    elif throw_monkey == 2:
                        monkey_2.append(item2)

                    elif throw_monkey == 3:
                        monkey_3.append(item2)

                    elif throw_monkey == 4:
                        monkey_4.append(item2)

                    elif throw_monkey == 5:
                        monkey_5.append(item2)

                    elif throw_monkey == 6:
                        monkey_6.append(item2)

                    elif throw_monkey == 7:
                        monkey_7.append(item2)

                else:

                    throw_monkey = int(data_list[i + 13])
                    inspect_counter6 += 1
                    if throw_monkey == 0:
                        monkey_0.append(item2)

                    elif throw_monkey == 1:
                        monkey_1.append(item2)

                    elif throw_monkey == 2:
                        monkey_2.append(item2)

                    elif throw_monkey == 3:
                        monkey_3.append(item2)

                    elif throw_monkey == 4:
                        monkey_4.append(item2)

                    elif throw_monkey == 5:
                        monkey_5.append(item2)

                    elif throw_monkey == 6:
                        monkey_6.append(item2)

                    elif throw_monkey == 7:
                        monkey_7.append(item2)

    monkey_6.clear()
    result_list.clear()

    # For monkey 7
    for item in monkey_7:
        for i in range(data_list.index('7:'), len(data_list)):
            if data_list[i] == '=':
                if data_list[i + 1] == 'old':
                    to_operate1 = int(item)
                else:
                    to_operate1 = int(data_list[i + 1])
                if data_list[i + 3] == 'old':
                    to_operate2 = int(item)
                else:
                    to_operate2 = int(data_list[i + 3])
                if data_list[i + 2] == '+':
                    result = to_operate1 + to_operate2
                    result_after_bored = result // 3
                    result_list.append(result_after_bored)
                elif data_list[i + 2] == '*':
                    result = to_operate1 * to_operate2
                    result_after_bored = result // 3
                    result_list.append(result_after_bored)

    for item2 in result_list:
        for i in range(data_list.index('7:'), len(data_list)):
            if data_list[i] == 'by':
                division = int(data_list[i + 1])
                if item2 % division == 0:
                    throw_monkey = int(data_list[i + 7])
                    inspect_counter7 += 1
                    if throw_monkey == 0:
                        monkey_0.append(item2)

                    elif throw_monkey == 1:
                        monkey_1.append(item2)

                    elif throw_monkey == 2:
                        monkey_2.append(item2)

                    elif throw_monkey == 3:
                        monkey_3.append(item2)

                    elif throw_monkey == 4:
                        monkey_4.append(item2)

                    elif throw_monkey == 5:
                        monkey_5.append(item2)

                    elif throw_monkey == 6:
                        monkey_6.append(item2)

                    elif throw_monkey == 7:
                        monkey_7.append(item2)

                else:

                    throw_monkey = int(data_list[i + 13])
                    inspect_counter7 += 1
                    if throw_monkey == 0:
                        monkey_0.append(item2)

                    elif throw_monkey == 1:
                        monkey_1.append(item2)

                    elif throw_monkey == 2:
                        monkey_2.append(item2)

                    elif throw_monkey == 3:
                        monkey_3.append(item2)

                    elif throw_monkey == 4:
                        monkey_4.append(item2)

                    elif throw_monkey == 5:
                        monkey_5.append(item2)

                    elif throw_monkey == 6:
                        monkey_6.append(item2)

                    elif throw_monkey == 7:
                        monkey_7.append(item2)

    monkey_7.clear()
    result_list.clear()




list_res=[inspect_counter0, inspect_counter1, inspect_counter2, inspect_counter3, inspect_counter4, inspect_counter5,
      inspect_counter6, inspect_counter7]
res1=max(list_res)
list_res.pop(list_res.index(res1))
res2=max(list_res)
print("result", res1*res2)

# part 2

import re

with open('input_day11.txt', 'r') as myfile:
    lines = myfile.read().strip().split()
data_list = []

for line in lines:
    new_line = (re.sub(",", "", line))
    data_list.append(new_line)
result_list = []
monkey_0 = []
monkey_1 = []
monkey_2 = []
monkey_3 = []
monkey_4 = []
monkey_5 = []
monkey_6 = []
monkey_7 = []

for i in range(0, data_list.index('1:')):
    if data_list[i].isdigit():
        monkey_0.append(data_list[i])
    elif data_list[i] == 'Operation:':
        break
for i in range(data_list.index('1:'), data_list.index('2:')):
    if data_list[i].isdigit():
        monkey_1.append(data_list[i])
    elif data_list[i] == 'Operation:':
        break
for i in range(data_list.index('2:'), data_list.index('3:')):
    if data_list[i].isdigit():
        monkey_2.append(data_list[i])
    elif data_list[i] == 'Operation:':
        break
for i in range(data_list.index('3:'), data_list.index('4:')):
    if data_list[i].isdigit():
        monkey_3.append(data_list[i])
    elif data_list[i] == 'Operation:':
        break
for i in range(data_list.index('4:'), data_list.index('5:')):
    if data_list[i].isdigit():
        monkey_4.append(data_list[i])
    elif data_list[i] == 'Operation:':
        break
for i in range(data_list.index('5:'), data_list.index('6:')):
    if data_list[i].isdigit():
        monkey_5.append(data_list[i])
    elif data_list[i] == 'Operation:':
        break
for i in range(data_list.index('6:'), data_list.index('7:')):
    if data_list[i].isdigit():
        monkey_6.append(data_list[i])
    elif data_list[i] == 'Operation:':
        break
for i in range(data_list.index('7:'), len(data_list)):
    if data_list[i].isdigit():
        monkey_7.append(data_list[i])
    elif data_list[i] == 'Operation:':
        break

inspect_counter0 = 0
inspect_counter1 = 0
inspect_counter2 = 0
inspect_counter3 = 0
inspect_counter4 = 0
inspect_counter5 = 0
inspect_counter6 = 0
inspect_counter7 = 0

for round in range(0, 10000):
    # For monkey 0
    for item in monkey_0:
        for i in range(0, data_list.index('1:')):
            if data_list[i] == '=':
                if data_list[i + 1] == 'old':
                    to_operate1 = int(item)
                else:
                    to_operate1 = int(data_list[i + 1])
                if data_list[i + 3] == 'old':
                    to_operate2 = int(item)
                else:
                    to_operate2 = int(data_list[i + 3])
                if data_list[i + 2] == '+':
                    result = to_operate1 + to_operate2
                    result_after_bored = result % 9699690
                    result_list.append(result_after_bored)
                elif data_list[i + 2] == '*':
                    result = to_operate1 * to_operate2
                    result_after_bored = result % 9699690
                    result_list.append(result_after_bored)

    for item2 in result_list:
        for i in range(0, data_list.index('1:')):
            if data_list[i] == 'by':
                division = int(data_list[i + 1])
                if item2 % division == 0:
                    throw_monkey = int(data_list[i + 7])
                    inspect_counter0 += 1
                    if throw_monkey == 0:
                        monkey_0.append(item2)

                    elif throw_monkey == 1:
                        monkey_1.append(item2)

                    elif throw_monkey == 2:
                        monkey_2.append(item2)

                    elif throw_monkey == 3:
                        monkey_3.append(item2)

                    elif throw_monkey == 4:
                        monkey_4.append(item2)

                    elif throw_monkey == 5:
                        monkey_5.append(item2)

                    elif throw_monkey == 6:
                        monkey_6.append(item2)

                    elif throw_monkey == 7:
                        monkey_7.append(item2)

                else:

                    throw_monkey = int(data_list[i + 13])
                    inspect_counter0 += 1
                    if throw_monkey == 0:
                        monkey_0.append(item2)

                    elif throw_monkey == 1:
                        monkey_1.append(item2)

                    elif throw_monkey == 2:
                        monkey_2.append(item2)

                    elif throw_monkey == 3:
                        monkey_3.append(item2)

                    elif throw_monkey == 4:
                        monkey_4.append(item2)

                    elif throw_monkey == 5:
                        monkey_5.append(item2)

                    elif throw_monkey == 6:
                        monkey_6.append(item2)

                    elif throw_monkey == 7:
                        monkey_7.append(item2)

    monkey_0.clear()
    result_list.clear()

    # For monkey 1
    for item in monkey_1:
        for i in range(data_list.index('1:'), data_list.index('2:')):
            if data_list[i] == '=':
                if data_list[i + 1] == 'old':
                    to_operate1 = int(item)
                else:
                    to_operate1 = int(data_list[i + 1])
                if data_list[i + 3] == 'old':
                    to_operate2 = int(item)
                else:
                    to_operate2 = int(data_list[i + 3])
                if data_list[i + 2] == '+':
                    result = to_operate1 + to_operate2
                    result_after_bored = result % 9699690
                    result_list.append(result_after_bored)
                elif data_list[i + 2] == '*':
                    result = to_operate1 * to_operate2
                    result_after_bored = result % 9699690
                    result_list.append(result_after_bored)

    for item2 in result_list:
        for i in range(data_list.index('1:'), data_list.index('2:')):
            if data_list[i] == 'by':
                division = int(data_list[i + 1])
                if item2 % division == 0:
                    throw_monkey = int(data_list[i + 7])
                    inspect_counter1 += 1
                    if throw_monkey == 0:
                        monkey_0.append(item2)

                    elif throw_monkey == 1:
                        monkey_1.append(item2)

                    elif throw_monkey == 2:
                        monkey_2.append(item2)

                    elif throw_monkey == 3:
                        monkey_3.append(item2)

                    elif throw_monkey == 4:
                        monkey_4.append(item2)

                    elif throw_monkey == 5:
                        monkey_5.append(item2)

                    elif throw_monkey == 6:
                        monkey_6.append(item2)

                    elif throw_monkey == 7:
                        monkey_7.append(item2)

                else:
                    throw_monkey = int(data_list[i + 13])
                    inspect_counter1 += 1
                    if throw_monkey == 0:
                        monkey_0.append(item2)

                    elif throw_monkey == 1:
                        monkey_1.append(item2)

                    elif throw_monkey == 2:
                        monkey_2.append(item2)

                    elif throw_monkey == 3:
                        monkey_3.append(item2)

                    elif throw_monkey == 4:
                        monkey_4.append(item2)

                    elif throw_monkey == 5:
                        monkey_5.append(item2)

                    elif throw_monkey == 6:
                        monkey_6.append(item2)

                    elif throw_monkey == 7:
                        monkey_7.append(item2)

    monkey_1.clear()
    result_list.clear()

    # For monkey 2
    for item in monkey_2:
        for i in range(data_list.index('2:'), data_list.index('3:')):
            if data_list[i] == '=':
                if data_list[i + 1] == 'old':
                    to_operate1 = int(item)
                else:
                    to_operate1 = int(data_list[i + 1])
                if data_list[i + 3] == 'old':
                    to_operate2 = int(item)
                else:
                    to_operate2 = int(data_list[i + 3])
                if data_list[i + 2] == '+':
                    result = to_operate1 + to_operate2
                    result_after_bored = result % 9699690
                    result_list.append(result_after_bored)
                elif data_list[i + 2] == '*':
                    result = to_operate1 * to_operate2
                    result_after_bored = result % 9699690
                    result_list.append(result_after_bored)

    for item2 in result_list:
        for i in range(data_list.index('2:'), data_list.index('3:')):
            if data_list[i] == 'by':
                division = int(data_list[i + 1])
                if item2 % division == 0:
                    throw_monkey = int(data_list[i + 7])
                    inspect_counter2 += 1
                    if throw_monkey == 0:
                        monkey_0.append(item2)

                    elif throw_monkey == 1:
                        monkey_1.append(item2)

                    elif throw_monkey == 2:
                        monkey_2.append(item2)

                    elif throw_monkey == 3:
                        monkey_3.append(item2)

                    elif throw_monkey == 4:
                        monkey_4.append(item2)

                    elif throw_monkey == 5:
                        monkey_5.append(item2)

                    elif throw_monkey == 6:
                        monkey_6.append(item2)

                    elif throw_monkey == 7:
                        monkey_7.append(item2)

                else:

                    throw_monkey = int(data_list[i + 13])
                    inspect_counter2 += 1
                    if throw_monkey == 0:
                        monkey_0.append(item2)

                    elif throw_monkey == 1:
                        monkey_1.append(item2)

                    elif throw_monkey == 2:
                        monkey_2.append(item2)

                    elif throw_monkey == 3:
                        monkey_3.append(item2)

                    elif throw_monkey == 4:
                        monkey_4.append(item2)

                    elif throw_monkey == 5:
                        monkey_5.append(item2)

                    elif throw_monkey == 6:
                        monkey_6.append(item2)

                    elif throw_monkey == 7:
                        monkey_7.append(item2)

    monkey_2.clear()
    result_list.clear()

    # For monkey 3
    for item in monkey_3:
        for i in range(data_list.index('3:'), data_list.index('4:')):
            if data_list[i] == '=':
                if data_list[i + 1] == 'old':
                    to_operate1 = int(item)
                else:
                    to_operate1 = int(data_list[i + 1])
                if data_list[i + 3] == 'old':
                    to_operate2 = int(item)
                else:
                    to_operate2 = int(data_list[i + 3])
                if data_list[i + 2] == '+':
                    result = to_operate1 + to_operate2
                    result_after_bored = result % 9699690
                    result_list.append(result_after_bored)
                elif data_list[i + 2] == '*':
                    result = to_operate1 * to_operate2
                    result_after_bored = result % 9699690
                    result_list.append(result_after_bored)

    for item2 in result_list:
        for i in range(data_list.index('3:'), data_list.index('4:')):
            if data_list[i] == 'by':
                division = int(data_list[i + 1])
                if item2 % division == 0:
                    throw_monkey = int(data_list[i + 7])
                    inspect_counter3 += 1
                    if throw_monkey == 0:
                        monkey_0.append(item2)

                    elif throw_monkey == 1:
                        monkey_1.append(item2)

                    elif throw_monkey == 2:
                        monkey_2.append(item2)

                    elif throw_monkey == 3:
                        monkey_3.append(item2)

                    elif throw_monkey == 4:
                        monkey_4.append(item2)

                    elif throw_monkey == 5:
                        monkey_5.append(item2)

                    elif throw_monkey == 6:
                        monkey_6.append(item2)

                    elif throw_monkey == 7:
                        monkey_7.append(item2)

                else:

                    throw_monkey = int(data_list[i + 13])
                    inspect_counter3 += 1
                    if throw_monkey == 0:
                        monkey_0.append(item2)

                    elif throw_monkey == 1:
                        monkey_1.append(item2)

                    elif throw_monkey == 2:
                        monkey_2.append(item2)

                    elif throw_monkey == 3:
                        monkey_3.append(item2)

                    elif throw_monkey == 4:
                        monkey_4.append(item2)

                    elif throw_monkey == 5:
                        monkey_5.append(item2)

                    elif throw_monkey == 6:
                        monkey_6.append(item2)

                    elif throw_monkey == 7:
                        monkey_7.append(item2)

    monkey_3.clear()
    result_list.clear()

    # For monkey 4
    for item in monkey_4:
        for i in range(data_list.index('4:'), data_list.index('5:')):
            if data_list[i] == '=':
                if data_list[i + 1] == 'old':
                    to_operate1 = int(item)
                else:
                    to_operate1 = int(data_list[i + 1])
                if data_list[i + 3] == 'old':
                    to_operate2 = int(item)
                else:
                    to_operate2 = int(data_list[i + 3])
                if data_list[i + 2] == '+':
                    result = to_operate1 + to_operate2
                    result_after_bored = result % 9699690
                    result_list.append(result_after_bored)
                elif data_list[i + 2] == '*':
                    result = to_operate1 * to_operate2
                    result_after_bored = result % 9699690
                    result_list.append(result_after_bored)

    for item2 in result_list:
        for i in range(data_list.index('4:'), data_list.index('5:')):
            if data_list[i] == 'by':
                division = int(data_list[i + 1])
                if item2 % division == 0:
                    throw_monkey = int(data_list[i + 7])
                    inspect_counter4 += 1
                    if throw_monkey == 0:
                        monkey_0.append(item2)

                    elif throw_monkey == 1:
                        monkey_1.append(item2)

                    elif throw_monkey == 2:
                        monkey_2.append(item2)

                    elif throw_monkey == 3:
                        monkey_3.append(item2)

                    elif throw_monkey == 4:
                        monkey_4.append(item2)

                    elif throw_monkey == 5:
                        monkey_5.append(item2)

                    elif throw_monkey == 6:
                        monkey_6.append(item2)

                    elif throw_monkey == 7:
                        monkey_7.append(item2)

                else:

                    throw_monkey = int(data_list[i + 13])
                    inspect_counter4 += 1
                    if throw_monkey == 0:
                        monkey_0.append(item2)

                    elif throw_monkey == 1:
                        monkey_1.append(item2)

                    elif throw_monkey == 2:
                        monkey_2.append(item2)

                    elif throw_monkey == 3:
                        monkey_3.append(item2)

                    elif throw_monkey == 4:
                        monkey_4.append(item2)

                    elif throw_monkey == 5:
                        monkey_5.append(item2)

                    elif throw_monkey == 6:
                        monkey_6.append(item2)

                    elif throw_monkey == 7:
                        monkey_7.append(item2)

    monkey_4.clear()
    result_list.clear()

    # For monkey 5
    for item in monkey_5:
        for i in range(data_list.index('5:'), data_list.index('6:')):
            if data_list[i] == '=':
                if data_list[i + 1] == 'old':
                    to_operate1 = int(item)
                else:
                    to_operate1 = int(data_list[i + 1])
                if data_list[i + 3] == 'old':
                    to_operate2 = int(item)
                else:
                    to_operate2 = int(data_list[i + 3])
                if data_list[i + 2] == '+':
                    result = to_operate1 + to_operate2
                    result_after_bored = result % 9699690
                    result_list.append(result_after_bored)
                elif data_list[i + 2] == '*':
                    result = to_operate1 * to_operate2
                    result_after_bored = result % 9699690
                    result_list.append(result_after_bored)

    for item2 in result_list:
        for i in range(data_list.index('5:'), data_list.index('6:')):
            if data_list[i] == 'by':
                division = int(data_list[i + 1])
                if item2 % division == 0:
                    throw_monkey = int(data_list[i + 7])
                    inspect_counter5 += 1
                    if throw_monkey == 0:
                        monkey_0.append(item2)

                    elif throw_monkey == 1:
                        monkey_1.append(item2)

                    elif throw_monkey == 2:
                        monkey_2.append(item2)

                    elif throw_monkey == 3:
                        monkey_3.append(item2)

                    elif throw_monkey == 4:
                        monkey_4.append(item2)

                    elif throw_monkey == 5:
                        monkey_5.append(item2)

                    elif throw_monkey == 6:
                        monkey_6.append(item2)

                    elif throw_monkey == 7:
                        monkey_7.append(item2)

                else:

                    throw_monkey = int(data_list[i + 13])
                    inspect_counter5 += 1
                    if throw_monkey == 0:
                        monkey_0.append(item2)

                    elif throw_monkey == 1:
                        monkey_1.append(item2)

                    elif throw_monkey == 2:
                        monkey_2.append(item2)

                    elif throw_monkey == 3:
                        monkey_3.append(item2)

                    elif throw_monkey == 4:
                        monkey_4.append(item2)

                    elif throw_monkey == 5:
                        monkey_5.append(item2)

                    elif throw_monkey == 6:
                        monkey_6.append(item2)

                    elif throw_monkey == 7:
                        monkey_7.append(item2)

    monkey_5.clear()
    result_list.clear()

    # For monkey 6
    for item in monkey_6:
        for i in range(data_list.index('6:'), data_list.index('7:')):
            if data_list[i] == '=':
                if data_list[i + 1] == 'old':
                    to_operate1 = int(item)
                else:
                    to_operate1 = int(data_list[i + 1])
                if data_list[i + 3] == 'old':
                    to_operate2 = int(item)
                else:
                    to_operate2 = int(data_list[i + 3])
                if data_list[i + 2] == '+':
                    result = to_operate1 + to_operate2
                    result_after_bored = result % 9699690
                    result_list.append(result_after_bored)
                elif data_list[i + 2] == '*':
                    result = to_operate1 * to_operate2
                    result_after_bored = result % 9699690
                    result_list.append(result_after_bored)

    for item2 in result_list:
        for i in range(data_list.index('6:'), data_list.index('7:')):
            if data_list[i] == 'by':
                division = int(data_list[i + 1])
                if item2 % division == 0:
                    throw_monkey = int(data_list[i + 7])
                    inspect_counter6 += 1
                    if throw_monkey == 0:
                        monkey_0.append(item2)

                    elif throw_monkey == 1:
                        monkey_1.append(item2)

                    elif throw_monkey == 2:
                        monkey_2.append(item2)

                    elif throw_monkey == 3:
                        monkey_3.append(item2)

                    elif throw_monkey == 4:
                        monkey_4.append(item2)

                    elif throw_monkey == 5:
                        monkey_5.append(item2)

                    elif throw_monkey == 6:
                        monkey_6.append(item2)

                    elif throw_monkey == 7:
                        monkey_7.append(item2)

                else:

                    throw_monkey = int(data_list[i + 13])
                    inspect_counter6 += 1
                    if throw_monkey == 0:
                        monkey_0.append(item2)

                    elif throw_monkey == 1:
                        monkey_1.append(item2)

                    elif throw_monkey == 2:
                        monkey_2.append(item2)

                    elif throw_monkey == 3:
                        monkey_3.append(item2)

                    elif throw_monkey == 4:
                        monkey_4.append(item2)

                    elif throw_monkey == 5:
                        monkey_5.append(item2)

                    elif throw_monkey == 6:
                        monkey_6.append(item2)

                    elif throw_monkey == 7:
                        monkey_7.append(item2)

    monkey_6.clear()
    result_list.clear()

    # For monkey 7
    for item in monkey_7:
        for i in range(data_list.index('7:'), len(data_list)):
            if data_list[i] == '=':
                if data_list[i + 1] == 'old':
                    to_operate1 = int(item)
                else:
                    to_operate1 = int(data_list[i + 1])
                if data_list[i + 3] == 'old':
                    to_operate2 = int(item)
                else:
                    to_operate2 = int(data_list[i + 3])
                if data_list[i + 2] == '+':
                    result = to_operate1 + to_operate2
                    result_after_bored = result % 9699690
                    result_list.append(result_after_bored)
                elif data_list[i + 2] == '*':
                    result = to_operate1 * to_operate2
                    result_after_bored = result % 9699690
                    result_list.append(result_after_bored)

    for item2 in result_list:
        for i in range(data_list.index('7:'), len(data_list)):
            if data_list[i] == 'by':
                division = int(data_list[i + 1])
                if item2 % division == 0:
                    throw_monkey = int(data_list[i + 7])
                    inspect_counter7 += 1
                    if throw_monkey == 0:
                        monkey_0.append(item2)

                    elif throw_monkey == 1:
                        monkey_1.append(item2)

                    elif throw_monkey == 2:
                        monkey_2.append(item2)

                    elif throw_monkey == 3:
                        monkey_3.append(item2)

                    elif throw_monkey == 4:
                        monkey_4.append(item2)

                    elif throw_monkey == 5:
                        monkey_5.append(item2)

                    elif throw_monkey == 6:
                        monkey_6.append(item2)

                    elif throw_monkey == 7:
                        monkey_7.append(item2)

                else:

                    throw_monkey = int(data_list[i + 13])
                    inspect_counter7 += 1
                    if throw_monkey == 0:
                        monkey_0.append(item2)

                    elif throw_monkey == 1:
                        monkey_1.append(item2)

                    elif throw_monkey == 2:
                        monkey_2.append(item2)

                    elif throw_monkey == 3:
                        monkey_3.append(item2)

                    elif throw_monkey == 4:
                        monkey_4.append(item2)

                    elif throw_monkey == 5:
                        monkey_5.append(item2)

                    elif throw_monkey == 6:
                        monkey_6.append(item2)

                    elif throw_monkey == 7:
                        monkey_7.append(item2)

    monkey_7.clear()
    result_list.clear()




list_res=[inspect_counter0, inspect_counter1, inspect_counter2, inspect_counter3, inspect_counter4, inspect_counter5,
      inspect_counter6, inspect_counter7]
res1=max(list_res)
list_res.pop(list_res.index(res1))
res2=max(list_res)
print("result", res1*res2)
