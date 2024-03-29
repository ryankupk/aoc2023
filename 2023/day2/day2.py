import time
import re
import math

COLOR_MAXES = {
    'red': 12,
    'green': 13,
    'blue': 14
}

def parse_input(filename: str) -> list[tuple[str, str]]:
    # list of tuples of the form ("<game ID>", "<#> <color>, <#> <color>; <#> <color> ...")
    return [re.search(r"Game (\d+): (.*)", string).groups() for string in open(filename, "r").read().splitlines()]

def part_one(games: list[tuple[str, str]]) -> None:
    possible_ids = []
    for game in games:
        impossible = False
        id, sets = game
        for set in sets.split(';'):
            for counts in set.split(','):
                count, color = counts.strip().split(' ')
                if int(count) > COLOR_MAXES[color]: impossible = True
            
        if not impossible: possible_ids.append(int(id))
        
    print(sum(possible_ids))
                    
        
 
def part_two(games: list[tuple[str, str]]) -> None:
    total_power = 0
    for game in games:
        mins = {
            'red' : float('-inf'),
            'green' : float('-inf'),
            'blue' : float('-inf')
        }
        _, sets = game
        for set in sets.split(';'):
            for counts in set.split(','):
                count, color = counts.strip().split(' ')
                mins[color] = int(count) if int(count) > mins[color] else mins[color]
                
        total_power += math.prod(mins.values())
        
    print(total_power)
                

def main(input_filename: str):
    inp = parse_input(input_filename)
    start_part_one = time.time()
    part_one(inp)
    start_part_two = time.time()
    part_two(inp)
    end_time = time.time()
    print(f"Part one took {start_part_two - start_part_one} seconds")
    print(f"Part two took {end_time - start_part_two} seconds")

if __name__ == "__main__":
    main("input.txt")
