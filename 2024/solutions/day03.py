def read_input():
    with open('2024\inputs\day03.txt', 'r') as file:
        input = file.read()
        
    return input

def solution_part_1():
    text = read_input()
    multiples = [idx for idx in range(len(text)) if text.startswith('mul(', idx)] 
    print(multiples)
    for i, char in enumerate(text):
        if i in multiples:
            # this is where the X, Y starts
            print(text[i+4])
            
            possible_X = text[i+4:i+6]
            possible_comma = text[i+5:7]
            possible_Y = text[i+6:i+10]

def solution_part_2():
    return None