import math

day = 'day08'


def read_input():
    with open(f'2024/inputs/{day}.txt', 'r') as file:
        input = file.readlines()
        input = [line.strip() for line in input]
    return input


def find_antennas(rows, cols, grid):
    antennas = {}

    # Collect antenna positions
    for x in range(rows):
        for y in range(cols):
            c = grid[x][y]
            if c != '.':
                if c not in antennas:
                    antennas[c] = []
                antennas[c].append((x, y))
    
    return antennas


def count_antinodes(grid):
    pass


def solution_part_1():
    grid = read_input()

    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0

    antennas = find_antennas(rows, cols, grid)
    

    antinodes = set()

    for freq, coords in antennas.items():
        n = len(coords)
        if n < 2:
            continue
        
        for i in range(n):
            x1, y1 = coords[i]
            for j in range(i+1, n):
                x2, y2 = coords[j]

                ax = 2*x1 - x2
                ay = 2*y1 - y2

                bx = 2*x2 - x1
                by = 2*y2 - y1

                antinodes.add((ax, ay))
                antinodes.add((bx, by))

    valid_antinodes = [(x, y) for (x, y) in antinodes if 0 <= x < rows and 0 <= y < cols]

    print(len(valid_antinodes))



def solution_part_2():
    grid = read_input()

    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0

    antennas = find_antennas(rows, cols, grid)
    

    antinodes = set()

    for freq, coords in antennas.items():
        n = len(coords)
        if n < 2:
            continue
        
        
        for i in range(n):
            x1, y1 = coords[i]
            for j in range(i+1, n):
                x2, y2 = coords[j]
                
                dx = x2 - x1
                dy = y2 - y1

                g = math.gcd(dx, dy)
                
                step_x = dx // g
                step_y = dy // g

                new_x, new_y = x1, y1
                while 0 <= new_x < rows and 0 <= new_y < cols:
                    antinodes.add((new_x, new_y))
                    new_x += step_x
                    new_y += step_y

                new_x, new_y = x1 - step_x, y1 - step_y
                while 0 <= new_x < rows and 0 <= new_y < cols:
                    antinodes.add((new_x, new_y))
                    new_x -= step_x
                    new_y -= step_y

    valid_antinodes = [(x, y) for (x, y) in antinodes if 0 <= x < rows and 0 <= y < cols]

    print(len(valid_antinodes))


solution_part_1()
solution_part_2()