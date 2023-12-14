from helper import *

data = readData("case1.txt")
expandedUniverse = expandUniverse(data)

galaxies = []
for row in range(len(expandedUniverse)):
    for col in range(len(expandedUniverse[0])):
        if expandedUniverse[row][col] == '#':
            galaxies.append((row, col))

sum = 0
for i in range(len(galaxies)-1):
    for j in range(i+1, len(galaxies)):
        sum += manhattanDist(galaxies[i], galaxies[j])

print(sum)