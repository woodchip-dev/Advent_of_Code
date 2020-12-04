import utils, re, json

# fetch data
data = utils.separated_by_blanks('input_files/aoc_04.txt')

### START SOLUTION BODY ###

# task overview comment
found, answer = False, 0
# add code here
passports = []
for item in data:
    temp = {}
    if 'byr' in item and 'iyr' in item and 'eyr' in item and 'hgt' in item and 'hcl' in item and 'ecl' in item and 'pid' in item:
        item = item.replace(' ','","')
        item = item.replace(':','":"')
        item = '{"' + item + '"}'
        passports.append(json.loads(item))

ecls = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
for passport in passports:
    if len(passport['byr']) == 4 and int(passport['byr']) >= 1920 and int(passport['byr']) <= 2002:
        if len(passport['iyr']) == 4 and int(passport['iyr']) >= 2010 and int(passport['iyr']) <= 2020:
            if len(passport['eyr']) == 4 and int(passport['eyr']) >= 2020 and int(passport['eyr']) <= 2030:
                hgt, unit = passport['hgt'][:-2], passport['hgt'][-2:]
                if (unit == 'cm' and int(hgt) >= 150 and int(hgt) <= 193) or (unit == 'in' and int(hgt) >= 59 and int(hgt) <= 76):
                    if re.match('^#[0-9a-f]{6}$', passport['hcl']):
                        if passport['ecl'] in ecls:
                            if len(passport['pid']) == 9:
                                answer += 1
found = True

### END SOLUTION BODY ###

# output result
utils.one_val_out(found, answer)

