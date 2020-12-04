import utils

# fetch data
data = utils.separated_by_blanks('input_files/aoc_04.txt')

### START SOLUTION BODY ###

# find the number of valid passports;
# passports are valid if they have all required fields
found, answer = False, 0
for item in data:
    if 'byr' in item and 'iyr' in item and 'eyr' in item and 'hgt' in item and 'hcl' in item and 'ecl' in item and 'pid' in item:
        answer += 1
found = True

### END SOLUTION BODY ###

# output result
utils.one_val_out(found, answer)

