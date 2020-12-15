import utils

# fetch data
data = utils.line_to_list('input_files/aoc_14.txt')

### START SOLUTION BODY ###

# find the sum of the remaining memory values
found, answer = False, 0
rules, temp = {}, []
for idx in range(len(data)):
    if data[idx][:4] == 'mask':
        temp = []
        mask = data[idx].split(' = ')[1]
    elif data[idx][:3] == 'mem':
        mem = data[idx].split(' = ')
        temp.append((mem[0][4:-1], bin(int(mem[1]))[2:].zfill(len(mask))))
        if (idx + 1 < len(data) and data[idx + 1][:4] == 'mask') or idx == len(data) - 1:
            rules[mask] = temp
vals = {}
for rule in rules:
    val = [ch for ch in bin(0)[2:].zfill(len(rule))]
    for item in rules[rule]:
        for idx in range(len(rule)):
            if rule[idx] == '0':
                val[idx] = '0'
            elif rule[idx] == '1':
                val[idx] = '1'
            elif rule[idx] == 'X':
                val[idx] = item[1][idx]
        vals[item[0]] = ''.join(val)
for val in vals:
    answer += int(vals[val], 2)
found = True

### END SOLUTION BODY ###

# output result
utils.one_val_out(found, answer)

