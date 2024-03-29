import time
import re

def parse_input(filename: str) -> tuple[list[int], list[int]]:
    with open(filename, "r") as f:
        times = list(map(int, re.search(r'Time:\s*(.*)', f.readline()).groups()[0].split()))
        distances = list(map(int, re.search(r'Distance:\s*(.*)', f.readline()).groups()[0].split()))
    return times, distances

def calculate_distance(time_held: int, total_time: int) -> int:
    return (total_time - time_held) * time_held

def part_one(times: list[int], distances_to_beat: list[int]) -> None:
    margin_of_error = 1
    for time, distance_to_beat in zip(times, distances_to_beat):
        ways_to_win = 0
        for ms in range(1, time):
            if calculate_distance(ms, time) > distance_to_beat:
                ways_to_win += 1
        margin_of_error *= ways_to_win
    print(margin_of_error)
    
 
def part_two(times: list[int], distances_to_beat: list[int]) -> None:
    time = int(''.join(list(map(str, times))))
    distance_to_beat = int(''.join(list(map(str, distances_to_beat))))
    ways_to_win = 0
    for ms in range(1, time):
        if calculate_distance(ms, time) > distance_to_beat:
            ways_to_win += 1
    print(ways_to_win)

def main(input_filename: str):
    times, distances_to_beat = parse_input(input_filename)
    start_part_one = time.time()
    part_one(times, distances_to_beat)
    start_part_two = time.time()
    part_two(times, distances_to_beat)
    end_time = time.time()
    print(f"Part one took {start_part_two - start_part_one} seconds")
    print(f"Part two took {end_time - start_part_two} seconds")

if __name__ == "__main__":
    main("input.txt")
