import utils, math

# fetch data
data = utils.line_to_list('input_files/aoc_13.txt')

### START SOLUTION BODY ###

# find the product of the bus ID I'll take and the minutes I need to wait for it
found, answer = False, 0
buses = [int(bus) for bus in data[1].split(',') if not bus == 'x']
departures = [(bus, bus * math.ceil(int(data[0]) / bus)) for bus in buses]
departure = min(departures, key = lambda t: t[1])
answer = departure[0] * (departure[1] - int(data[0]))
found = True

### END SOLUTION BODY ###

# output result
utils.one_val_out(found, answer)

