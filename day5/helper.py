import re

def getInput(line):
    inputs = line.strip().split(':')[1].strip(' ').split(' ')
    inputs = [int(inp) for inp in inputs]

    return {"seeds": inputs}

def genMap(lines):
    mapName = lines[0].strip().split(' ')[0]
    lines.pop(0)

    conversion_map = {mapName: {
        "source_min": [],
        "source_max": [],
        "dest_min": [],
        "dest_max": []
    }}

    expr = "^.* map"
    while len(lines) and not re.search(expr, lines[0]):
        line = lines[0]
        line = line.strip()

        dest, start, _range = line.split(' ')
        conversion_map[mapName]["source_min"].append(int(start))
        conversion_map[mapName]["source_max"].append(int(start)+int(_range)-1)
        conversion_map[mapName]["dest_min"].append(int(dest))
        # conversion_map[mapName]["dest_max"].append(int(dest)+int(_range)-1)
        
        lines.pop(0)
    return conversion_map, lines

def parseInput(path):
    with open(path, 'r') as f:
        lines = f.readlines()
        lines = [line for line in lines if line != '\n']

        conversion_map = getInput(lines[0])
        lines = lines[1:]
        while len(lines):
            _map, lines = genMap(lines)
            conversion_map.update(_map)
        
    return conversion_map

def getFromRange(data, val):
    for idx, (_min, _max) in enumerate(zip(data["source_min"], data["source_max"])):
        if _min <= val <= _max:
            diff = val - _min
            dest_val = data["dest_min"][idx] + diff
            return dest_val
    return val


if __name__ == "__main__":
    # print(parseInput("./test-case1.txt"))
    data = parseInput("./test-case1.txt")
    getFromRange(data["seed-to-soil"], None)
