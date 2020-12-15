import utils

# fetch data
data = utils.commas_to_list('input_files/aoc_15.txt')

### START SOLUTION BODY ###

# find the 2020th number spoken given the rules
found, answer = False, None
for idx in range(len(data), 2020):
    if data.count(data[-1]) == 1:
        data.append(str(0))
    elif data.count(data[-1]) > 1:
        indices = [i for i, num in enumerate(data) if num == data[-1]]
        if not indices[-1] - indices[-2] == 1:
            data.append(str(indices[-1] - indices[-2]))
        else:
            data.append(str(1))
answer = data[-1]
found = True

### END SOLUTION BODY ###

# output result
utils.one_val_out(found, answer)

