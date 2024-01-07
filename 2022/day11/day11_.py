import sys
from math import floor
from gmpy2 import mpz

class Monkey:
    def __init__(self, monkeys, name, items, operation, divisible_test, true_monkey, false_monkey):
        self.monkeys = monkeys
        self.name = name
        self.items = [mpz(item) for item in items]
        self.operation = [operation[0], mpz(operation[1]) if operation[1] != 'old' else operation[1]]
        self.divisible_test = mpz(divisible_test)
        self.true_monkey = int(true_monkey)
        self.false_monkey = int(false_monkey)
        self.num_inspected = 0
        
    def inspect_item(self, idx, worry):
        new_item = mpz(0)
        item = self.items[idx]
        if self.operation[0] == "*":
            if self.operation[1] == "old":
                new_item = mpz(item) * mpz(item)
            else: new_item = mpz(item) * mpz(self.operation[1])
            
        elif self.operation[0] == "+":
            if self.operation[1] == "old":
                new_item = mpz(item) + mpz(item)
            else: new_item = mpz(item) + mpz(self.operation[1])
            
        
        if worry: self.items[idx] = floor(new_item / 3)
        else: self.items[idx] = new_item % 9699690
        
        self.num_inspected += 1
        

def parse_data(filename):
    data = []
    with open(filename) as f:
        lines = f.read().splitlines()
        for i in range(0, len(lines), 7):
            monkeys = [i for i in range(8)]
            name = lines[i][-2]
            items = [num[:2] for num in lines[i + 1].split()[2:]]
            operation = lines[i + 2].split()[-2:]
            divisible_test = lines[i + 3].split()[-1]
            true_monkey = lines[i + 4].split()[-1]
            false_monkey = lines[i + 5].split()[-1]
            data.append(Monkey(monkeys, name, items, operation, divisible_test, true_monkey, false_monkey))
        
    return data


def solve_part_one(monkeys):
    round = 1
    while round != 21:
        for monkey in monkeys:
            for idx, _ in enumerate(monkey.items):
                monkey.inspect_item(idx, True)
                
                if mpz(monkey.items[idx]) % mpz(monkey.divisible_test) == 0:
                    monkeys[monkey.true_monkey].items.append(monkey.items[idx])
                else:
                    monkeys[monkey.false_monkey].items.append(monkey.items[idx])
                    
            monkey.items = []
        round += 1
        
    monkeys.sort(key=lambda monkey: monkey.num_inspected * -1)
    return monkeys[0].num_inspected * monkeys[1].num_inspected
        
                    

def solve_part_two(monkeys):
    round = 1
    while round != 10001:
        for monkey in monkeys:
            for idx, _ in enumerate(monkey.items):
                monkey.inspect_item(idx, False)
                
                if mpz(monkey.items[idx]) % mpz(monkey.divisible_test) == 0:
                    monkeys[monkey.true_monkey].items.append(monkey.items[idx])
                else:
                    monkeys[monkey.false_monkey].items.append(monkey.items[idx])
                    
            monkey.items = []
        round += 1
        
    monkeys.sort(key=lambda monkey: monkey.num_inspected * -1)
    return monkeys[0].num_inspected * monkeys[1].num_inspected


def main(filename):
    data = parse_data(filename)
    
    print(solve_part_one(data))
    print(solve_part_two(data))
    
    
if __name__ == "__main__":
    main(r"input.txt")