import utils, re

# fetch data
data = utils.line_to_list('input_files/aoc_07.txt')

### START SOLUTION BODY ###

def find_bags(sacks, bags, color):
    if color not in sacks:
        sacks.add(color)
        for bag in bags:
            if color in bags[bag]:
                find_bags(sacks, bags, bag)
    return len(sacks) - 1

# find how many bag colors can (eventually) contain at least one shiny gold bag
found, answer = False, 0
bags = {}
for item in data:
    item = item.split(' bags contain ')
    bags[item[0]] = [re.sub('[0-9]{1,2} | bag[.s]*', '', bag) for bag in item[1].split(', ')]
answer = find_bags(set(), bags, 'shiny gold')
found = True

### END SOLUTION BODY ###

# output result
utils.one_val_out(found, answer)

