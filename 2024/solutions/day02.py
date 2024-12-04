def read_input():
    with open('2024\inputs\day02.txt', 'r') as file:
        input = file.readlines()
        
    report = [[int(num) for num in line.split()] for line in input]
    return report


def valid_report(report):
    check_increase = 0
    check_decrease = 0
    for i, num in enumerate(report):
        if i + 1 < len(report):
    
            if report[i+1] > num and (report[i+1] <= num + 3):
                check_increase += 1
                
            if report[i+1] < num and (report[i+1] >= num - 3):
                check_decrease += 1
                
    if check_increase == len(report) - 1 or check_decrease == len(report) - 1:
        return True
    
    return False
    

def solution_part_1():
    valid_reports = 0
    
    for report in read_input():
        if valid_report(report):
            valid_reports += 1
    
    print(valid_reports)
    
    

def solution_part_2():
    valid_reports = 0
    
    for report in read_input():
        if valid_report(report):
            valid_reports += 1
            
        else:
            for i in range(len(report)):
                temp_report = report[:i] + report[i+1:]
                if valid_report(temp_report):
                    valid_reports += 1 
                    break
    
    print(valid_reports)