with open('input_day9.2.txt', 'r') as myfile:
    lines = myfile.read().strip().split()

head = [0, 0]
tail = [0, 0]
moves = []
head_positions = []
tail_positions = []

for line in lines:
    moves.append(line)

def tail_travel(tail: [int, int], head: [int, int]) -> [int, int]:
    match head[0] - tail[0], head[1] - tail[1]:
        case _ as loc1, _ as loc2 if abs(loc2) <= 1 and abs(loc1) <= 1 :
            return (tail[0], tail[1])
        case 0, _ as loc2:
            return (tail[0], tail[1] + loc2 // abs(loc2))
        case _ as loc1, 0:
            return (tail[0] + loc1 // abs(loc1), tail[1])
        case _ as loc1, _ as loc2:
            return (tail[0] + loc1 // abs(loc1), tail[1] + loc2 // abs(loc2))
    return (0, 0)

for i in range(0, len(moves)):
    if moves[i] == 'U':
        for k in range(0, int(moves[i + 1])):
            head[1] = head[1] + 1
            new_head = [head[0], head[1]]
            head_positions.append(new_head)
    if moves[i] == 'D':
        for k in range(0, int(moves[i + 1])):
            head[1] = head[1] - 1
            new_head = [head[0], head[1]]
            head_positions.append(new_head)
    if moves[i] == 'L':
        for k in range(0, int(moves[i + 1])):
            head[0] = head[0] - 1
            new_head = [head[0], head[1]]
            head_positions.append(new_head)
    if moves[i] == 'R':
        for k in range(0, int(moves[i + 1])):
            head[0] = head[0] + 1
            new_head = [head[0], head[1]]
            head_positions.append(new_head)

for i in range(0, len(head_positions)):
    tail=tail_travel(tail, head_positions[i])
    tail_positions.append(tail)


set_tail_positions = []


for elem in tail_positions:
    if elem not in set_tail_positions:

        set_tail_positions.append(elem)

print(len(set_tail_positions))

# part 2
tail_positions.clear()
tails=[(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0)]

for i in range(0, len(head_positions)):
    tails[0] = head_positions[i]
    for k in range(1, len(tails)):
        tails[k] = tail_travel(tails[k], tails[k - 1])
    tail_positions.append(tails[-1])

set_tail_positions = []

for elem in tail_positions:
    if elem not in set_tail_positions:
        set_tail_positions.append(elem)

print(len(set_tail_positions))






