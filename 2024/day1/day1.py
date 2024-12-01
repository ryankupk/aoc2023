from collections import Counter
import time

def parse_input(filename: str) -> list[str]:
    with open(filename) as f:
        rows = [line.split() for line in f.readlines()]
        return rows

def part_one(strings: list[str]) -> None:
    left = []
    right = []
    for row in strings:
        left.append(int(row[0]))
        right.append(int(row[1]))
    left.sort()
    right.sort()
    res = []
    for a, b in zip(left, right):
        res.append(abs(a-b))

    print(sum(res))
 
def part_two(strings: list[str]) -> None:
    left = []
    right = []
    for row in strings:
        left.append(int(row[0]))
        right.append(int(row[1]))
    right_counts = Counter(right)
    res = 0
    for left_num in left:
        res += (left_num * right_counts[left_num])

    print(res)


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
    # main("sample.txt")
    main("input.txt")