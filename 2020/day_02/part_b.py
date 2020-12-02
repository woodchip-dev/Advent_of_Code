import utils

# fetch data
data = utils.line_to_list('input_files/aoc_02.txt')

### START SOLUTION BODY ###

# find how many passwords are valid according to their respective policy
found, answer = False, 0
for item in data:
    range_vals, ch, pwd = item.split(' ')
    low, high = range_vals.split('-')
    if (pwd[int(low) - 1] == ch[:-1] and not pwd[int(high) - 1] == ch[:-1]) or (not pwd[int(low) - 1] == ch[:-1] and pwd[int(high) - 1] == ch[:-1]):
        answer = answer + 1
found = True

### END SOLUTION BODY ###

# output result
utils.one_val_out(found, answer)

