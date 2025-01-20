import numpy as np

loc_list=[]
grid_size=700
grid = [[0]*grid_size for x in range(grid_size)]

with open("input_day14.txt") as myfile:
    for line in myfile.readlines():
        coordinates = []
        for items in line.strip().split('->'):
            coordinates.append([int(x) for x in items.split(',')])
        loc_list.append(coordinates)

    for item in loc_list:
        position = item[0]
        grid[position[0]][position[1]] = 1
        for i in range(1,len(item)):
            differance_x = item[i][0]- item[i-1][0]
            differance_y = item[i][1] - item[i - 1][1]
            abs_diff= max(abs(differance_x), abs(differance_y))
            for count in range (abs_diff):
                position[0] += (0 if differance_x == 0 else -1 if differance_x < 0 else 1)
                position[1] += (0 if differance_y == 0 else -1 if differance_y < 0 else 1)
                grid[position[0]][position[1]] = 1

sand=0
while True:
    position=[500,0]
    landed= False
    while True:
        if position[1]>=grid_size-1:
            print(sand)
            break
        if grid[position[0]][position[1]+1]==0:
            position[1]+=1
        elif grid[position[0]-1][position[1]+1]==0:
            position[0]-=1
            position[1]+=1
        elif grid[position[0]+1][position[1]+1]==0:
            position[0]+=1
            position[1]+=1
        else:
            grid[position[0]][position[1]]=2
            sand+=1
            landed=True
            break
    if landed==False:
        break

# part 2

def secondPart(input):
    grid, sand_land_surface = gridParsing(input)

    sand_tiles = 0
    added_sand = sand_movement(grid, sand_land_surface)
    while grid[500, 0] == 0:
        grid[added_sand[0], added_sand[1]] = 1
        sand_tiles += 1
        added_sand = sand_movement(grid, sand_land_surface)
    print(sand_tiles)


def sand_movement(grid, sand_land_surface):
    sand_to_move = (500,0)
    ending_surface = sand_land_surface + 2
    while sand_to_move[1]+1 < ending_surface:
        if grid[sand_to_move[0]+1, sand_to_move[1]+1] == 0:
            sand_to_move = (sand_to_move[0]+1, sand_to_move[1]+1)

        elif grid[sand_to_move[0], sand_to_move[1]+1] == 0:
            sand_to_move = (sand_to_move[0], sand_to_move[1]+1)

        elif grid[sand_to_move[0]-1, sand_to_move[1]+1] == 0:
            sand_to_move = (sand_to_move[0]-1, sand_to_move[1]+1)

        else:
            return sand_to_move
    return sand_to_move


def gridParsing(input):
    with open(input, 'r') as myfile:
        lines = myfile.readlines()
        lines = [start.strip() for start in lines]

    grid = np.zeros((7000, 300))
    sand_land_surface = 0
    for line in lines:
        edges = line.split(' -> ')
        for i in range(len(edges) - 1):
            first_edge, last_edge = edges[i], edges[i + 1]
            axis_x = [int(first_edge.split(',')[0]), int(last_edge.split(',')[0])]
            axis_y = [int(first_edge.split(',')[1]), int(last_edge.split(',')[1])]
            for x in range(min(axis_x), max(axis_x) + 1):
                for y in range(min(axis_y), max(axis_y) + 1):
                    if y > sand_land_surface:
                        sand_land_surface = y
                    grid[x, y] = 1
    return grid, sand_land_surface



secondPart('input_day14.txt')