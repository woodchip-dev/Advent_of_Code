import utils

# fetch data
data = utils.line_to_list('input_files/aoc_23.txt')

### START SOLUTION BODY ###

def wrap(val, size):
    return (val + 1) % size

# find the order of the cups after cup 1 after 100 moves
found, answer = False, None
cups = [int(ch) for ch in data[0]]
curr = cups[0]
size = len(cups)
for num in range(100):
    temp = []
    idx = wrap(cups.index(curr), size)
    for it in range(3):
        temp.append(cups[idx])
        idx = wrap(idx, size)
    for item in temp:
        cups.remove(item)
    dest = curr - 1
    while dest not in cups:
        dest -= 1
        if dest < min(cups):
            dest = max(cups)
    ins = wrap(cups.index(dest), size)
    cups = cups[:ins] + temp + cups[ins:]
    curr = cups[wrap(cups.index(curr), size)]
circle = ''.join([str(ch) for ch in cups])
loc = circle.index('1')
answer = circle[loc + 1:] + circle[:loc]
found = True

### END SOLUTION BODY ###

# output result
utils.one_val_out(found, answer)

