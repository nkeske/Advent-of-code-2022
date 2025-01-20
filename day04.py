with open('input_day4.txt', 'r') as myfile:
    lines = myfile.read().strip().split()

numbers_list=[]
first_elf= []
second_elf = []
subset_counter = 0
overlap_counter= 0
overlapping_in_list =[]
for line in lines:
    no_hypen_line = line.replace('-', ' ')
    no_comma_line = no_hypen_line.replace(',', ' ')
    for num_str in no_comma_line.split():
        num_int = int(num_str)
        numbers_list.append(num_int)


    for m in range (numbers_list[0],(numbers_list[1]+1) ):
        first_elf.append(m)
    for n in range (numbers_list[2],numbers_list[3]+1):
        second_elf.append(n)


    if set(first_elf).issubset(set(second_elf)):
        subset_counter+=1
    elif set(second_elf).issubset(set(first_elf)):
        subset_counter += 1

    for a in range (0, len(first_elf)):
        for b in range (0, len(second_elf)):
            if first_elf[a]==second_elf[b]:
                overlapping_in_list.append(first_elf[a])

    if len(overlapping_in_list)!=0:
        overlap_counter+=1

    overlapping_in_list.clear()
    first_elf.clear()
    second_elf.clear()
    numbers_list.clear()

print(subset_counter)

#part two
print(overlap_counter)
