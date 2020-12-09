import utils

# fetch data
data = utils.lines_to_ints('input_files/aoc_09.txt')

### START SOLUTION BODY ###

def two_sum_next(nums, target):
    for n in nums:
        if target - n in nums:
            return True
    return False

# find the first number that is not the sum of 2 of the 25 numbers before it
found, answer = False, 0
for idx in range(len(data) - 25):
    if not two_sum_next(data[idx : idx + 25], data[idx + 25]):
        answer = data[idx + 25]
        break
found = True

### END SOLUTION BODY ###

# output result
utils.one_val_out(found, answer)

