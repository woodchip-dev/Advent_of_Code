import utils

# fetch data
data = utils.line_to_list('input_files/aoc_12.txt')

def determine_heading(cur, pos, deg, wx, wy):
    val = int(int(deg) / 90)
    if val % 4 == 0:
        cardinal = cur
    elif val % 4 == 1 or val % 4 == 3:
        if val % 4 == 3:
            pos = not pos
        if pos:
            wx, wy = wy, -wx
            if cur == 'N':
                cardinal = 'E'
            elif cur == 'E':
                cardinal = 'S'
            elif cur == 'S':
                cardinal = 'W'
            elif cur == 'W':
                cardinal = 'N'
        else:
            wx, wy = -wy, wx
            if cur == 'N':
                cardinal = 'W'
            elif cur == 'E':
                cardinal = 'N'
            elif cur == 'S':
                cardinal = 'E'
            elif cur == 'W':
                cardinal = 'S'
    elif val % 4 == 2:
        wx, wy = -wx, -wy
        if cur == 'N':
            cardinal = 'S'
        elif cur == 'E':
            cardinal = 'W'
        elif cur == 'S':
            cardinal = 'N'
        elif cur == 'W':
            cardinal = 'E'
    return cardinal, wx, wy

### START SOLUTION BODY ###

# find the Manhattan distance between origin and destination given the waypoint
found, answer = False, None
x, y = 0, 0
wx, wy = 10, 1
heading = 'E'
for item in data:
    if item[0] == 'N':
        wy += int(item[1:])
    elif item[0] == 'E':
        wx += int(item[1:])
    elif item[0] == 'S':
        wy -= int(item[1:])
    elif item[0] == 'W':
        wx -= int(item[1:])
    elif item[0] == 'L':
        heading, wx, wy = determine_heading(heading, False, item[1:], wx, wy)
    elif item[0] == 'R':
        heading, wx, wy = determine_heading(heading, True, item[1:], wx, wy)
    elif item[0] == 'F':
        x += wx * int(item[1:])
        y += wy * int(item[1:])
answer = abs(x) + abs(y)
found = True

### END SOLUTION BODY ###

# output result
utils.one_val_out(found, answer)

