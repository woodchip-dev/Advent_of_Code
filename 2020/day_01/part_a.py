import utils

# fetch data
data = utils.line_to_list('input_files/aoc_01.txt')

### START SOLUTION BODY ###

# find xy given x + y == 2020
found, answer = False, None
for item in data:
	val = str(2020 - int(item))
	if val in data:
		answer = int(item) * int(val)
		found = True
		break

### END SOLUTION BODY ###

# output result
utils.one_val_out(found, answer)

