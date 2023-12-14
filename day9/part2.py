from helper import *

data = readData("case1.txt")

sum = 0
for values in data:
    sum += prevNumber(values)

print(sum)