import utils

# fetch data
data = utils.different_groups('input_files/aoc_16.txt')

### START SOLUTION BODY ###

# find my ticket scanning error rate
found, answer = False, 0
fields = {item.split(': ')[0]: [(int(num.split('-')[0]), int(num.split('-')[1])) for num in item.split(': ')[1].split(' or ')] for item in data[0]}
tickets = [[int(num) for num in item.split(',')] for item in data[2][1:]]
for ticket in tickets:
    for val in ticket:
        good = False
        for field in fields:
            if (fields[field][0][0] <= val and val <= fields[field][0][1]) or (fields[field][1][0] <= val and val <= fields[field][1][1]):
                good = True
        if not good:
            answer += val
found = True

### END SOLUTION BODY ###

# output result
utils.one_val_out(found, answer)

