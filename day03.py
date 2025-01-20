with open('input_day3.txt', 'r') as myfile:
    lines = myfile.read().strip().split()
ruckscak_1=[]
ruckscak_2=[]
to_prioritize=[]
to_prioritize_line=[]
prioritize_dict={'a':1,'b':2, 'c':3, 'd': 4, 'e':5, 'f':6, 'g': 7, 'h': 8, 'i':9, 'j':10, 'k':11, 'l':12, 'm': 13,
                 'n': 14, 'o': 15, 'p':16, 'q': 17, 'r': 18, 's':19, 't': 20, 'u':21, 'v':22, 'w':23, 'x':24, 'y':25,
                 'z': 26, 'A':27,'B':28, 'C':29, 'D': 30, 'E':31, 'F':32, 'G': 33, 'H': 34, 'I':35, 'J':36, 'K':37,
                 'L':38, 'M': 39, 'N':40, 'O': 41, 'P':42, 'Q': 43, 'R': 44, 'S':45, 'T': 46, 'U':47, 'V':48, 'W':49,
                 'X':50, 'Y':51,'Z': 52}

prioritizing_score_list=[]

for line in lines:
    line_lenght=len(line)
    for i in range(0, line_lenght):
        if i<line_lenght//2:
            ruckscak_1.append(line[i])
        else:
            ruckscak_2.append(line[i])
    for k in range(0,len(ruckscak_1)):
        for j in range(0, len(ruckscak_2)):
            if ruckscak_1[k]==ruckscak_2[j]:
                to_prioritize_line.append(ruckscak_2[j])
    new_list=set(to_prioritize_line)
    prioritize = next(iter(new_list))
    value_score = prioritize_dict[prioritize]
    prioritizing_score_list.append(value_score)


    to_prioritize_line.clear()
    ruckscak_1.clear()
    ruckscak_2.clear()


print(sum(prioritizing_score_list))

#Part two
group_list=[]
to_prioritize_line_2=[]
prioritizing_score_list_2=[]
for i in range(0,len(lines),3):
    group_list.append(lines[i])
    group_list.append(lines[i+1])
    group_list.append(lines[i+2])

    for k in range(0,len(group_list[0])):
        for j in range(0, len(group_list[1])):
            for l in range(0, len(group_list[2])):
                if group_list[0][k]==group_list[1][j] and group_list[1][j] ==group_list[2][l] :
                    to_prioritize_line_2.append(group_list[0][k])

    new_list_2 = set(to_prioritize_line_2)
    prioritize_2 = next(iter(new_list_2))

    value_score_2 = prioritize_dict[prioritize_2]
    prioritizing_score_list_2.append(value_score_2)
    group_list.clear()
    to_prioritize_line_2.clear()


print(sum(prioritizing_score_list_2))



