from math import gcd

def readData(path):
    with open(path, 'r') as f:
        data = f.readlines()
        directions = data[0].strip()
        nodes = data[2:]

        node_map = {}
        for node in nodes:
            node_from, node_to = node.split('=')

            node_left, node_right = node_to.split(',')
            node_map[node_from.strip()] = {'L': node_left[2:], 'R': node_right[1:4]}

        return directions, node_map
    
def checkLast(nodes):
    for node in nodes:
        if node[-1] != 'Z':
            return False
    return True

def getLCM(numbers):
    lcm = 1
    for i in numbers:
        lcm = lcm*i//gcd(lcm, i)
    return lcm

if __name__ == "__main__":
    print(readData("./test-case1.txt"))