import utils

# fetch data
data = utils.separated_by_blanks('input_files/aoc_06.txt')

### START SOLUTION BODY ###

# find the sum of the unanimous 'yes' answers from each group
found, answer = False, 0
for item in data:
    count = len(item.split(' '))
    item = item.replace(' ', '')
    item = [ch for ch in item]
    for ch in set(item):
        if item.count(ch) == count:
            answer += 1
found = True

### END SOLUTION BODY ###

# output result
utils.one_val_out(found, answer)

