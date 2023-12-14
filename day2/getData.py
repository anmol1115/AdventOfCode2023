def fetch(path):
    games = {}
    with open(path, 'r') as f:
        lines = f.readlines()

        for line in lines:
            game_num, data = line.split(':')
            game_num = int(game_num.split(' ')[1].strip())

            games[game_num] = {'red': [], 'blue': [], 'green': []}
            for balls in data.split(';'):
                for ball in balls.split(','):
                    num, color = ball.strip().split(' ')
                    games[game_num][color].append(int(num))

    return games

if __name__ == "__main__":
    print(fetch("test-case1.txt"))