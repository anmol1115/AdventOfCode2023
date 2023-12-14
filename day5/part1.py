from helper import parseInput, getFromRange

data = parseInput("test-case1.txt")
minLoc = float("inf")

for seed in data["seeds"]:
    soil = getFromRange(data["seed-to-soil"], seed)
    fertilizer = getFromRange(data["soil-to-fertilizer"], soil)
    water = getFromRange(data["fertilizer-to-water"], fertilizer)
    light = getFromRange(data["water-to-light"], water)
    temp = getFromRange(data["light-to-temperature"], light)
    humidity = getFromRange(data["temperature-to-humidity"], temp)
    loc = getFromRange(data["humidity-to-location"], humidity)

    minLoc = min(minLoc, loc)

print(minLoc)