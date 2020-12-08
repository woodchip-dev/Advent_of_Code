import utils

# fetch data
data = utils.line_to_list('input_files/aoc_08.txt')

### START SOLUTION BODY ###

def process_data(data):
    ops, fops, count = [], [], 0
    for item in data:
        ins, mag = item.split(' ')
        ops.append([ins, int(mag), False])
        if not ins == 'acc':
            fops.append(count)
        count += 1
    return ops, fops

# find the value in the accumulator when it terminates normally
found, answer = False, None
ops, fops =  process_data(data)
for fop in fops:
    ops, ignore = process_data(data)
    idx, acc = 0, 0
    if ops[fop][0] == 'jmp':
        ops[fop][0] = 'nop'
    elif ops[fop][0] == 'nop':
        ops[fop][0] = 'jmp'
    while idx < len(ops):
        if ops[idx][2]:
            answer = acc
            break
        if ops[idx][0] == 'acc':
            ops[idx][2] = True
            acc += ops[idx][1]
        elif ops[idx][0] == 'jmp':
            ops[idx][2] = True
            idx += ops[idx][1] - 1
        elif ops[idx][0] == 'nop':
            ops[idx][2] = True
        idx += 1
    if idx >= len(ops):
        answer = acc
        break
found = True

### END SOLUTION BODY ###

# output result
utils.one_val_out(found, answer)

