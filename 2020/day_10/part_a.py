import utils

# fetch data
data = utils.lines_to_ints('input_files/aoc_10.txt')

### START SOLUTION BODY ###

# find the product of the number of 1- and 3-volt differences
found, answer = False, 0
ones, threes = 1, 1
for item in data:
    if item + 1 in data:
        ones += 1
    elif item + 3 in data:
        threes += 1
answer = ones * threes
found = True

### END SOLUTION BODY ###

# output result
utils.one_val_out(found, answer)

