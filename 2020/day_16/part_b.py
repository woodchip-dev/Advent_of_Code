import utils

# fetch data
data = utils.different_groups('input_files/aoc_16.txt')

### START SOLUTION BODY ###

# find the product of the 6 departure values on my ticket
found, answer = False, 1
fields = {item.split(': ')[0]: [(int(num.split('-')[0]), int(num.split('-')[1])) for num in item.split(': ')[1].split(' or ')] for item in data[0]}
my_ticket = [int(num) for num in data[1][1].split(',')]
tickets = [[int(num) for num in item.split(',')] for item in data[2][1:]]
indices = []
for ticket in tickets:
    for val in ticket:
        good = False
        for field in fields:
            if (fields[field][0][0] <= val and val <= fields[field][0][1]) or (fields[field][1][0] <= val and val <= fields[field][1][1]):
                good = True
        if not good:
            indices.append(tickets.index(ticket))
for idx in reversed(indices):
    del tickets[idx]
tickets.append(my_ticket)
aggr = {idx: [ticket[idx] for ticket in tickets] for idx in range(len(tickets[0]))}
record, candidates = {}, {}
for field in fields:
    if not field in list(record.keys()):
        candidates[field] = []
    for agg in aggr:
        temp = agg
        if all(not val < fields[field][0][0] and not (fields[field][0][1] < val and val < fields[field][1][0]) and not fields[field][1][1] < val for val in aggr[agg]):
            candidates[field].append(agg)
while not len(record) == len(my_ticket):
    for candid in candidates:
        if len(candidates[candid]) == 1:
            record[candid] = candidates[candid][0]
            for rekt in candidates:
                if record[candid] in candidates[rekt]:
                    candidates[rekt].remove(record[candid])
for rec in record:
    if rec.startswith('departure'):
        answer *= my_ticket[record[rec]]
found = True

### END SOLUTION BODY ###

# output result
utils.one_val_out(found, answer)

