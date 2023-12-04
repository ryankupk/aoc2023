import re
from collections import defaultdict

def parse_input(filename: str):
    return open(filename, 'r').read().splitlines()

def part_one(strings: list):
    total_points = 0
    for string in strings:
        numbers: tuple[str] = re.search('Card\s+\d+: (.*)', string).groups()
        winning, yours = numbers[0].split('|')
        winning = set(winning.split(' '))
        yours = set(yours.split(' '))
        
        power = len(winning.intersection(yours))
        card_points = 2 ** (power - 2) if power > 1 else 0
        total_points += card_points
        
    print(total_points)
 
def part_two(strings: list):
    card_counts = defaultdict(int)
    for string in strings:
        idx, numbers = re.search('Card\s+(\d+): (.*)', string).groups()
        idx = int(idx)
        card_counts[idx] += 1
        winning, yours = numbers.split('|')
        winning = set(winning.split(' '))
        yours = set(yours.split(' '))
        
        wins = len(winning.intersection(yours))
        for card in range(idx+1, idx + wins):
            card_counts[card] += (1 * card_counts[idx])
            
    print(sum(card_counts.values()))
            

def main(input_filename: str):
    inp = parse_input(input_filename)
    part_one(inp)
    part_two(inp)

if __name__ == "__main__":
    main("input.txt")