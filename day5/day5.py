import re

def parse_input(filename: str):
    seeds = None
    seed_soil_map_data = []
    soil_fertilizer_map_data = []
    fertilizer_water_map_data = []
    water_light_map_data = []
    light_temperature_map_data = []
    temperature_humidity_map_data = []
    humidity_location_map_data = []
    with open(filename, "r") as f:
        # lines = f.read().splitlines()
        seeds = list(map(int, re.search("seeds: (.*)", f.readline()).groups()[0].split(' ')))
        f.readline(); f.readline()
        # idx = 3 # read from start of seed-to-soil map
        while line := f.readline():
            if line != '\n':
                seed_soil_map_data.append(list(map(int, line.strip().split(' '))))
            else: break
        f.readline()
        
        while line := f.readline():
            if line != '\n':
                soil_fertilizer_map_data.append(list(map(int, line.strip().split(' '))))
            else: break
        f.readline()
        
        while line := f.readline():
            if line != '\n':
                fertilizer_water_map_data.append(list(map(int, line.strip().split(' '))))
            else: break
        f.readline()
        
        while line := f.readline():
            if line != '\n':
                water_light_map_data.append(list(map(int, line.strip().split(' '))))
            else: break
        f.readline()
        
        while line := f.readline():
            if line != '\n':
                light_temperature_map_data.append(list(map(int, line.strip().split(' '))))
            else: break
        f.readline()
        
        while line := f.readline():
            if line != '\n':
                temperature_humidity_map_data.append(list(map(int, line.strip().split(' '))))
            else: break
        f.readline()
        
        while line := f.readline():
            if line != '\n':
                humidity_location_map_data.append(list(map(int, line.strip().split(' '))))
            else: break
        f.readline()
            
    return (seeds, seed_soil_map_data, soil_fertilizer_map_data, fertilizer_water_map_data, water_light_map_data, light_temperature_map_data, temperature_humidity_map_data, humidity_location_map_data)


def bounds_check(map_data, item):
    for dest, source, length in map_data:
        if source <= item < source + length:
            return dest + (item - source)
    else:
        return item

def get_location(seed: int, seed_soil_map_data, soil_fertilizer_map_data, fertilizer_water_map_data, water_light_map_data, light_temperature_map_data, temperature_humidity_map_data, humidity_location_map_data):
    soil = bounds_check(seed_soil_map_data, seed)
    fert = bounds_check(soil_fertilizer_map_data, soil)
    water = bounds_check(fertilizer_water_map_data, fert)
    light = bounds_check(water_light_map_data, water)
    temp = bounds_check(light_temperature_map_data, light)
    humid = bounds_check(temperature_humidity_map_data, temp)
    location = bounds_check(humidity_location_map_data, humid)
    return location

def part_one(seeds, seed_soil_map_data, soil_fertilizer_map_data, fertilizer_water_map_data, water_light_map_data, light_temperature_map_data, temperature_humidity_map_data, humidity_location_map_data):
    locations = []
    
    for seed in seeds:
        locations.append(get_location(seed, seed_soil_map_data, soil_fertilizer_map_data, fertilizer_water_map_data, water_light_map_data, light_temperature_map_data, temperature_humidity_map_data, humidity_location_map_data))
    
    print(min(locations))
 
def part_two(seeds, seed_soil_map_data, soil_fertilizer_map_data, fertilizer_water_map_data, water_light_map_data, light_temperature_map_data, temperature_humidity_map_data, humidity_location_map_data):
    min_location = float('inf')
    for idx, seed in enumerate(seeds):
        if idx % 2 == 1: continue
        for seed in range(seed, seed + seeds[idx+1]):
            cur_location = get_location(seed, seed_soil_map_data, soil_fertilizer_map_data, fertilizer_water_map_data, water_light_map_data, light_temperature_map_data, temperature_humidity_map_data, humidity_location_map_data)
            min_location = min(min_location, cur_location)
        print(f"completed iteration {idx}")
        
    
    print(min_location)

def main(input_filename: str):
    inp = parse_input(input_filename)
    part_one(*inp)
    part_two(*inp)

if __name__ == "__main__":
    main("input.txt")