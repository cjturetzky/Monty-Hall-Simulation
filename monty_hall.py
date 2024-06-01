import numpy as np
import matplotlib.pyplot as plt

total_games = 100000


# initial switching strategy - more literal, more expensive
# def switch_strategy(selected, winning):
#     shown = -1
#     for i in range(3):
#         if(i != winning and i != selected and shown == -1):
#             shown = i
#             # print('Shown door: %i' % shown)
#     for i in range(3):
#         if(i != select and i != shown):
#             final_select = i
#     return final_select

def switch_strategy(selected, winning):
    # If you were wrong on your first guess, switching means you win
    # Otherwise, you lose
    return selected != winning


def stick_strategy(selected, winning):
    # If you were right on your first guess, sticking means you in
    # Otherwise, you lose
    return selected == winning


games = 0
switch_wins = 0
while games < total_games:
    winning_door = np.random.randint(0, 3)
    select = np.random.randint(0, 3)

    if switch_strategy(select, winning_door):
        # print("WINNER!")
        switch_wins += 1
    games += 1

# print('After %i games, switching won %i times, for a percentage of %s' % (
#     total_games, switch_wins, format(switch_wins / total_games, ".0%")))

games = 0
stick_wins = 0
while games < total_games:
    winning_door = np.random.randint(0, 3)
    select = np.random.randint(0, 3)

    if stick_strategy(select, winning_door):
        # print("WINNER!")
        stick_wins += 1
    games += 1

# print('After %i games, sticking won %i times, for a percentage of %s' % (
    # total_games, stick_wins, format(stick_wins / total_games, ".0%")))

labels = 'Wins', 'Losses'
switch_sizes = [switch_wins, total_games - switch_wins]
stick_sizes = [stick_wins, total_games - stick_wins]

fig, axlist = plt.subplots(ncols=2)
fig.suptitle('Monty Hall Simulation with %i trials' % total_games)
axlist[0].pie(switch_sizes, labels=labels, colors=['springgreen', 'crimson'], autopct='%1.1f%%', explode=[0.1, 0.1],
              shadow=True)
axlist[0].set_title('Switch win/loss chart\nWins: %i' % switch_wins)

axlist[1].pie(stick_sizes, labels=labels, colors=['springgreen', 'crimson'], autopct='%1.1f%%', explode=[0.1, 0.1],
              shadow=True)
axlist[1].set_title('Stick win/loss chart\nWins: %i' % stick_wins)

plt.show()
