from helper import *

times = getTimes("case1.txt")
distances = getDistances("case1.txt")

actual_time = int(''.join(map(str, times)))
actual_dist = int(''.join(map(str, distances)))

count = 0
for i in range(1, actual_time+1):
    if i * (actual_time-i) > actual_dist:
        count += 1

print(count)