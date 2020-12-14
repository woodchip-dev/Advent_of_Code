import utils
from sympy.ntheory.modular import crt

# fetch data
data = utils.line_to_list('input_files/aoc_13.txt')

### START SOLUTION BODY ###

# find the earliest timestamp such that all of the bus IDs depart at offsets matching their positions in the list
found, answer = False, None
time_table = data[1].split(',')
buses = [int(bus) for bus in time_table if not bus == 'x']
index = [i for i in range(len(time_table)) if not time_table[i] == 'x']
crt_ans = crt(buses, index)
answer = crt_ans[1] - crt_ans[0]
found = True

### END SOLUTION BODY ###

# output result
utils.one_val_out(found, answer)

