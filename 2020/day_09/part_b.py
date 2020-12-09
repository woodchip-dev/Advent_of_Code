import utils

# fetch data
data = utils.lines_to_ints('input_files/aoc_09.txt')

### START SOLUTION BODY ###

def two_sum_next(nums, target):
    for n in nums:
        if target - n in nums:
            return True
    return False

# find the value of the encryption weakness
found, answer = False, 0
for idx in range(len(data) - 25):
    if not two_sum_next(data[idx : idx + 25], data[idx + 25]):
        target = data[idx + 25]
        break
s, e = 0, 1
while e < len(data) - 1:
    if sum(data[s:e]) < target:
        e += 1
    elif target < sum(data[s:e]):
        s += 1
    else:
        break
answer = min(data[s:e]) + max(data[s:e])
found = True

### END SOLUTION BODY ###

# output result
utils.one_val_out(found, answer)

