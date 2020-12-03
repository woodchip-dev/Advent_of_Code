import utils

# fetch data
data = utils.line_to_list('input_files/aoc_03.txt')

### START SOLUTION BODY ###

def calculate_collisions(data, x_inc, y_inc):
    width, height = len(data[0]), len(data)
    x, count = 0, 0
    for y in range(0, height, y_inc):
        if data[y][x] == '#':
            count = count + 1
        x = x + x_inc
        if x >= width:
            x = x - width
    return count

# find the product of tree collisions for R1,D1; R3,D1; R5,D1; R7,D1; R1,D2
found, answer = False, 0
slopes = [(1,1),(3,1),(5,1),(7,1),(1,2)]
answer = calculate_collisions(data, slopes[0][0], slopes[0][1])
iter_slopes = iter(slopes)
next(iter_slopes)
for item in iter_slopes:
    answer = answer * calculate_collisions(data, item[0], item[1])
found = True

### END SOLUTION BODY ###

# output result
utils.one_val_out(found, answer)

