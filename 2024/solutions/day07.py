import itertools

day = 'day07'

def read_input():
    with open(f'2024\inputs\{day}.txt', 'r') as file:
        input = file.readlines()
        
    split_input = [(int(line.split(':')[0]), [int(num.strip()) for num in line.split(':')[1].split(' ') if num != '']) for line in input]
    
    return split_input


def get_possible_equations(nums, operators):    
    combos = itertools.product(operators, repeat=len(nums)-1)
    
    equations = []
    
    for combo in combos:
        equation = str(nums[0]) + ' '
        for i in range(len(nums)-1):
            equation += combo[i] + ' ' + str(nums[i+1]) + ' '
        equations.append(equation)

    return equations    


def calculate(equation):
    equation = equation.split(' ')
        
    total = int(equation[0])
    
    for i in range(1, len(equation)):
        if equation[i] == '+':
            total = total + int(equation[i+1])
            
        if equation[i] == '*':
            total = total * int(equation[i+1])
            
        elif equation[i - 1] == '||':
            total = int(str(total) + str(equation[i]))
            
    return int(total)


def solution_part_1():
    lines = read_input()
    
    summed_true_values = 0
    
    for (test_value, nums) in lines:
        equations = get_possible_equations(nums, ['+', '*'])
        
        for eq in equations:
            if calculate(eq) == test_value:
                summed_true_values += test_value
                break
            
    print(summed_true_values)        
            

def solution_part_2():
    lines = read_input()
    
    summed_true_values = 0
    
    for (test_value, nums) in lines:
        equations = get_possible_equations(nums, ['+', '*', '||'])
        
        for eq in equations:                        
            if calculate(eq) == test_value:
                summed_true_values += test_value
                break
            
    print(summed_true_values)  

