day = 'day09'

def read_input():
    with open(f'2024\inputs\{day}.txt', 'r') as file:
        input = file.read()
        
    return input


def solution_part_1():
    line = read_input()
    print(line)
    
    is_block_file = True
    
    decompressed_disk_map = ''
    
    for i, num in enumerate(line):
        file_size = int(num)
        if is_block_file:
            for j in range(file_size):
                decompressed_disk_map += str(i)
                is_block_file = False
        else:
            for j in range(file_size):
                decompressed_disk_map += '.'
                is_block_file = True
                
        
    print(decompressed_disk_map)

def solution_part_2():
    pass

solution_part_1()
solution_part_2()