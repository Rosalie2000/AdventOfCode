def readinput():
    left = []
    right = []
    input_path = "AdventOfCode\\2024\inputs\day01.txt"
    with open(input_path, 'r') as input:
        for line in input:
            left.append(int(line.split()[0]))
            right.append(int(line.split()[1]))
    return [left, right]

def solution_part_1():
    left, right = readinput()
    left.sort()
    right.sort()

    sum = 0

    distances = [(abs(left[i] - right[i])) for i in range(len(left))]

    for dist in distances:
        sum += dist

    print(sum)

def solution_part_2():
    left, right = readinput()

    result = 0
    

    for l_num in left:
        occ_of_l_in_r = 0
        for r_num in right:
            if l_num == r_num:
                occ_of_l_in_r += 1
        if occ_of_l_in_r > 0:
            result += (l_num*occ_of_l_in_r)

    print(result)


