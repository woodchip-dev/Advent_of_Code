import utils

# fetch data
data = utils.line_to_list('input_files/aoc_11.txt')

### START SOLUTION BODY ###

def identify_adjacents(data, width, height, tx, ty):
    temp = []
    paths = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    for path in paths:
        if (not path[0] == 0 or not path[1] == 0) and ((tx + path[0] >= 0 and tx + path[0] < width) and (ty + path[1] >= 0 and ty + path[1] < height)):
            temp.append(data[ty + path[1]][tx + path[0]])
    return temp

# find how many seats end up occupied
found, answer = False, None
width, height = len(data[0]), len(data)
for idx in range(len(data)):
    data[idx] = [char for char in data[idx]]

count = 0
while 1:
    storage = {}
    for idx in range(width):
        for idy in range(height):
            storage[(idx, idy)] = identify_adjacents(data, width, height, idx, idy)
    changed = False
    for item in storage:
        if data[item[1]][item[0]] == 'L' and storage[item].count('#') == 0:
            data[item[1]][item[0]] = '#'
            count += 1
            changed = True
        elif data[item[1]][item[0]] == '#' and storage[item].count('#') >= 4:
            data[item[1]][item[0]] = 'L'
            count -= 1
            changed = True
    if not changed:
        break
answer = count
found = True

### END SOLUTION BODY ###

# output result
utils.one_val_out(found, answer)

