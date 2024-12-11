day = 'day09'

def read_input():
    with open(f'AdventOfCode\\2024\inputs\{day}.txt', 'r') as file:
        input = file.read()
        
    return input


def get_decompressed_disk_map(line):
    is_block_file = True
    
    decompressed_disk_map = []
    id_number = 0

    for num in line:
        file_size = int(num)
        if is_block_file:
            for j in range(file_size):
                decompressed_disk_map.append(str(id_number))
            is_block_file = False
            id_number += 1
        else:
            for j in range(file_size):
                decompressed_disk_map.append('.')
            is_block_file = True

    return decompressed_disk_map


def sort_mapping(mapping):
    while '.' in mapping:        
        idx = mapping.index('.')

        for i in range(len(mapping) - 1, -1, -1):
            if mapping[i] != '.':
                num_idx = i
                break

        mapping[idx] = mapping[num_idx]
        mapping[num_idx] = '.'
        mapping.pop()

    return mapping


def solution_part_1():
    line = read_input()
    
    mapping = get_decompressed_disk_map(line)

    print('Decompressed disk map, now sorting...')
    print('Len disk map is ', len([char for char in mapping if char != '.']))

    sorted_mapping = sort_mapping(mapping)

    print('Sorted')
    
    multiples = [i*int(num) for i, num in enumerate(sorted_mapping)]
    print(sum(multiples))



def solution_part_2():
    pass


solution_part_1()
solution_part_2()
