with open("input_day7.txt") as file:
    lines = file.readlines()

directories = {"/root": 0}
path = "/root"

for line in lines:

    if line[0] == "$":
        if line[2:4] == "cd":
            if line[5:7] == "..":
                path = path[0:path.rfind("/")]
            elif line[5:6] == "/":
                path = "/root"
            else:
                current_dir = line[5:]
                path = path + "/" + current_dir
                directories.update({path: 0})
        elif line[2:4] == "ls":
            pass

    elif line[0:3] == "dir":
        pass

    else:
        size_of_dir = int(line[:line.find(" ")])
        new_dir = path
        for i in range(path.count("/")):
            directories[new_dir] += size_of_dir
            new_dir = new_dir[:new_dir.rfind("/")]

size_total = 0

for new_dir in directories:

    if 100000>directories[new_dir]:
        size_total += directories[new_dir]

#part 2

to_cutoff=70000000 - directories["/root"]
cutoff = 30000000 - to_cutoff
dirs_to_use = []

for new_dir in directories:
    if cutoff <= directories[new_dir]:
        dirs_to_use.append(directories[new_dir])

print( size_total)
print( min(dirs_to_use))