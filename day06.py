with open('input_day6.2.txt', 'r') as myfile:
    lines = myfile.read().strip()



four_chr_list=[]
line_list=[]

for line in lines:
    line_list.append(line)
for i in range(0, len(line_list)-3):
    second_elem=line_list[i+1]
    third_elem = line_list[i+2]
    fourth_elem = line_list[i+3]
    four_chr_list.append(line_list[i])
    four_chr_list.append(second_elem)
    four_chr_list.append(third_elem)
    four_chr_list.append(fourth_elem)

    if four_chr_list[0]!=four_chr_list[1] and four_chr_list[0]!=four_chr_list[2] and four_chr_list[0]!=four_chr_list[3]:
        if  four_chr_list[1]!=four_chr_list[2] and four_chr_list[1]!=four_chr_list[3] and four_chr_list[2]!=four_chr_list[3]:

            print(i+4)
            break

    four_chr_list.clear()


#part two

fourteen_chr_list=[]

for line in lines:
    line_list.append(line)
for i in range(0, len(line_list)-13):
    second_elem=line_list[i+1]
    third_elem = line_list[i+2]
    fourth_elem = line_list[i+3]
    fifth_elem = line_list[i + 4]
    sixth_elem = line_list[i + 5]
    seventh_elem = line_list[i + 6]
    eight_elem = line_list[i + 7]
    nineth_elem = line_list[i + 8]
    tenth_elem = line_list[i + 9]
    eleventh_elem = line_list[i + 10]
    twelweth_elem = line_list[i + 11]
    thirteenth_elem = line_list[i+12]
    fourteenth_elem = line_list[i+13]

    fourteen_chr_list.append(line_list[i])
    fourteen_chr_list.append(second_elem)
    fourteen_chr_list.append(third_elem)
    fourteen_chr_list.append(fourth_elem)
    fourteen_chr_list.append(fifth_elem)
    fourteen_chr_list.append(sixth_elem)
    fourteen_chr_list.append(seventh_elem)
    fourteen_chr_list.append(eight_elem)
    fourteen_chr_list.append(nineth_elem)
    fourteen_chr_list.append(tenth_elem)
    fourteen_chr_list.append(eleventh_elem)
    fourteen_chr_list.append(twelweth_elem)
    fourteen_chr_list.append(thirteenth_elem)
    fourteen_chr_list.append(fourteenth_elem)

    list_set=set(fourteen_chr_list)


    if len(list_set)==len(fourteen_chr_list):
        print(i+14)
        break

    fourteen_chr_list.clear()
    list_set.clear()