sum = 0
from helper import *

with open("case1.txt", 'r') as f:
    lines = f.readlines()

    for row, line in enumerate(lines):
        line = line.strip()
        numbers = getNums(line)

        for number, start, end in numbers:
            rows = [max(row-1, 0), row, min(row+1, len(lines)-1)]
            col_start = max(start-1,0)
            col_end = min(end+2, len(line))

            check = False
            check = checkSymbol(lines[rows[0]][col_start:col_end]) or \
                    checkSymbol(lines[rows[1]][col_start:col_end]) or \
                    checkSymbol(lines[rows[2]][col_start:col_end])

            if check:
                sum += number

print(sum)