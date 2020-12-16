import utils

# fetch data
data = utils.congruous_groups('input_files/aoc_06.txt')

### START SOLUTION BODY ###

# find the sum of the 'yes' answers from each group
found, answer = False, 0
for item in data:
    item = item.replace(' ', '')
    item = [ch for ch in item]
    answer += len(set(item))
found = True

### END SOLUTION BODY ###

# output result
utils.one_val_out(found, answer)

