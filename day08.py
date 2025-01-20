with open('input_day8.txt', 'r') as myfile:
    lines = myfile.read().strip().split()
two_dim_array = []
row_array = []
item_array = []
vis_counter=0
for line in lines:
    row_array.append(line)

for i in range(0, len(row_array)):
    item_array = []
    for digits in row_array[i]:
        item_array.append(digits)
    two_dim_array.append(item_array)

x_edge = len(two_dim_array[0])
y_edge = len(two_dim_array)
total_edge = ((2 * x_edge) + (2 * y_edge)) - 4
coordinates = []
coordinates2 = []
coordinates3 = []
coordinates4 = []
visible_tree_coordinates = []

maximum=0


for x in range(0, len(two_dim_array)):
    for y in range(0, len(two_dim_array)):
        coordinates = []
        max = int( two_dim_array[x][y])

        if (maximum < max):

            maximum=max

            vis_counter+=1
            coordinates.append(x)
            coordinates.append(y)

            visible_tree_coordinates.append(coordinates)
    maximum = 0

maximum = 0

for x in range(0, len(two_dim_array)):
    for y in range(len(two_dim_array)-1,-1,-1):
        coordinates2 = []
        max = int( two_dim_array[x][y])

        if (maximum < max):

            maximum=max

            vis_counter+=1
            coordinates2.append(x)
            coordinates2.append(y)

            visible_tree_coordinates.append(coordinates2)
    maximum=0

maximum=0

for y in range(0, len(two_dim_array)):
    for x in range(0, len(two_dim_array)):
        coordinates3 = []
        max = int( two_dim_array[x][y])
        if (maximum < max):
            maximum=max
            vis_counter+=1
            coordinates3.append(x)
            coordinates3.append(y)

            visible_tree_coordinates.append(coordinates3)
    maximum=0
maximum=0

for y in range(0, len(two_dim_array)):
    for x in range(len(two_dim_array)-1,-1,-1):
        coordinates4 = []
        max = int( two_dim_array[x][y])
        if (maximum < max):
            maximum=max
            vis_counter+=1
            coordinates4.append(x)
            coordinates4.append(y)

            visible_tree_coordinates.append(coordinates4)
    maximum=0
maximum=0


new_visible = []
cord_2=[]
new_new=[]

for elem in visible_tree_coordinates:
    if elem not in new_visible:
        new_visible.append(elem)

for i in range(0,len(new_visible)):
    cord_2 = []

    for k in range(0,1):
        if new_visible[i][k] !=0 and new_visible[i][k] !=(len(two_dim_array)-1):
            if new_visible[i][k+1] != 0 and new_visible[i][k+1] != (len(two_dim_array)-1):
                cord_2.append(new_visible[i][k])
                cord_2.append(new_visible[i][k+1])
                new_new.append(cord_2)

print("result:", len(new_new)+ total_edge)

#part 2

with open('input_day8.txt', 'r') as myfile:
    lines = myfile.read().strip().split()
two_dim_array = []
row_array = []
item_array = []
vis_counter=0
for line in lines:
    row_array.append(line)


for i in range(0, len(row_array)):
    item_array = []
    for digits in row_array[i]:
        item_array.append(digits)
    two_dim_array.append(item_array)

left_vis=[]
right_vis=[]
up_vis=[]
down_vis=[]
left_counter=0
right_counter=0
up_counter=0
down_counter=0
object_vis1=[]
object_vis2=[]
object_vis_total=[]

maximum=0
for x in range(0, len(two_dim_array)):
    for y in range(0, len(two_dim_array)):
        left_counter = 0
        right_counter = 0
        up_counter = 0
        down_counter = 0
        for z in range(y, 0, -1):
            left_coordinates=two_dim_array[x][z-1]
            if two_dim_array[x][y] > left_coordinates:
                left_counter += 1
            elif two_dim_array[x][y] <=  left_coordinates:
                left_counter += 1
                break
        left_vis.append(left_counter)

        for k in range(y, len(two_dim_array)-1):
            right_coordinates = two_dim_array[x][k+1]
            if two_dim_array[x][y] > right_coordinates:
                right_counter += 1
            elif two_dim_array[x][y] <= right_coordinates:
                right_counter += 1
                break
        right_vis.append(right_counter)


for x in range(0, len(two_dim_array)):
    for y in range(0, len(two_dim_array)):
        up_counter=0
        down_counter=0

        for k in range (x, 0, -1):
            up_coordinates = two_dim_array[k-1][y]
            if two_dim_array[x][y] > up_coordinates:
                up_counter += 1
            elif two_dim_array[x][y] <= up_coordinates:
                up_counter += 1
                break
        up_vis.append(up_counter)

        for l in range(x+1, len(two_dim_array)):

            down_coordinates=two_dim_array[l][y]
            if two_dim_array[x][y] > down_coordinates:
                down_counter += 1
            elif two_dim_array[x][y] <= down_coordinates:
                down_counter += 1
                break
        down_vis.append(down_counter)



for f in range (0, len(up_vis)):
    result= up_vis[f]*down_vis[f]
    result2=result*right_vis[f]
    result3=result2*left_vis[f]

    object_vis_total.append(result3)
maximum=0
for i in range(0, len(object_vis_total)):
    if object_vis_total[i]>maximum:
        maximum= object_vis_total[i]

print("result:",maximum )





