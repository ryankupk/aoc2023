import time

def parse_input(filename: str) -> list[str]:
    return open(filename).read().splitlines()

def roll_rocks(rocks: list[str], direction: str) -> list[str]:
    rolled_rocks: list[str] = []
    if direction == "up":
        for i in range(len(rocks[0])):
            col = [row[i] for row in rocks]
            leftmost_available = 0
            for idx, item in enumerate(col):
                if item == '#':
                    leftmost_available = idx
                    continue
                    
    elif direction == "down":
        pass
    elif direction == "left":
        pass
    elif direction == "right":
        pass
    else:
        raise ValueError("Invalid direction")
    return rocks

def part_one(strings: list[str]) -> None:
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