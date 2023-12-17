import re
import multiprocessing

maps: list[list[list[int]]] = []

def parse_input(filename: str) -> list[int]:
    seeds = None
    groups = None
    with open(filename, "r") as f:
        seeds = list(map(int, re.search(r"seeds: (.*)", f.readline()).groups()[0].split(' ')))
        f.readline()
        groups = [group.split('\n') for group in f.read().split('\n\n')]
    global maps
    maps = [[list(map(int, line.strip().split(' '))) for line in group[1:]] for group in groups]
            
    return seeds


def bounds_check(map_data: list[list[int]], item: int) -> int:
    for dest, source, length in map_data:
        if source <= item < source + length:
            return dest + (item - source)
    else:
        return item

def get_location(seed: int) -> int:
    soil = bounds_check(maps[0], seed)
    fert = bounds_check(maps[1], soil)
    water = bounds_check(maps[2], fert)
    light = bounds_check(maps[3], water)
    temp = bounds_check(maps[4], light)
    humid = bounds_check(maps[5], temp)
    location = bounds_check(maps[6], humid)
    return location

def get_min_location_for_seed_range(seeds: tuple[int, int]) -> int:
    min_location = float('inf')
    for seed in range(seeds[0], seeds[0] + seeds[1]):
        min_location = min(min_location, get_location(seed))
    return min_location

def part_one(seeds: list[int]) -> int:
    print(min([get_location(seed) for seed in seeds]))
 
def part_two(seeds: list[int]) -> int:
    seed_sets = [(seeds[i], seeds[i + 1]) for i in range(0, len(seeds), 2)]
    with multiprocessing.Pool() as pool:
        min_locations = pool.map(get_min_location_for_seed_range, seed_sets)
    
    print(min(min_locations))

def main(input_filename: str):
    seeds = parse_input(input_filename)
    part_one(seeds)
    part_two(seeds)

if __name__ == "__main__":
    main("input.txt")