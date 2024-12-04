import re


def read_input():
    with open('AdventOfCode\\2024\inputs\day03.txt', 'r') as file:
        input = file.read()
        
    return input


def solution_part_1():
    text = read_input()
    summed_multiples = sum([int(x)*int(y) for (x, y) in re.findall(r"mul\((\d{1,3}),(\d{1,3})\)", text)])
    print(summed_multiples)


def solution_part_2():
    text = read_input()

    add_multiplies = True
    summed_multiples = 0

    for instruction, x, y in re.findall(r"(do\(\)|don't\(\)|mul\((\d{1,3}),(\d{1,3})\))", text):
        if instruction == "do()":
            add_multiplies = True
        if instruction == "don't()":
            add_multiplies = False
        if add_multiplies and "mul(" in instruction:
            summed_multiples += int(x)*int(y) 
    
    print(summed_multiples)
