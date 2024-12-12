import time
from functools import cache

def parse_input(filename: str) -> list[str]:
    with open(filename) as f:
        return [int(string) for string in f.readline().strip().split(' ')]

@cache
def count_stones_after_n_steps(stone: int, steps: int) -> int:
    if steps == 0:
        return 1
        
    if stone == 0:
        return count_stones_after_n_steps(1, steps - 1)
    elif len(str(stone)) % 2 == 0:
        stone_str = str(stone)
        mid = len(stone_str) // 2
        left = int(stone_str[:mid])
        right = int(stone_str[mid:])
        return (count_stones_after_n_steps(left, steps - 1) + 
                count_stones_after_n_steps(right, steps - 1))
    else:
        return count_stones_after_n_steps(stone * 2024, steps - 1)

def part_one(stones: list[int]) -> None:
    res = 0
    for stone in stones:
        res += count_stones_after_n_steps(stone, 25)
    print(res)
    
def part_two(stones: list[int]) -> None:
    res = 0
    for stone in stones:
        res += count_stones_after_n_steps(stone, 75)
    print(res)

def main(input_filename: str):
    inp = parse_input(input_filename)
    start_part_one = time.time()
    part_one(inp)
    start_part_two = time.time()
    part_two(inp)
    end_time = time.time()
    print(f"Part one took {start_part_two - start_part_one:.2f} seconds")
    print(f"Part two took {end_time - start_part_two:.2f} seconds")

if __name__ == "__main__":
    # main("sample.txt")
    main("input.txt")
    # main("sample_2.txt")