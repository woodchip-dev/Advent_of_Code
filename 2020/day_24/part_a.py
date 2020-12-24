import utils, re
from collections import defaultdict

# fetch data
data = utils.line_to_list('input_files/aoc_24.txt')

### START SOLUTION BODY ###

# find how many tiles are left with the black side up
found, answer = False, 0
record = [{'se': item.count('se'), 'sw': item.count('sw'), 'ne': item.count('ne'), 'nw': item.count('nw'), 'e': len(re.findall(r'(?<![ns])e', item)), 'w': len(re.findall(r'(?<![ns])w', item))} for item in data]
for item in record:
    while 1:
        temp = {key: item[key] for key in item}
        if item['se'] >= item['ne']:
            item['e'] += item['ne']
            item['se'] -= item['ne']
            item['ne'] -= item['ne']
        else:
            item['e'] += item['se']
            item['ne'] -= item['se']
            item['se'] -= item['se']
        if item['sw'] >= item['nw']:
            item['w'] += item['nw']
            item['sw'] -= item['nw']
            item['nw'] -= item['nw']
        else:
            item['w'] += item['sw']
            item['nw'] -= item['sw']
            item['sw'] -= item['sw']
        if item['se'] >= item['w']:
            item['sw'] += item['w']
            item['se'] -= item['w']
            item['w'] -= item['w']
        else:
            item['sw'] += item['se']
            item['w'] -= item['se']
            item['se'] -= item['se']
        if item['sw'] >= item['e']:
            item['se'] += item['e']
            item['sw'] -= item['e']
            item['e'] -= item['e']
        else:
            item['se'] += item['sw']
            item['e'] -= item['sw']
            item['sw'] -= item['sw']
        if item['ne'] >= item['w']:
            item['nw'] += item['w']
            item['ne'] -= item['w']
            item['w'] -= item['w']
        else:
            item['nw'] += item['ne']
            item['w'] -= item['ne']
            item['ne'] -= item['ne']
        if item['nw'] >= item['e']:
            item['ne'] += item['e']
            item['nw'] -= item['e']
            item['e'] -= item['e']
        else:
            item['ne'] += item['nw']
            item['e'] -= item['nw']
            item['nw'] -= item['nw']
        if item['se'] >= item['nw']:
            item['se'] -= item['nw']
            item['nw'] -= item['nw']
        else:
            item['nw'] -= item['se']
            item['se'] -= item['se']
        if item['sw'] >= item['ne']:
            item['sw'] -= item['ne']
            item['ne'] -= item['ne']
        else:
            item['ne'] -= item['sw']
            item['sw'] -= item['sw']
        if item['e'] >= item['w']:
            item['e'] -= item['w']
            item['w'] -= item['w']
        else:
            item['w'] -= item['e']
            item['e'] -= item['e']
        if item == temp:
            break
tiles = []
for item in record:
    if not item in tiles:
        tiles.append(item)
        if record.count(item) % 2 == 1:
            answer += 1
found = True

### END SOLUTION BODY ###

# output result
utils.one_val_out(found, answer)

