def readinput():
    left = []
    right = []
    input_path = "day01.txt"
    with open(input_path, 'r') as input:
        for line in input:
            left.append(int(line.split()[0]))
            right.append(int(line.split()[1]))
    return [left, right]

def solution():
    left, right = readinput()
    left.sort()
    right.sort()

    sum = 0

    distances = [(abs(left[i] - right[i])) for i in range(len(left))]

    for dist in distances:
        sum += dist

    print(sum)

