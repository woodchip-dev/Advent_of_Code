import utils

# fetch data
data = utils.lines_to_ints('input_files/aoc_10.txt')

### START SOLUTION BODY ###

# find the product of the number of 1- and 3-volt differences
found, answer = False, 0
data.sort()
ones, threes = 1, 1
for idx in range(len(data) - 1):
    if data[idx + 1] == data[idx] + 1:
        ones += 1
    elif data[idx + 1] == data[idx] + 3:
        threes += 1
answer = ones * threes
found = True

### END SOLUTION BODY ###

# output result
utils.one_val_out(found, answer)

