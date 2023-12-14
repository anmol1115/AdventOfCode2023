from getData import fetch

games = fetch("case1.txt")
sum = 0

for game in games.values():
    prod = 1

    for balls in game.values():
        prod *= max(balls)

    sum += prod

print(sum)