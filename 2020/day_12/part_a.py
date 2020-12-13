import utils

# fetch data
data = utils.line_to_list('input_files/aoc_12.txt')

def determine_heading(cur, pos, deg):
    val = int(int(deg) / 90)
    if val % 4 == 0:
        cardinal = cur
    elif val % 4 == 1 or val % 4 == 3:
        if val % 4 == 3:
            pos = not pos
        if pos and cur == 'N':
            cardinal = 'E'
        elif pos and cur == 'E':
            cardinal = 'S'
        elif pos and cur == 'S':
            cardinal = 'W'
        elif pos and cur == 'W':
            cardinal = 'N'
        elif not pos and cur == 'N':
            cardinal = 'W'
        elif not pos and cur == 'E':
            cardinal = 'N'
        elif not pos and cur == 'S':
            cardinal = 'E'
        elif not pos and cur == 'W':
            cardinal = 'S'
    elif val % 4 == 2:
        if cur == 'N':
            cardinal = 'S'
        elif cur == 'E':
            cardinal = 'W'
        elif cur == 'S':
            cardinal = 'N'
        elif cur == 'W':
            cardinal = 'E'
    return cardinal

### START SOLUTION BODY ###

# find the Manhattan distance between origin and destination
found, answer = False, None
x, y = 0, 0
heading = 'E'
for item in data:
    if item[0] == 'N' or (item[0] == 'F' and heading == 'N'):
        y -= int(item[1:])
    elif item[0] == 'E' or (item[0] == 'F' and heading == 'E'):
        x += int(item[1:])
    elif item[0] == 'S' or (item[0] == 'F' and heading == 'S'):
        y += int(item[1:])
    elif item[0] == 'W' or (item[0] == 'F' and heading == 'W'):
        x -= int(item[1:])
    elif item[0] == 'L':
        heading = determine_heading(heading, False, item[1:])
    elif item[0] == 'R':
        heading = determine_heading(heading, True, item[1:])
answer = abs(x) + abs(y)
found = True

### END SOLUTION BODY ###

# output result
utils.one_val_out(found, answer)

