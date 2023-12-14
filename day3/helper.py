def getNums(line):
    nums = []
    ptr = 0

    while ptr < len(line):
        if line[ptr].isdigit():
            end = ptr
            while end < len(line) and line[end].isdigit():
                end += 1
            nums.append([int(line[ptr:end]), ptr, end-1])
            ptr = end
        ptr += 1

    return nums

def checkSymbol(line):
    for c in line:
        if c != '.' and not c.isdigit():
            return True
    return False

def getStars(line):
    indices = []

    for i, c in enumerate(line):
        if c == '*':
            indices.append(i)

    return indices

def getNumber(idx, line, row):
    l, r = idx-1, idx+1

    while l > -1 and line[l].isdigit():
        l -= 1
    while r < len(line) and line[r].isdigit():
        r += 1

    return (int(line[l+1: r]), l+1, row)

if __name__ == "__main__":
    # getNums("467..114..")
    # print(checkSymbol(".114."))
    print(getNumber(2, '467..114..'))