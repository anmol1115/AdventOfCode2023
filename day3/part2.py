from helper import *
sum = 0

with open("case1.txt", 'r') as f:
    lines = f.readlines()

    for row, line in enumerate(lines):
        starIndices = getStars(line)

        for col in starIndices:
            neighbors = [
                [row-1, col-1], [row-1, col], [row-1, col+1],
                [row, col-1], [row, col], [row, col+1],
                [row+1, col-1], [row+1, col], [row+1, col+1]
            ]

            numbers = set()
            for nr, nc in neighbors:
                if lines[nr][nc].isdigit():
                    number = getNumber(nc, lines[nr], nr)
                    numbers.add(number)

            if len(numbers) == 2:
                numbers = list(numbers)
                sum += numbers[0][0] * numbers[1][0]


print(sum)