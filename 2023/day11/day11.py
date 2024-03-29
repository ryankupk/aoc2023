import time
from copy import copy

def parse_input(filename: str):
    return open(filename, "r").read().splitlines()

def expand_space(strings: list[str]) -> list[str]:
    expanded = copy(strings)
    w = len(expanded[0])
    empty_row = '.' * w
    indices_to_add = []
    for idx, string in enumerate(expanded):
        if '#' not in string:
            indices_to_add.insert(0,idx)
    for index in indices_to_add:
        expanded.insert(index, empty_row)
    
    l = len(expanded)
    for x in range(w - 1, -1, -1):
        string = ''
        for y in range(l):
            if expanded[y][x] == '#': break
            string += expanded[y][x]
        else:
            for idx, cur_string in enumerate(expanded):
                expanded[idx] = cur_string[:x] + '.' + cur_string[x:]
    return expanded

def get_expanded_indices(strings: list[str]) -> tuple[ list[int], list[int] ]:
    y_indices_to_add = [idx for idx, string in enumerate(strings) if '#' not in string]
    
    x_indices_to_add = []
    l = len(strings[0])
    for i in range(l):
        if '#' not in [string[i] for string in strings]:
            x_indices_to_add.append(i)
    return x_indices_to_add, y_indices_to_add

def get_distance(x1y1: tuple[int, int], x2y2: tuple[int, int]) -> int:
    return abs((x2y2[1] - x1y1[1])) + abs((x2y2[0] - x1y1[0]))

def part_one(strings: list[str]):
    distances = []
    coordinates = {0: (None, None)}
    expanded = expand_space(strings)
    for y, line in enumerate(expanded):
        for x in [i for i, ltr in enumerate(line) if ltr == '#']:
            coordinates[max(list(coordinates.keys())) + 1] = (x, y)
    del coordinates[0] # it made indexing easy don't talk to me
    
    min_key = min(coordinates.keys())
    max_key = max(coordinates.keys())
    for i in range(min_key, max_key + 1):
        for j in range(i + 1, max_key + 1):
            distances.append(get_distance(coordinates[i], coordinates[j]))
    
    
    print(sum(distances))
 
def part_two(strings: list[str]):
    distances = []
    scale = 1000000
    
    coordinates = {0: (None, None)}
    expanded_indices = get_expanded_indices(strings)
    for y, line in enumerate(strings):
        for x in [i for i, ltr in enumerate(line) if ltr == '#']:
            expanded_x = x + ((scale - 1) * len([exd for exd in expanded_indices[0] if exd < x]))
            expanded_y = y + ((scale - 1) * len([exd for exd in expanded_indices[1] if exd < y]))
            coordinates[max(list(coordinates.keys())) + 1] = (expanded_x, expanded_y)
    del coordinates[0]
    
    min_key = min(coordinates.keys())
    max_key = max(coordinates.keys())
    for i in range(min_key, max_key + 1):
        for j in range(i + 1, max_key + 1):
            distances.append(get_distance(coordinates[i], coordinates[j]))
    
    
    print(sum(distances))


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
