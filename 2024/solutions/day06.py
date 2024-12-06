day = 'day06'

obstructions = ['#', 'O']

def read_input():
    with open(f'2024\inputs\{day}.txt', 'r') as file:
        input = file.readlines()
        
    matrix = [[char for char in line.strip()] for line in input]    
    
    return input, matrix
        
        
def moveup(matrix, y, x, direction, is_in_matrix, visited_path):
    while y > 0 and matrix[y-1][x] not in obstructions:
        y -= 1
        if matrix[y][x] == '.':
            matrix[y][x] = 'X'
            visited_path.append((y, x, direction))
        if y == 0:
            is_in_matrix = False
            break
    return matrix, x, y, '>', is_in_matrix, visited_path


def movedown(matrix, y, x, direction, is_in_matrix, visited_path):
    while y + 1 < len(matrix) and matrix[y+1][x] not in obstructions:
        y += 1
        if matrix[y][x] == '.':
            matrix[y][x] = 'X'
            visited_path.append((y, x, direction))
        if y == len(matrix) - 1:
            is_in_matrix = False
            break
    return matrix, x, y, '<', is_in_matrix, visited_path


def moveleft(matrix, y, x, direction, is_in_matrix, visited_path):
    while x > 0 and matrix[y][x-1] not in obstructions:
        x -= 1
        if matrix[y][x] == '.':
            matrix[y][x] = 'X'
            visited_path.append((y, x, direction))
        if x == 0:
            is_in_matrix = False
            break
    return matrix, x, y, '^', is_in_matrix, visited_path


def moveright(matrix, y, x, direction, is_in_matrix, visited_path):
    while x + 1 < len(matrix[y]) and matrix[y][x+1] not in obstructions:
        x += 1
        if matrix[y][x] == '.':
            matrix[y][x] = 'X'
            visited_path.append((y, x, direction))
        if x == len(matrix[y]):
            is_in_matrix = False
            break
    return matrix, x, y, 'v', is_in_matrix, visited_path


def move_through_matrix(matrix, y, x, direction, is_in_matrix, visited_path):
    if direction == '>':
        matrix, x, y, direction, is_in_matrix, new_path = moveright(matrix, y, x, direction, is_in_matrix, visited_path)
    elif direction == '<':
        matrix, x, y, direction, is_in_matrix, new_path = moveleft(matrix, y, x, direction, is_in_matrix, visited_path)
    elif direction == '^':
        matrix, x, y, direction, is_in_matrix, new_path = moveup(matrix, y, x, direction, is_in_matrix, visited_path)
    elif direction == 'v':
        matrix, x, y, direction, is_in_matrix, new_path = movedown(matrix, y, x, direction, is_in_matrix, visited_path)
    return matrix, x, y, direction, is_in_matrix, new_path


def solution_part_1():
    lines, matrix = read_input()
    
    is_in_matrix = True
    direction = '^'
    
    for y in range(len(matrix)):
        for x in range(len(matrix[y])):
            if matrix[y][x] == '^': # mark starting point
                matrix[y][x] = 'X'
                while is_in_matrix:                    
                    matrix, x, y, direction, is_in_matrix, _ = move_through_matrix(matrix, y, x, direction, is_in_matrix, [])
                        
      
    path_length = len([x for y in matrix for x in y if x == 'X'])
                
    print(path_length)
            

def solution_part_2():
    lines, matrix = read_input()
    
    is_in_matrix = True
    loops = 0
    direction = '^'    
                
    for obstruction_y in range(len(matrix)):
        for obstruction_x in range(len(matrix[obstruction_y])):
    
            if matrix[obstruction_y][obstruction_x] not in obstructions:
                matrix[obstruction_y][obstruction_x] = 'O'
            
                
                for y in range(len(matrix)):
                    for x in range(len(matrix[y])):
                        if matrix[y][x] == '^': 
                            while is_in_matrix:   
                                visited_path = []
                    
                                matrix, x, y, direction, is_in_matrix, visited_path = move_through_matrix(matrix, y, x, direction, is_in_matrix, visited_path)
                                     
                                if (y, x, direction) in visited_path:
                                    loops += 1
                                    matrix[obstruction_y][obstruction_x] = '.'
                                    break
                                break
                            break       
                        break
                    break
                matrix[obstruction_y][obstruction_x] = '.'        
                                
    print(loops)
    for line in matrix:
        print(line)
    
solution_part_1()
solution_part_2()