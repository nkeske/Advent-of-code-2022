list_1 = ['D','L', 'V', 'T', 'M', 'H', 'F']
list_2 = ['H','Q', 'G', 'J', 'C', 'T', 'N', 'P']
list_3 = ['R','S', 'D', 'M', 'P', 'H']
list_4 = ['L','B', 'V', 'F']
list_5 = ['N','H', 'G', 'L', 'Q']
list_6 = ['W','B', 'D', 'G', 'R', 'M', 'P']
list_7 = ['G','M', 'N', 'R', 'C', 'H', 'L', 'Q']
list_8 = ['C','L', 'W']
list_9 = ['R','D', 'L', 'Q', 'J', 'Z', 'M', 'T']
list_to_pop=[]
list_to_append=[]
number_items=[]
line_words=[]
with open('input_day5.txt', 'r') as myfile:
    lines = myfile.read().strip().split()

for item in lines:
    line_words.append(item)

    for sub_item in item.split():
        if sub_item.isdigit():
            number_items.append(sub_item)

# removing first nine element which are not a statement

number_items.pop(0)
number_items.pop(0)
number_items.pop(0)
number_items.pop(0)
number_items.pop(0)
number_items.pop(0)
number_items.pop(0)
number_items.pop(0)
number_items.pop(0)


for i in range(0, len(number_items)-2,3):

    number_of_moves = int (number_items[i])
    if int(number_items[i+1])==1:
        list_to_pop=list_1
    elif int(number_items[i+1])==2:
        list_to_pop=list_2
    elif int(number_items[i+1])==3:
        list_to_pop=list_3
    elif int(number_items[i+1])==4:
        list_to_pop=list_4
    elif int(number_items[i+1])==5:
        list_to_pop=list_5
    elif int(number_items[i+1])==6:
        list_to_pop=list_6
    elif int(number_items[i+1])==7:
        list_to_pop=list_7
    elif int(number_items[i+1])==8:
        list_to_pop=list_8
    elif int(number_items[i+1])==9:
        list_to_pop=list_9

    if int(number_items[i + 2]) == 1:
        list_to_append = list_1
    elif int(number_items[i + 2]) == 2:
        list_to_append = list_2
    elif int(number_items[i + 2]) == 3:
        list_to_append = list_3
    elif int(number_items[i + 2]) == 4:
        list_to_append = list_4
    elif int(number_items[i + 2]) == 5:
        list_to_append = list_5
    elif int(number_items[i + 2]) == 6:
        list_to_append = list_6
    elif int(number_items[i + 2]) == 7:
        list_to_append = list_7
    elif int(number_items[i + 2]) == 8:
        list_to_append = list_8
    elif int(number_items[i + 2]) == 9:
        list_to_append = list_9


    for k in range (0, number_of_moves):
        list_to_append.append(list_to_pop[-1])
        list_to_pop.pop(-1)



print("Result1")
print(list_1[-1])
print(list_2[-1])
print(list_3[-1])
print(list_4[-1])
print(list_5[-1])
print(list_6[-1])
print(list_7[-1])
print(list_8[-1])
print(list_9[-1])

#part 2
list_1 = ['D','L', 'V', 'T', 'M', 'H', 'F']
list_2 = ['H','Q', 'G', 'J', 'C', 'T', 'N', 'P']
list_3 = ['R','S', 'D', 'M', 'P', 'H']
list_4 = ['L','B', 'V', 'F']
list_5 = ['N','H', 'G', 'L', 'Q']
list_6 = ['W','B', 'D', 'G', 'R', 'M', 'P']
list_7 = ['G','M', 'N', 'R', 'C', 'H', 'L', 'Q']
list_8 = ['C','L', 'W']
list_9 = ['R','D', 'L', 'Q', 'J', 'Z', 'M', 'T']

list_to_pop1=[]
list_to_append1=[]
number_items=[]
line_words=[]

with open('input_day5.txt', 'r') as myfile:
    lines = myfile.read().strip().split()

for item in lines:
    line_words.append(item)

    for sub_item in item.split():
        if sub_item.isdigit():
            number_items.append(sub_item)

# removing first nine element which are not a statement

number_items.pop(0)
number_items.pop(0)
number_items.pop(0)
number_items.pop(0)
number_items.pop(0)
number_items.pop(0)
number_items.pop(0)
number_items.pop(0)
number_items.pop(0)


for i in range(0, len(number_items)-2,3):

    number_of_moves = int (number_items[i])
    if int(number_items[i+1])==1:
        list_to_pop1=list_1
    elif int(number_items[i+1])==2:
        list_to_pop1=list_2
    elif int(number_items[i+1])==3:
        list_to_pop1=list_3
    elif int(number_items[i+1])==4:
        list_to_pop1=list_4
    elif int(number_items[i+1])==5:
        list_to_pop1=list_5
    elif int(number_items[i+1])==6:
        list_to_pop1=list_6
    elif int(number_items[i+1])==7:
        list_to_pop1=list_7
    elif int(number_items[i+1])==8:
        list_to_pop1=list_8
    elif int(number_items[i+1])==9:
        list_to_pop1=list_9

    if int(number_items[i + 2]) == 1:
        list_to_append1 = list_1
    elif int(number_items[i + 2]) == 2:
        list_to_append1 = list_2
    elif int(number_items[i + 2]) == 3:
        list_to_append1 = list_3
    elif int(number_items[i + 2]) == 4:
        list_to_append1 = list_4
    elif int(number_items[i + 2]) == 5:
        list_to_append1 = list_5
    elif int(number_items[i + 2]) == 6:
        list_to_append1 = list_6
    elif int(number_items[i + 2]) == 7:
        list_to_append1 = list_7
    elif int(number_items[i + 2]) == 8:
        list_to_append1 = list_8
    elif int(number_items[i + 2]) == 9:
        list_to_append1 = list_9

    for k in range(number_of_moves, 0,-1):
        list_to_append1.append(list_to_pop1[-k])
        list_to_pop1.pop(-k)



print("Result2")
print(list_1[-1])
print(list_2[-1])
print(list_3[-1])
print(list_4[-1])
print(list_5[-1])
print(list_6[-1])
print(list_7[-1])
print(list_8[-1])
print(list_9[-1])
