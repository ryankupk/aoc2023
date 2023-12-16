import re
from multiprocessing import Pool

def parse_input(filename: str) -> list[list[list[int]]]:
    seeds = None
    groups = None
    maps = []
    with open(filename, "r") as f:
        seeds = list(map(int, re.search(r"seeds: (.*)", f.readline()).groups()[0].split(' ')))
        f.readline()
        groups = [group.split('\n') for group in f.read().split('\n\n')]
    for group in groups:
        cur_map = []
        for line in group[1:]: # skip name of map
            cur_map.append(list(map(int, line.strip().split(' '))))
            
        maps.append(cur_map)
    return seeds, maps


def bounds_check(map_data, item):
    for dest, source, length in map_data:
        if source <= item < source + length:
            return dest + (item - source)
    else:
        return item

def get_location(seed: int, maps: list[list[list[int]]]):
    
    soil = bounds_check(maps[0], seed)
    fert = bounds_check(maps[1], soil)
    water = bounds_check(maps[2], fert)
    light = bounds_check(maps[3], water)
    temp = bounds_check(maps[4], light)
    humid = bounds_check(maps[5], temp)
    location = bounds_check(maps[6], humid)
    return location

def part_one(seeds: list[int], maps: list[list[list[int]]]):
    locations = []
    
    for seed in seeds:
        locations.append(get_location(seed, maps))
    
    print(min(locations))
 
def part_two(seeds, maps):
    min_location = float('inf')
    for idx, seed in enumerate(seeds):
        if idx % 2 == 1: continue
        for seed in range(seed, seed + seeds[idx+1]):
            cur_location = get_location(seed, maps)
            min_location = min(min_location, cur_location)
        print(f"completed iteration {idx}")
        
    
    print(min_location)

def main(input_filename: str):
    seeds, maps = parse_input(input_filename)
    part_one(seeds, maps)
    part_two(seeds, maps)

if __name__ == "__main__":
    main("sample.txt")