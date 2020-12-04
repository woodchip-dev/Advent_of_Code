import utils

# fetch data
data = utils.line_to_list('input_files/aoc_03.txt')

### START SOLUTION BODY ###

# find how many collisions with trees there'd be while travelling R3,D1
found, answer = False, 0
width, height, x = len(data[0]), len(data), 0
for y in range(height):
    if data[y][x] == '#':
        answer += 1
    x += 3
    x %= width
found = True

### END SOLUTION BODY ###

# output result
utils.one_val_out(found, answer)

