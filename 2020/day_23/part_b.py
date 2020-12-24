import utils

# fetch data
data = utils.line_to_list('input_files/aoc_23.txt')

### START SOLUTION BODY ###

# find the product of the two cups CW from 1 after 10.000.000 moves
found, answer = False, None
cups = [int(ch) for ch in data[0]]
more = [val for val in range(max(cups) + 1, 1_000_001)]
cups += more
record = [0] * 1_000_001
for idx in range(len(cups)):
    record[cups[idx]] = cups[0] if idx == len(cups) - 1 else cups[idx + 1]
curr = cups[0]
for num in range(10_000_001):
    a = record[curr]
    b = record[a]
    c = record[b]
    record[curr] = record[c]
    dest = curr - 1
    while dest in [a, b, c] or dest < 1:
        dest -= 1
        if dest < 1:
            dest = len(cups)
    record[c] = record[dest]
    record[dest] = a
    curr = record[curr]
answer = record[1] * record[record[1]]
found = True

### END SOLUTION BODY ###

# output result
utils.one_val_out(found, answer)

