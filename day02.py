with open('input_day2.txt', 'r') as myfile:
    lines = myfile.read().strip().split()

line_list=[]
score=0

for line in lines:
    line_list.append(line)


for i in range(0, len(line_list)):
    if line_list[i] == 'A':
        if line_list[i+1] == 'X':
            score += 4
        elif line_list[i+1] == 'Y':
            score += 8
        elif line_list[i+1] == 'Z':
            score += 3
    elif line_list[i] == 'B':
        if line_list[i+1] == 'X':
            score += 1
        elif line_list[i+1] == 'Y':
            score += 5
        elif line_list[i+1] == 'Z':
            score += 9
    elif line_list[i] == 'C':
        if line_list[i+1] == 'X':
            score += 7
        elif line_list[i+1] == 'Y':
            score += 2
        elif line_list[i+1] == 'Z':
            score += 6

print(score)
# Part two
score2=0

for i in range(0, len(line_list)):
    if line_list[i] == 'A':
        if line_list[i+1] == 'X':
            score2 += 3
        elif line_list[i+1] == 'Y':
            score2 += 4
        elif line_list[i+1] == 'Z':
            score2 += 8
    if line_list[i] == 'B':
        if line_list[i+1] == 'X':
            score2 += 1
        elif line_list[i+1] == 'Y':
            score2 += 5
        elif line_list[i+1] == 'Z':
            score2 += 9
    if line_list[i] == 'C':
        if line_list[i+1] == 'X':
            score2 += 2
        elif line_list[i+1] == 'Y':
            score2 += 6
        elif line_list[i+1] == 'Z':
            score2 += 7
print(score2)