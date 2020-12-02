import utils

# fetch data
data = utils.line_to_list('input_files/aoc_01.txt')

### START SOLUTION BODY ###

# find xyz given x + y + z == 2020
found, answer = False, None
for item_a in data:
	for item_b in data:
		val = str(2020 - int(item_a) - int(item_b))
		if val in data:
			answer = int(item_a) * int(item_b) * int(val)
			found = True
			break
	if found:
		break

### END SOLUTION BODY ###

# output result
utils.one_val_out(found, answer)

