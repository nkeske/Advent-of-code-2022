def solveEncription():
    pin_result = 0
    locs = [1000, 2000, 3000]

    with open("input_day20.txt") as myfile:
        lines = myfile.read().split()
    pin_items = [int(line) for line in lines]

    right_item = {k: (k + 1) % len(pin_items) for k in range(len(pin_items))}
    left_item = {v: k for k, v in right_item.items()}

    for item_coord in range(len(pin_items)):
        walkEncription(item_coord, pin_items, right_item, left_item)

    starting_item = 0
    while pin_items[starting_item] != 0:
        starting_item = right_item[starting_item]

    for i in range(1, locs[2] + 1):
        starting_item = right_item[starting_item]
        if i in locs:
            pin_result += pin_items[starting_item]

    print(pin_result)


def walkEncription(item_coord, items, right_item, left_item):
    walk_after_loop = items[item_coord] % (len(items) - 1)

    if walk_after_loop == 0:
        return

    assert walk_after_loop > 0

    left_before_walk = left_item[item_coord]
    right_before_walk = right_item[item_coord]

    new_right = right_before_walk
    for i in range(walk_after_loop):
        new_right = right_item[new_right]

    new_left = left_item[new_right]

    right_item[left_before_walk] = right_before_walk
    left_item[right_before_walk] = left_before_walk

    right_item[new_left] = item_coord
    right_item[item_coord] = new_right

    left_item[new_right] = item_coord
    left_item[item_coord] = new_left


if __name__ == "__main__":
    solveEncription()


# Part 2
description_key = 811589153

def solveEncriptionTwo():

    pin_result = 0
    locs = [1000, 2000, 3000]

    with open("input_day20.txt") as myfile:
        lines = myfile.read().split()
    pin_items = [int(line) for line in lines]
    pin_items = [pin * description_key for pin in pin_items]

    right_item = {k: (k + 1) % len(pin_items) for k in range(len(pin_items))}
    left_item = {v: k for k, v in right_item.items()}

    for i in range(10):
        for item_coord in range(len(pin_items)):
            walkEncription(item_coord, pin_items, right_item, left_item)

    starting_item = 0
    while pin_items[starting_item] != 0:
        starting_item = right_item[starting_item]

    for i in range(1, locs[2] + 1):
        starting_item = right_item[starting_item]
        if i in locs:
            pin_result += pin_items[starting_item]

    print(pin_result)

if __name__ == "__main__":
    solveEncriptionTwo()