import utils

# fetch data
data = utils.line_to_list('input_files/aoc_02.txt')

### START SOLUTION BODY ###

# find how many passwords are valid according to their respective policy
found, answer = False, 0
for item in data:
    range_vals, char, password = item.split(' ')
    low, high = range_vals.split('-')
    count = password.count(char[:-1])
    if int(low) <= count and count <= int(high):
        answer = answer + 1
found = True

### END SOLUTION BODY ###

# output result
utils.one_val_out(found, answer)

