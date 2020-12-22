import utils

# fetch data
data = utils.different_groups('input_files/aoc_22.txt')

### START SOLUTION BODY ###

def sub_game(player1, player2, layer):
    prev, autowin = [], False
    while len(player1) > 0 and len(player2) > 0:
        p1_win, p2_win = False, False
        if (player1, player2) in prev:
            p1_win, autowin = True, True
        elif not (player1, player2) in prev:
            prev.append(([tmp1 for tmp1 in player1], [tmp2 for tmp2 in player2]))
        if player1[0] <= len(player1[1:]) and player2[0] <= len(player2[1:]) and not p1_win:
            if max(player1[1 : player1[0] + 1]) > max(player2[1 : player2[0] + 1]):
                p1_win = True
            else:
                layer += 1
                p1_temp, p2_temp = sub_game(player1[1 : player1[0] + 1], player2[1 : player2[0] + 1], layer)
                layer -= 1
                if p1_temp == [] and not p2_temp == []:
                    p2_win = True
                else:
                    p1_win = True
        if not p2_win and (player1[0] > player2[0] or p1_win or autowin):
            player1.append(player1[0])
            player1.append(player2[0])
            del player1[0]
            del player2[0]
            p1_win = False
            if autowin:
                autowin = False
                return player1, player2
        else:
            player2.append(player2[0])
            player2.append(player1[0])
            del player1[0]
            del player2[0]
            p2_win = False
    return player1, player2

# find the score of the winning player
found, answer = False, 0
player1, player2 = sub_game([int(p1) for p1 in data[0][1:]], [int(p2) for p2 in data[1][1:]], 0)
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

