import utils

# fetch data
data = utils.line_to_list('input_files/aoc_17.txt')

### START SOLUTION BODY ###

def get_neighbors(x, y, z):
    return [(i, j, k) for i in range(x - 1, x + 2) for j in range(y - 1, y + 2) for k in range(z - 1, z + 2) if not i == x or not j == y or not k == z]

# find the number of active cubes after the 6th cycle
found, answer = False, 0
grid = [line for line in data]
offset = (1 - len(grid)) // 2
space, counts = {}, {}
for y in range(len(grid)):
    for x in range(len(grid[y])):
        space[(x + offset, y + offset, 0)] = grid[y][x]
        if grid[y][x] == '#':
            counts[(x + offset, y + offset, 0)] = 1
        else:
            counts[(x + offset, y + offset, 0)] = 0
for idx in range(6):
    X, Y, Z = zip(*space.keys())
    x1, x2 = min(X), max(X)
    y1, y2 = min(Y), max(Y)
    z1, z2 = min(Z), max(Z)
    for i in range(x1 - 1, x2 + 2):
        for j in range(y1 - 1, y2 + 2):
            for k in range(z1 - 1, z2 + 2):
                loc = (i, j, k)
                if loc not in space:
                    space[loc] = '.'
                    counts[loc] = 0
    temp = {}
    for shape in space:
        active = 0
        for neighbors in get_neighbors(*shape):
            if space.get(neighbors, '.') == '#':
                active += 1
        if (space[shape] == '#' and (active == 2 or active == 3)) or (space[shape] == '.' and active == 3):
            temp[shape] = '#'
            counts[shape] += 1
        else:
            temp[shape] = '.'
            counts[shape] -= 1
    space = temp
for val in space:
    if space[val] == '#':
        answer += 1
found = True

### END SOLUTION BODY ###

# output result
utils.one_val_out(found, answer)

