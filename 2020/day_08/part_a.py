import utils

# fetch data
data = utils.line_to_list('input_files/aoc_08.txt')

### START SOLUTION BODY ###

# find the value in the accumulator right before an instruction is called a second time
found, answer = False, None
ops = []
for item in data:
    ins, mag = item.split(' ')
    ops.append([ins, int(mag), False])
idx, acc = 0, 0
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
found = True

### END SOLUTION BODY ###

# output result
utils.one_val_out(found, answer)

