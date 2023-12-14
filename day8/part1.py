from helper import *

directions, nodeMap = readData("case1.txt")
idx = 0
steps = 0
start = "AAA"

while True:
    steps += 1
    if nodeMap[start][directions[idx]] == 'ZZZ':
        break

    start = nodeMap[start][directions[idx]]
    idx = (idx + 1) % len(directions)

print(steps)