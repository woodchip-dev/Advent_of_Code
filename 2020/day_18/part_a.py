import utils, re

# fetch data
data = utils.line_to_list('input_files/aoc_18.txt')

### START SOLUTION BODY ###

def calculate(expr):
    while 1:
        parens = re.findall('\\([0-9\\+\\*]+\\)', expr)
        if not parens == []:
            for par in parens:
                new_val = calculate(par[1:-1])
                expr = expr.replace(par, str(new_val))
        else:
            break
    temp = 0
    plus, mult = False, False
    expr = expr.replace('*', ' * ')
    expr = expr.replace('+', ' + ')
    expr = expr.split(' ')
    for ch in expr:
        if ch == '+':
            plus = True
        elif ch == '*':
            mult = True
        elif ch.isdigit():
            if not plus and not mult:
                temp = int(ch)
            elif plus and not mult:
                temp += int(ch)
                plus = False
            elif not plus and mult:
                temp *= int(ch)
                mult = False
    return temp

# find the sum of the results of each equation given the precedent rules
found, answer = False, 0
data = [item.replace(' ', '') for item in data]
for item in data:
    answer += calculate(item)
found = True

### END SOLUTION BODY ###

# output result
utils.one_val_out(found, answer)

