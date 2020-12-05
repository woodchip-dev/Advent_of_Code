import utils, math

# fetch data
data = utils.line_to_list('input_files/aoc_05.txt')

### START SOLUTION BODY ###

def cut(deck, top):
    if top:
        deck['high'] -=  math.ceil((deck['high'] - deck['low']) / 2)
    else:
        deck['low'] +=  math.ceil((deck['high'] - deck['low']) / 2)
    return deck

# find the highest seat ID on a boarding pass
found, answer = False, None
seats = []
for item in data:
    rows = {'low': 0, 'high': 127}
    cols = {'low': 0, 'high': 7}
    for ch in item[:7]:
        if ch == 'F':
            rows = cut(rows, True)
        else:
            rows = cut(rows, False)
    for ch in item[-3:]:
        if ch == 'L':
            cols = cut(cols, True)
        else:
            cols = cut(cols, False)
    seats.append((rows['low'] * 8 + cols['low']))
answer = max(seats)
found = True

### END SOLUTION BODY ###

# output result
utils.one_val_out(found, answer)

