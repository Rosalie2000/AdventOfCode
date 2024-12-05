day = 'day05'

def read_input():
    with open(f'AdventOfCode\\2024\inputs\{day}.txt', 'r') as file:
        input = file.readlines()


    split = input.index('\n')
    rules = [[int(r.strip()) for r in rule.split('|')] for rule in input[:split]]
    updates = [[int(u.strip()) for u in update.split(',')] for update in input[split+1:]]
        
    return rules, updates


def solution_part_1():
    rules, updates = read_input()

    total_sum = 0

    for update in updates:
        count = 1
        for i, num in enumerate(update):
            must_appear_before = [a for [a, b] in rules if b == num]
            must_appear_after = [b for [a, b] in rules if a == num]
            for before in update[:i]:
                if before in must_appear_after:
                    count = 0
            for after in update[i:]:
                if after in must_appear_before:
                    count = 0

        total_sum += (count * update[int(len(update)/2)])

    print(total_sum)



def solution_part_2():
    rules, updates = read_input()

    total_sum = 0

    for update in updates:
        count = 0
        for i, num in enumerate(update):
            must_appear_before = [a for [a, b] in rules if b == num]
            must_appear_after = [b for [a, b] in rules if a == num]
            for before in update[:i]:
                if before in must_appear_after:
                    count = 1
            for after in update[i:]:
                if after in must_appear_before:
                    count = 1
            if count == 1:
                sorted_update = []
                while update:
                    for num in update:
                        if all(before not in update or before in sorted_update for before, after in rules if after == num):
                            sorted_update.append(num)
                            update.remove(num)
                            break

        total_sum += (count * sorted_update[int(len(sorted_update)/2)])

    print(total_sum)