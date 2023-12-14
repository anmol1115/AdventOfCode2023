from helper import getFromRange, parseInput

data = parseInput("case1.txt")
minLoc = float("inf")
idx = 0

while idx < len(data["seeds"]):
    start =  data["seeds"][idx]
    _range =  data["seeds"][idx+1]
    for r in range(_range):
        seed = start + r
        soil = getFromRange(data["seed-to-soil"], seed)
        fertilizer = getFromRange(data["soil-to-fertilizer"], soil)
        water = getFromRange(data["fertilizer-to-water"], fertilizer)
        light = getFromRange(data["water-to-light"], water)
        temp = getFromRange(data["light-to-temperature"], light)
        humidity = getFromRange(data["temperature-to-humidity"], temp)
        loc = getFromRange(data["humidity-to-location"], humidity)

        minLoc = min(minLoc, loc)

    idx += 2

print(minLoc)