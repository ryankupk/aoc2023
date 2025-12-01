import time

def parse_input(filename: str) -> list[str]:
    with open(filename) as f:
        return f.readlines()

def part_one(strings: list[str]) -> None:
    start = 50
    res = 0
    for turn in strings:
        if turn[0] == 'L':
            start -= int(turn[1:]) 
            start %= 100
        elif turn[0] == 'R':
            start += int(turn[1:]) 
            start %= 100
        if start == 0:
            res += 1
    print(f"{res=}")

 
def part_two(strings: list[str]) -> None:
    start = 50
    res = 0
    for turn in strings:
        if turn[0] == 'L':
            turn_amount = int(turn[1:])
            if turn_amount > 100:
                spins = turn_amount // 100
                res += spins
                turn_amount = int(turn[2:])
            if turn_amount >= start:
                res += 1
            start -= turn_amount
            start %= 100
        elif turn[0] == 'R':
            turn_amount = int(turn[1:])
            if turn_amount > 100:
                spins = turn_amount // 100
                res += spins
                turn_amount = int(turn[2:])
            if turn_amount + start >= 100:
                res += 1
            start += turn_amount
            start %= 100
    print(f"{res=}")

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
    main("sample.txt")
    # main("input.txt")