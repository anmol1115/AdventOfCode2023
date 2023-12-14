from helper import *
from math import ceil

data = readData("case1.txt")
StartLoc = findStart(data)

pathStart, pathEnd = findPathStart(StartLoc, data)

count = 1
startNode, nextNode = StartLoc, pathStart
while nextNode != pathEnd:
    if data[nextNode[0]][nextNode[1]] == '|':
        if diff(nextNode, startNode) == (-1, 0):
            tempNode = (nextNode[0]-1, nextNode[1])
        else:
            tempNode = (nextNode[0]+1, nextNode[1])
    if data[nextNode[0]][nextNode[1]] == '-':
        if diff(nextNode, startNode) == (0, 1):
            tempNode = (nextNode[0], nextNode[1]+1)
        else:
            tempNode = (nextNode[0], nextNode[1]-1)
    if data[nextNode[0]][nextNode[1]] == 'L':
        if diff(nextNode, startNode) == (1, 0):
            tempNode = (nextNode[0], nextNode[1]+1)
        else:
            tempNode = (nextNode[0]-1, nextNode[1])
    if data[nextNode[0]][nextNode[1]] == 'J':
        if diff(nextNode, startNode) == (0, 1):
            tempNode = (nextNode[0]-1, nextNode[1])
        else:
            tempNode = (nextNode[0], nextNode[1]-1)
    if data[nextNode[0]][nextNode[1]] == '7':
        if diff(nextNode, startNode) == (0, 1):
            tempNode = (nextNode[0]+1, nextNode[1])
        else:
            tempNode = (nextNode[0], nextNode[1]-1)
    if data[nextNode[0]][nextNode[1]] == 'F':
        if diff(nextNode, startNode) == (-1, 0):
            tempNode = (nextNode[0], nextNode[1]+1)
        else:
            tempNode = (nextNode[0]+1, nextNode[1])

    startNode = nextNode
    nextNode = tempNode
    count += 1

print(ceil(count / 2))