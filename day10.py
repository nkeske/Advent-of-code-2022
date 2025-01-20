with open('input_day10.txt', 'r') as myfile:
    lines = myfile.read().strip().split()

lines_list = []
value_x = 0
result_list = []
for line in lines:
    lines_list.append(line)
cycle_counter = 0
value_list = []
value_x = 1
for i in range(0, len(lines_list)):

    if lines_list[i] == "noop":

        cycle_counter += 1
        if cycle_counter == 20:
            value_list.append(value_x)
        elif cycle_counter == 60:
            value_list.append(value_x)
        elif cycle_counter == 100:
            value_list.append(value_x)
        elif cycle_counter == 140:
            value_list.append(value_x)
        elif cycle_counter == 140:
            value_list.append(value_x)
        elif cycle_counter == 180:
            value_list.append(value_x)
        elif cycle_counter == 220:
            value_list.append(value_x)

    elif lines_list[i] == "addx":

        cycle_counter += 1
        value_to_add = int(lines_list[i + 1])
        if cycle_counter == 20:
            value_list.append(value_x)

        elif cycle_counter == 60:
            value_list.append(value_x)

        elif cycle_counter == 100:
            value_list.append(value_x)

        elif cycle_counter == 140:
            value_list.append(value_x)

        elif cycle_counter == 140:
            value_list.append(value_x)

        elif cycle_counter == 180:
            value_list.append(value_x)

        elif cycle_counter == 220:
            value_list.append(value_x)

        cycle_counter += 1

        if cycle_counter == 20:
            value_list.append(value_x)

        elif cycle_counter == 60:
            value_list.append(value_x)

        elif cycle_counter == 100:
            value_list.append(value_x)

        elif cycle_counter == 140:
            value_list.append(value_x)

        elif cycle_counter == 140:
            value_list.append(value_x)

        elif cycle_counter == 180:
            value_list.append(value_x)

        elif cycle_counter == 220:
            value_list.append(value_x)

        value_x += value_to_add

result = (value_list[0] * 20) + (value_list[1] * 60) + (value_list[2] * 100) + (value_list[3] * 140) + (
            value_list[4] * 180) + (value_list[5] * 220)
print(result)


# Part two

def CRT_machine(filename: str) -> None:
    x_after_operation = input(filename)
    marked = []
    for loc in range(240):
        cycle_counter = loc + 1
        x_reg = cycle_to_xvalues(x_after_operation, cycle_counter)
        if -1 <= loc % 40 - x_reg <= 1:
            marked.append(loc)
    CRT_marked(marked)


def cycle_to_xvalues(x_after_operation: dict[int, int], cycle_counter: int) -> int:
    if cycle_counter in x_after_operation:
        return x_after_operation[cycle_counter]
    elif cycle_counter - 1 in x_after_operation:
        return x_after_operation[cycle_counter - 1]
    elif cycle_counter - 2 in x_after_operation:
        return x_after_operation[cycle_counter - 2]
    else:
        raise ValueError(f"Register value not found for {cycle_counter=}")


def CRT_marked(marked: list[int]) -> None:
    for axis1 in range(6):
        for axis2 in range(40):
            if axis2 + axis1 * 40 in marked:
                print("#", end="")
            else:
                print(".", end="")
        print()


def input(filename: str) -> dict[int, int]:
    with open(filename, encoding="utf8") as file:
        lines = [line.strip() for line in file.readlines()]
    value_x = 1
    cycle_counter = 1
    x_after_operation = {cycle_counter: value_x}
    for line in lines:
        match line.split(" "):
            case ["noop"]:
                cycle_counter += 1
            case ["addx", val]:
                cycle_counter += 2
                value_x += int(val)
        x_after_operation[cycle_counter] = value_x
    return x_after_operation


if __name__ == "__main__":
    input_path = "input_day10.txt"
    CRT_machine(input_path)
