from collections import defaultdict
import heapq
import time

def parse_input(filename: str) -> list[str]:
    with open(filename) as f:
        rows = [line.split() for line in f.readlines()]
        return rows

def part_one(strings: list[str]) -> None:
    left, right = [], []
    for row in strings:
        heapq.heappush(left, int(row[0]))
        heapq.heappush(right, int(row[1]))
    res = 0
    while len(left) > 0:
        a, b = heapq.heappop(left), heapq.heappop(right)
        res += (abs(a-b))

    print(res)
 
def part_two(strings: list[str]) -> None:
    left = []
    right_counts = defaultdict(int)
    for row in strings:
        left_num, right_num = int(row[0]), int(row[1])
        left.append(left_num)
        right_counts[right_num] += 1
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
    print(f"Part one took {start_part_two - start_part_one:.2f} seconds")
    print(f"Part two took {end_time - start_part_two:.2f} seconds")

if __name__ == "__main__":
    # main("sample.txt")
    main("input.txt")