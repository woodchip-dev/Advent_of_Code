import utils

# fetch data
data = utils.line_to_list('input_files/aoc_13.txt')

### START SOLUTION BODY ###

# find the earliest timestamp such that all of the bus IDs depart at offsets matching their positions in the list
found, answer = False, None
time_table = data[1].split(',')
buses = [int(bus) for bus in time_table if not bus == 'x']
index = [i for i in range(len(time_table)) if not time_table[i] == 'x']
schedules = list(map(lambda i, b : (i, b), index, buses))
idx, time = 0, 0
clocked = []
while idx < len(schedules):
    offset = 1
    print(time)
    if time % schedules[idx][1] == 0:
        clocked.append(time)
        idx +=1
        if idx < len(schedules):
            offset = schedules[idx][0] - schedules[idx - 1][0]
    else:
        idx = 0
        clocked = []
    time += offset
answer = clocked[0]
found = True

### END SOLUTION BODY ###

# output result
utils.one_val_out(found, answer)

