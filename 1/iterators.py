from itertools import count, cycle


# for i in count(1, 1):
#     print(i)






players = [
    'Вася',
    'Петя',
    'Ваня'
]

counter = [
    'чики',
    'брики',
    'пальчик',
    'выкинь',
]

iter_players = cycle(players)
# iter_players = iter(players)
current_player = players[0]
for _ in counter:
    current_player = next(iter_players)

print(current_player)
print(players[len(counter) % len(players) - 1])