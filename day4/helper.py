def getNumbers(line):
    _, data = line.split(':')
    wNums, Nums = data.split('|')

    wNums = set([int(num.strip()) for num in wNums.split(' ') if len(num)])
    Nums = set([int(num.strip()) for num in Nums.split(' ') if len(num)])

    return wNums, Nums