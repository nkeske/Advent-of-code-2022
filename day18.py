with open("input_day18.txt") as myfile:
    lines = myfile.read().strip().split("\n")
total_sides =0
lava_coordinates = []

for line in lines:
    x, y, z = map(int, line.split(","))
    lava_coordinates.append((x, y, z))

for i in range(len(lava_coordinates)):
    sides_of_droplet=6
    lava_drop = lava_coordinates[i]
    x_to_check_right = lava_coordinates[i][0] + 1
    if (x_to_check_right, lava_coordinates[i][1], lava_coordinates[i][2]) in lava_coordinates:
        sides_of_droplet-=1
    x_to_check_left = lava_coordinates[i][0] -1
    if (x_to_check_left, lava_coordinates[i][1], lava_coordinates[i][2]) in lava_coordinates:
        sides_of_droplet -= 1
    y_to_check_right = lava_coordinates[i][1] + 1
    if (lava_coordinates[i][0], y_to_check_right , lava_coordinates[i][2]) in lava_coordinates:
        sides_of_droplet-=1
    y_to_check_left = lava_coordinates[i][1] -1
    if (lava_coordinates[i][0], y_to_check_left , lava_coordinates[i][2]) in lava_coordinates:
        sides_of_droplet-=1
    z_to_check_right = lava_coordinates[i][2] +1
    if (lava_coordinates[i][0], lava_coordinates[i][1], z_to_check_right) in lava_coordinates:
        sides_of_droplet -= 1
    z_to_check_left = lava_coordinates[i][2] -1
    if (lava_coordinates[i][0], lava_coordinates[i][1], z_to_check_left) in lava_coordinates:
        sides_of_droplet -= 1

    total_sides+=sides_of_droplet

print(total_sides)

# Part 2
from collections import deque

sides = {}

sides_to_walk = [(0, 0, 0.5),
                 (0, 0.5, 0),
                 (0.5, 0, 0),
                 (0, 0, -0.5),
                 (0, -0.5, 0),
                 (-0.5, 0, 0)]

Min_x =100000
Min_y = 100000
Min_z = 100000
Max_x = -100000
Max_y = -100000
Max_z = -100000

lava_drop = set()

for line in lines:
    x, y, z = cube = tuple(map(int, line.split(",")))
    lava_drop.add(cube)
    for dx, dy, dz in sides_to_walk:
        cube_neigbor = (x + dx, y + dy, z + dz)
        if cube_neigbor not in sides:
            sides[cube_neigbor] = 0
        sides[cube_neigbor] += 1

    Min_x = min(Min_x, x) ; Min_y = min(Min_y, y); Min_z = min(Min_z, z)
    Max_x = max(Max_x, x); Max_y = max(Max_y, y); Max_z = max(Max_z, z)


Min_x -= 1; Min_y -= 1; Min_z -= 1
Max_x += 1; Max_y += 1; Max_z += 1

geom = deque([(Min_x, Min_y, Min_z)])
drop_in_air = {(Min_x, Min_y, Min_z)}

while geom:
    x, y, z = geom.popleft()

    for dx, dy, dz in sides_to_walk:
        nx, ny, nz = cube_neigbor = (x + dx * 2, y + dy * 2, z + dz * 2)

        if not (Min_x <= nx <= Max_x and Min_y <= ny <= Max_y and Min_z <= nz <= Max_z):
            continue

        if cube_neigbor in lava_drop or cube_neigbor in drop_in_air:
            continue

        drop_in_air.add(cube_neigbor)
        geom.append(cube_neigbor)

surfical_faces = set()

for x, y, z in drop_in_air:
    for dx, dy, dz in sides_to_walk:
        surfical_faces.add((x + dx, y + dy, z + dz))

print(len(set(sides) & surfical_faces))