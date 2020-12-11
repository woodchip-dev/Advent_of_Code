import utils

# fetch data
data = utils.lines_to_ints('input_files/aoc_10.txt')

def count_arrangements(data, curr, storage):
    count = 0
    if curr == max(data):
        return 1
    for idx in range(curr + 1, curr + 4):
        if idx in data:
            if not idx in storage:
                storage[idx] = count_arrangements(data, idx, storage)
            count += storage[idx]
    return count

### START SOLUTION BODY ###

# find the total number of distinct ways to arrange the adapters
found, answer = False, 0
data.sort()
answer = count_arrangements(data, 0, {})
found = True

### END SOLUTION BODY ###

# output result
utils.one_val_out(found, answer)

