import utils

# fetch data
data = utils.different_groups('input_files/aoc_22.txt')

### START SOLUTION BODY ###

# find the score of the winning player
found, answer = False, 0
player1, player2 = [int(p1) for p1 in data[0][1:]], [int(p2) for p2 in data[1][1:]]
while len(player1) > 0 and len(player2) > 0:
    if player1[0] > player2[0]:
        player1.append(player1[0])
        player1.append(player2[0])
        del player1[0]
        del player2[0]
    else:
        player2.append(player2[0])
        player2.append(player1[0])
        del player1[0]
        del player2[0]
winner = None
if player1 == []:
    winner = player2
else:
    winner = player1
for item in winner:
    answer += item * (len(winner) - winner.index(item))
found = True

### END SOLUTION BODY ###

# output result
utils.one_val_out(found, answer)

