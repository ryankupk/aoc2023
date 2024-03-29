import time
def parse_input(filename: str) -> list[str]:
    return open(filename, "r").read().splitlines()

def find_horizontal_reflection(strings: list[str]) -> int:
    
    return -1

def find_vertical_reflection(strings: list[str]) -> int:
    
    return -1

def part_one(strings: list[str]) -> None:
    vertical_reflection = find_vertical_reflection(strings)
    horizontal_reflection = find_horizontal_reflection(strings)
    pass

def part_two(strings: list[str]) -> None:
    pass

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
    main("sample.txt")
