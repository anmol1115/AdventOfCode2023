from helper import *

data = readData("test-case2.txt")
StartLoc = findStart(data)

pathStart, pathEnd = findPathStart(StartLoc, data)

startNode, nextNode = StartLoc, pathStart
path = set([startNode, nextNode])
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
    path.add(nextNode)

ar = 0
for row in range(len(data)):
    for col in range(len(data[0])):
        if (row, col) not in path:
            count = 0
            newcol = col-1
            while newcol > -1:
                if (row, newcol) in path and data[row][newcol] in ['|', 'F', 'J', '7', 'L']:
                    count += 1
                newcol -= 1
            if count % 2 == 1:
                print(row, col, data[row][col])
                ar += 1

print(ar)