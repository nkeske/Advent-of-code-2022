
total_calories_array = []
calorie_counter = 0


with open('input_day1_1.txt', 'r') as myfile:
    lines = myfile.readlines()


for line in lines:
    if line.strip():
        calorie_counter+=int(line)
    else:
        total_calories_array.append(calorie_counter)
        calorie_counter=0


max_calori=max(total_calories_array)

print("Total calorie that elf carrying is (The answer for part one):", max_calori)

# Part two

max_three_array = []
max_three_array.append(max_calori)

for i in range(0, len(total_calories_array)):
    if total_calories_array[i]==max_calori:
        total_calories_array[i]=0

max_calori2 = max(total_calories_array)
max_three_array.append(max_calori2)

for i in range(0, len(total_calories_array)):
    if total_calories_array[i] == max_calori2:
        total_calories_array[i] = 0

max_calori3 = max(total_calories_array)
max_three_array.append(max_calori3)


print("The sum of three max calories (Answer for part two) is:", sum(max_three_array))


