def getTimes(path):
    with open(path, 'r') as f:
        data = f.readlines()[0]

        times = data.split(':')[1].split()
        times = [int(time) for time in times if time != '']

    return times

def getDistances(path):
    with open(path, 'r') as f:
        data = f.readlines()[1]

        distances = data.split(':')[1].split()
        distances = [int(dist) for dist in distances if dist != '']

    return distances