sum = 0

with open("case1.txt", 'r') as f:
    lines = f.readlines()

    for line in lines:
        l, r = 0, len(line)-1
        while l <= r:
            if line[l].isdigit():
                break
            l += 1
        while l <= r:
            if line[r].isdigit():
                break
            r -= 1

        sum += int(line[l]+line[r])
        
print(sum)