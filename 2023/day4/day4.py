import re
from collections import defaultdict

def parse_input(filename: str) -> list[tuple[str, str]]:
    return [re.search(r"Card\s+(\d+): (.*)", string).groups() for string in open(filename, 'r').read().splitlines()]

def part_one(cards: list[tuple[str, str]]) -> None:
    total_points = 0
    for card in cards:
        _, numbers = card
        winning, yours = [set(piece.split(' ')) for piece in numbers.split('|')]
        
        power = len(winning.intersection(yours))
        card_points = 2 ** (power - 2) if power > 1 else 0
        total_points += card_points
        
    print(total_points)
 
def part_two(cards: list[tuple[str, str]]) -> None:
    card_counts = defaultdict(int)
    for card in cards:
        idx, numbers = int(card[0]), card[1]
        card_counts[idx] += 1
        winning, yours = [set(piece.split(' ')) for piece in numbers.split('|')]
        
        wins = len(winning.intersection(yours))
        for current_card in range(idx+1, idx + wins):
            card_counts[current_card] += (card_counts[idx])
            
    print(sum(card_counts.values()))
            

def main(input_filename: str):
    inp = parse_input(input_filename)
    part_one(inp)
    part_two(inp)

if __name__ == "__main__":
    main("input.txt")