import re

day = 'day04'

def read_input():
    with open(f'AdventOFCode\\2024\inputs\{day}.txt', 'r') as file:
        input = file.readlines()
    
    matrix = [[char for char in line.strip()] for line in input]    
    
    return input, matrix


def get_diagonals(matrix):
    n = len(matrix)
    
    diagonal1 = [] 
    diagonal2 = [] 
     
    for p in range(2*n-1):
        diagonal1.append([matrix[p-q][q] for q in range(max(0, p - n + 1), min(p, n - 1) + 1)])
        diagonal2.append([matrix[n-p+q-1][q] for q in range(max(0, p - n + 1), min(p, n - 1) + 1)])
    
    return diagonal1, diagonal2
    

def solution_part_1():
    text, matrix = read_input()
    
    horizontal_count = sum([len(re.findall(r"(?=XMAS|SAMX)", line)) for line in text])
    
    vertical = [[line[i] for line in matrix] for i in range(len(matrix[0]))]
        
    vertical_count = sum([len(re.findall(r"(?=XMAS|SAMX)", ''.join(col))) for col in vertical])
    
    diagonal1, diagonal2 = get_diagonals(matrix)
    diagonal1_count = sum([len(re.findall(r"(?=XMAS|SAMX)", ''.join(d))) for d in diagonal1])
    diagonal2_count = sum([len(re.findall(r"(?=XMAS|SAMX)", ''.join(d))) for d in diagonal2])
    
    print(horizontal_count + vertical_count + diagonal1_count + diagonal2_count)    

    # print(diagonal1)

def solution_part_2():
    pass

solution_part_1()
solution_part_2()