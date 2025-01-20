with open ("input_day15.txt") as myfile:
    lines=myfile.readlines()

searching_grid=[]
y_axis= 2000000
loc_diffs=[]
y_pos=[]
x_pos=[]
to_compare_left=0
to_compare_right=0
for line in lines:
    line = line.strip().split(':')
    sensorx= line[0].split()[2]
    sensor_x= int(sensorx.split('=')[1][:-1])
    sensory = line[0].split()[3]
    sensor_y = int(sensory.split('=')[1])
    beaconx = line[1].split()[4]
    beacon_x = int(beaconx.split('=')[1][:-1])
    beacony = line[1].split()[5]
    beacon_y = int(beacony.split('=')[1])

    manhatten_d =abs(sensor_x - beacon_x) + abs(sensor_y - beacon_y)

    right_grid = sensor_x + manhatten_d
    left_grid = sensor_x - manhatten_d
    up_grid = sensor_y - manhatten_d
    down_grid = sensor_y + manhatten_d
    searching_grid.append([[left_grid,up_grid], [right_grid, down_grid]])

for i in range(len(searching_grid)):

    if searching_grid[i][0][1] <= y_axis <= searching_grid[i][1][1]:
        new_y = (searching_grid[i][0][1] + searching_grid[i][1][1])//2
        distance_to_d =abs(y_axis - new_y)
        loc_diffs.append([searching_grid[i][0][0] + distance_to_d, searching_grid[i][1][0] - distance_to_d])


for locs in loc_diffs:
    x_pos.append(locs[0])
    y_pos.append(locs[1])

result= max(y_pos) - min(x_pos)
print(result)

x_y_cut= 4000000
# part two
for line in range(x_y_cut):
    loc_diffs =[]
    for i in range(len(searching_grid)):
        if searching_grid[i][0][1] <= line <= searching_grid[i][1][1]:
            new_y = (searching_grid[i][0][1] + searching_grid[i][1][1])//2
            distance_to_d =abs(line - new_y)
            loc_diffs.append([searching_grid[i][0][0] + distance_to_d, searching_grid[i][1][0] - distance_to_d])
    to_compare_left = 0
    to_compare_right = 0
    while to_compare_left < len(loc_diffs):
        while to_compare_right < len(loc_diffs):
            if to_compare_right != to_compare_left:
                left_left = loc_diffs[to_compare_left][0]
                left_right = loc_diffs [to_compare_left][1]
                right_left = loc_diffs [to_compare_right][0]
                right_right = loc_diffs [to_compare_right][1]
                if (left_right >= right_left) and (right_right>= left_left):
                    between_range = [ min( left_left, right_left), max([left_right, right_right])]
                    loc_diffs.append(between_range)
                    del loc_diffs[max( to_compare_left, to_compare_right)]
                    del loc_diffs[min(to_compare_left, to_compare_right)]
                    to_compare_left =0
                    to_compare_right = -1
            to_compare_right +=1
        to_compare_left +=1
    if len(loc_diffs)==2:
        print(line, loc_diffs)
