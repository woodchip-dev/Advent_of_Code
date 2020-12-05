import utils

# fetch data
data = utils.line_to_list('input_files/aoc_05.txt')

### START SOLUTION BODY ###

# find the highest seat ID on a boarding pass
found, answer = False, None
seats = []
for item in data:
    rows, row = 128, 0
    for ch in item:
        rows /= 2
        if ch == 'B' or ch == 'R':
            row += rows
    seats.append(int(row * 8))
answer = max(seats)
found = True

### END SOLUTION BODY ###

# output result
utils.one_val_out(found, answer)

