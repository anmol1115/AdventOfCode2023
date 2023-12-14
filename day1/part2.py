sum = 0

with open("case1.txt", 'r') as f:
    lines = f.readlines()
    lookup = {
        "one": '1',
        "two": '2',
        "three": '3',
        "four": '4',
        "five": '5',
        "six": '6',
        "seven": '7',
        "eight": '8',
        "nine": '9'
    }

    for line in lines:
        line = line.strip()

        newLine = [c for c in line]
        for k, v in lookup.items():
            ptr = 0
            length = len(k)
            while ptr <= len(line) - length:
                substr = line[ptr: ptr+length]
                if substr == k:
                    newLine[ptr] = v
                ptr += 1

        l, r = 0, len(newLine)-1
        while l <= r:
            if newLine[l].isdigit():
                break
            l += 1

        while l <= r:
            if newLine[r].isdigit():
                break
            r -= 1

        sum += int(newLine[l]+newLine[r])

print(sum)