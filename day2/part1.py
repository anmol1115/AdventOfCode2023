from getData import fetch

threshold = {'red': 12, 'green': 13, 'blue': 14}
sum = 0

games = fetch('case1.txt')
for idx, game in games.items():
    valid = True

    for color, balls in game.items():
        for ball in balls:
            if ball > threshold[color]:
                valid = False
                break

    if valid: sum += idx

print(sum)