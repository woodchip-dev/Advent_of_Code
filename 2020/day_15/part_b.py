import utils

# fetch data
data = utils.commas_to_list('input_files/aoc_15.txt')

### START SOLUTION BODY ###

# find the 30000000th number spoken given the rules
found, answer = False, None
record = {int(last): i + 1 for i, last in enumerate(data)}
last = int(data[-1])
for idx in range(len(data), 30000000):
    curr = idx - record[last] if last in record else 0
    record[last] = idx
    last = curr
answer = curr
found = True

### END SOLUTION BODY ###

# output result
utils.one_val_out(found, answer)

