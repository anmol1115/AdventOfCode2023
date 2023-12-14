from helper import *

data = readData("case1.txt")

sum = 0
for values in data:
    sum += nextNumber(values)

print(sum)