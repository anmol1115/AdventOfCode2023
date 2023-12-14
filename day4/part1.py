from helper import *

sum = 0
with open("test-case1.txt", 'r') as f:
    lines = f.readlines()

    for line in lines:
        line = line.strip()

        wNums, Nums = getNumbers(line)
        diff = wNums - Nums

        count = len(wNums) - len(diff)
        print(count)
        if count>0:
            sum += 2 ** (count - 1)

print(sum)