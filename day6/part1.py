from helper import *

times = getTimes("case1.txt")
distances = getDistances("case1.txt")
prod = 1

for idx, time in enumerate(times):
    count = 0
    for i in range(1, time+1):
        if i * (time-i) > distances[idx]:
            count += 1
    prod *= count

print(prod)