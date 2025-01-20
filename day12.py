with open('input_day12.txt', 'r') as myfile:
    lines = myfile.read().split()

step_counter=0
space: dict[tuple[int,int]] = {}
start_loc = None
end_loc = None

elevation_dict={"a":0, "b": 1, "c": 2, "d": 3,"e": 4, "f": 5, "g": 6, "h": 7, "i": 8, "j": 9, "k": 10, "l": 11,"m": 12,
                "n": 13, "o": 14,"p": 15, "q": 16,"r": 17, "s": 18, "t": 19, "u": 20, "v": 21, "w": 22, "x": 23, "y": 24,
                "z": 25}

for x, line in enumerate(lines):
    for y, letter in enumerate(line):
        if letter == "S":
            space[(x, y)] = 0
            start_loc = (x, y)
        elif letter == "E":
            space[(x, y)] = 25
            end_loc = (x, y)
        else:
            space[(x,y)] = elevation_dict.get(letter)

def move_one_pos (space: dict[tuple[int, int], int], loc_on_space: set[tuple[int, int]]) -> set[tuple[int, int]]:

    step_locations=set()
    for axis in loc_on_space:
        for take_x, take_y in ((0, 1), (0, -1), (1, 0), (-1, 0)):
            new_loc = (axis[0] + take_x, axis[1] + take_y)
            if new_loc in space and space[new_loc] <= space[axis] + 1:
                step_locations.add(new_loc)
    return step_locations

loc_on_space = set()
loc_on_space.add(start_loc)
while end_loc not in loc_on_space:
    loc_on_space = move_one_pos(space, loc_on_space)
    step_counter += 1

print(step_counter)

# Part two

backwards_step_counter=0

def move_one_pos_back (space: dict[tuple[int, int], int], loc_on_space: set[tuple[int, int]]) -> set[tuple[int, int]]:
    step_locations_back = set()
    for axis in loc_on_space:
        for take_x, take_y in ((0, 1), (0, -1), (1, 0), (-1, 0)):
            new_loc = (axis[0] + take_x, axis[1] + take_y)
            if new_loc in space and space[axis] <= space[new_loc] + 1:
                step_locations_back.add(new_loc)
    return step_locations_back


loc_on_space = set()
loc_on_space.add(end_loc)
elevation=[]
for elements in loc_on_space:
    elevation.append(space[elements])

while 0 not in elevation:
    loc_on_space = move_one_pos_back(space, loc_on_space)
    elevation = {space[elements] for elements in loc_on_space}
    backwards_step_counter += 1

print(backwards_step_counter)






