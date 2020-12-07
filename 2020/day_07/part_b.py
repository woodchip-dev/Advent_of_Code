import utils, re

# fetch data
data = utils.line_to_list('input_files/aoc_07.txt')

### START SOLUTION BODY ###

def find_bags(bags, color, count):
    for bag in bags[color]:
        if not bag == 'no other':
            count += int(bag[0]) + int(bag[0]) * find_bags(bags, bag[2:], 0)
        else:
            return 0
    return count

# find how many bags I must have in my shiny gold bag
found, answer = False, 0
bags = {}
for item in data:
    item = item.split(' bags contain ')
    bags[item[0]] = [re.sub(' bag[.s]*', '', bag) for bag in item[1].split(', ')]
answer = find_bags(bags, 'shiny gold', 0)
found = True

### END SOLUTION BODY ###

# output result
utils.one_val_out(found, answer)

