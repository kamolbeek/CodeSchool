import time
import random
import asciichartpy as acp

weapons = ['M16A4', 'M416', 'SCAR-L', 'G36C', 'QBZ95', 'K2', 'AUG A3', 'FAMAS',
           'AKM', 'Beryl M762', 'Mk47 Mutant', 'Groza', 'ACE32', 'Tova',
           'Granata', 'Kar98k', 'M24', 'AWM']

players = [f'Player {player_number}' for player_number in range(1,9)]
red = {player: [0, [], 'Red', 0] for player in players if player[len(player)-1]<=str(4)}
blue = {player: [0, [], 'Blue', 0] for player in players if player[len(player)-1]>=str(5)}

print('\nGAME Players: 8\n')

while True:
    if sum([red[c1][0] for c1 in red]) == 40:
        mvp = max([red[m][0] for m in red])
        print('\nGAME FINISHED\n\nRED COMMAND WIN')
        for pl in red:
            print(f'{red[pl][2]} {pl}: {red[pl][0]} {red[pl][3]}')
        print('')
        for bl in blue:
            print(f'{blue[bl][2]} {bl}: {blue[bl][0]} {blue[bl][3]}')
        ind = [red[m][0] for m in red].index(mvp)
        s = list(red.keys())
        print(f'MVP PLAYER {s[ind]}: {mvp} kills')
        print(f'\nDrawing graphics of statistics of mvp player...\n\n')
        time.sleep(3)
        x = [random.randint(1,mvp+1) for i in range(40)]
        print(acp.plot(x))
        break
    elif sum([blue[c2][0] for c2 in blue]) == 40:
        mvp = max([blue[m][0] for m in blue])
        print('\nGAME FINISHED\n\nBLUE COMMAND WIN')
        for bl in blue:
            print(f'{blue[bl][2]} {bl}: {blue[bl][0]} {blue[bl][3]}')
        print('')
        for pl in red:
            print(f'{red[pl][2]} {pl}: {red[pl][0]} {red[pl][3]}')
        ind = [blue[m][0] for m in blue].index(mvp)
        s = list(blue.keys())
        print(f'MVP PLAYER {s[ind]}: {mvp} kills')
        print(f'\nDrawing graphics of statistics of mvp player...\n\n')
        time.sleep(3)
        x = [random.randint(1,mvp+1) for i in range(40)]
        print(acp.plot(x))
        break
    else:
        r_player = random.choice(players)
        if r_player[len(r_player)-1]<=str(4):
            k_player = random.choice(players)
            if k_player == r_player or (k_player in red):
                continue
            else:
                weapon = random.choice(weapons)
                red[r_player][0] += 1
                red[r_player][1].append(k_player)
                blue[k_player][3] += 1
                total_count = sum([red[c1][0] for c1 in red])
                print(f'🔴{r_player} kills 🟢{k_player} 🔫Weapon: {weapon} 👥Total kills: {total_count}')
                time.sleep(0.1)
        elif r_player[len(r_player)-1]>=str(5):
            k_player = random.choice(players)
            if k_player == r_player or (k_player in blue):
                continue
            else:
                weapon = random.choice(weapons)
                blue[r_player][0] += 1
                blue[r_player][1].append(k_player)
                red[k_player][3] += 1
                total_count = sum([red[c1][0] for c1 in red])
                print(f'🟢{r_player} kills 🔴{k_player} 🔫Weapon: {weapon} 👥Total kills: {total_count}')
                time.sleep(0.1)