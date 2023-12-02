import re

COLOR_MAXES = {
    'red': 12,
    'green': 13,
    'blue': 14
}

def parse_input(filename: str):
    return open(filename, "r").read().splitlines()

def part_one(strings: list):
    possible_ids = []
    for string in strings:
        impossible = False
        id, sets = re.search("Game (\d+): (.*)", string).groups()
        for set in sets.split(';'):
            for counts in set.split(','):
                count, color = counts.strip().split(' ')
                if int(count) > COLOR_MAXES[color]:
                    impossible = True
            
        if not impossible: possible_ids.append(int(id))
        
    print(sum(possible_ids))
                    
        
 
def part_two(strings: list):
    total_power = 0
    for string in strings:
        mins = {
            'red' : float('-inf'),
            'green' : float('-inf'),
            'blue' : float('-inf')
        }
        _, sets = re.search("Game (\d+): (.*)", string).groups()
        for set in sets.split(';'):
            for counts in set.split(','):
                count, color = counts.strip().split(' ')
                mins[color] = int(count) if int(count) > mins[color] else mins[color]
                
        cur_power = 1
        for power in mins.values():
            cur_power *= power
        total_power += cur_power
        
    print(total_power)
                

def main(input_filename: str):
    inp = parse_input(input_filename)
    part_one(inp)
    part_two(inp)

if __name__ == "__main__":
    main("input.txt")