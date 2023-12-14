def readData(path):
    data = []
    with open(path, 'r') as f:
        lines = f.readlines()

        data = [[*line.strip()] for line in lines]

    return data

def diff(tup1, tup2):
    return (tup1[0] - tup2[0], tup1[1] - tup2[1])

def findStart(data):
    for row in range(len(data)):
        for col in range(len(data)):
            if data[row][col] == 'S':
                return (row, col)

def findPathStart(coords, data):
    row, col = coords

    top = (row-1, col)
    bottom = (row+1, col)
    left = (row, col-1)
    right = (row, col+1)

    start = []
    for side in [top, bottom, left, right]:
        if side[0] > -1 and side[0] < len(data) and side[1] > -1 and side[1] < len(data[0]):
            if side == top and data[top[0]][top[1]] in ['7', '|', 'F']:
                start.append(top)
            if side == bottom and data[bottom[0]][bottom[1]] in ['J', '|', 'L']:
                start.append(bottom)
            if side == left and data[left[0]][left[1]] in ['L', '-', 'F']:
                start.append(left)
            if side == right and data[right[0]][right[1]] in ['J', '-', '7']:
                start.append(right)
    
    return start

if __name__ == "__main__":
    data = readData("test-case1.txt")