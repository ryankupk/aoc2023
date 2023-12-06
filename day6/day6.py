import re

def parse_input(filename: str):
    with open(filename, "r") as f:
        times = list(map(int, re.search('Time:\s*(.*)', f.readline()).groups()[0].split()))
        distances = list(map(int, re.search('Distance:\s*(.*)', f.readline()).groups()[0].split()))
    return times, distances

def calculate_distance(time_held, total_time):
    return (total_time - time_held) * time_held

def part_one(times, distances_to_beat):
    margin_of_error = 1
    for time, distance_to_beat in zip(times, distances_to_beat):
        ways_to_win = 0
        for ms in range(1, time):
            if calculate_distance(ms, time) > distance_to_beat:
                ways_to_win += 1
        margin_of_error *= ways_to_win
    print(margin_of_error)
    
 
def part_two(times, distances_to_beat):
    time = int(''.join(list(map(str, times))))
    distance_to_beat = int(''.join(list(map(str, distances_to_beat))))
    ways_to_win = 0
    for ms in range(1, time):
        if calculate_distance(ms, time) > distance_to_beat:
            ways_to_win += 1
    print(ways_to_win)

def main(input_filename: str):
    times, distances_to_beat = parse_input(input_filename)
    part_one(times, distances_to_beat)
    part_two(times, distances_to_beat)

if __name__ == "__main__":
    main("input.txt")