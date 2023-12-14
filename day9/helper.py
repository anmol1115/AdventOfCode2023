def readData(path):
    data = []
    with open(path, 'r') as f:
        lines = f.readlines()

        for line in lines:
            data.append(list(map(int, line.split())))

    return data

def checkZero(values):
    for val in values:
        if val != 0:
            return False
    return True

def nextNumber(values):
    if checkZero(values):
        return 0

    diff = []
    for i in range(1, len(values)):
        diff.append(values[i] - values[i-1])

    number = nextNumber(diff) + values[-1]
    return number

def prevNumber(values):
    if checkZero(values):
        return 0
    
    diff = []
    for i in range(1, len(values)):
        diff.append(values[i] - values[i-1])

    number = values[0] - prevNumber(diff)
    return number

if __name__ == "__main__":
    # print(readData("test-case1.txt"))
    # print(nextNumber([0, 3, 6, 9, 12, 15]))
    # print(nextNumber([1, 3, 6, 10, 15, 21]))
    print(prevNumber([10, 13, 16, 21, 30, 45]))