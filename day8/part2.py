from helper import *

directions, nodeMap = readData("case1.txt")

start = [node for node in nodeMap.keys() if node[-1] == 'A']
steps = []

for startingNode in start:
    idx = 0
    step = 0
    nextNode = startingNode
    flag = True
    while flag:
        nextNode = nodeMap[nextNode][directions[idx]]
        step += 1
        if nextNode[-1] == 'Z':
            flag = False
        idx = (idx + 1) % len(directions)

    steps.append(step)

print(steps)
print(getLCM(steps))