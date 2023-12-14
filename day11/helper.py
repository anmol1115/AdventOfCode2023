def readData(path):
    data = []
    with open(path, 'r') as f:
        lines = f.readlines()

        data = [[*line.strip()] for line in lines]

    return data

def expandrows(data):
    i = 0
    while i < len(data):
        j = 0
        flag = True
        while j < len(data[i]) and flag:
            if data[i][j] == '#':
                flag = False
            j += 1
        if flag:
            data.insert(i, ['.']*len(data[i]))
            i += 1

        i += 1
    return data

def expandUniverse(data):
    data = expandrows(data)
    data = list(map(list, zip(*data)))
    data = expandrows(data)
    data = list(map(list, zip(*data)))
    return data

def manhattanDist(pt1, pt2):
    return abs(pt1[0] - pt2[0]) + abs(pt1[1] - pt2[1])