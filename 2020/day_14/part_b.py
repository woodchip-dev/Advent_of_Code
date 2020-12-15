import utils

# fetch data
data = utils.line_to_list('input_files/aoc_14.txt')

### START SOLUTION BODY ###

def enum_bins(pattern, storage):
    if not 'X' in pattern:
        storage.append(pattern)
    else:
        enum_bins(pattern.replace('X', '0', 1), storage)
        enum_bins(pattern.replace('X', '1', 1), storage)
    return storage

# find the sum of the remaining memory values
found, answer = False, 0
rules, temp = {}, []
for idx in range(len(data)):
    if data[idx][:4] == 'mask':
        temp = []
        mask = data[idx].split(' = ')[1]
    elif data[idx][:3] == 'mem':
        mem = data[idx].split(' = ')
        temp.append((bin(int(mem[0][4:-1]))[2:].zfill(len(mask)), int(mem[1])))
        if (idx + 1 < len(data) and data[idx + 1][:4] == 'mask') or idx == len(data) - 1:
            rules[mask] = temp
addrs = []
for rule in rules:
    addr = [ch for ch in bin(0)[2:].zfill(len(rule))]
    for item in rules[rule]:
        for idx in range(len(rule)):
            if rule[idx] == '0':
                addr[idx] = item[0][idx]
            elif rule[idx] == '1':
                addr[idx] = '1'
            elif rule[idx] == 'X':
                addr[idx] = 'X'
        addrs.append((''.join(addr), item[1]))
enum_addrs = {}
for addr in addrs:
    addr = [(enum, addr[1]) for enum in enum_bins(addr[0], [])]
    for item in addr:
        enum_addrs[item[0]] = item[1]
for enum in enum_addrs:
    answer += enum_addrs[enum]
found = True

### END SOLUTION BODY ###

# output result
utils.one_val_out(found, answer)

