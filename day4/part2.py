from helper import *

with open("case1.txt", 'r') as f:
    lines = f.readlines()

    cache = [1] * len(lines)
    for idx, line in enumerate(lines):
        line = line.strip()

        wNums, Nums = getNumbers(line)
        diff = wNums - Nums

        count = len(wNums) - len(diff)
        for i in range(1, count+1):
            cache[idx+i] += cache[idx]

    print(sum(cache))