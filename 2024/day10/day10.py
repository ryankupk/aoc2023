import time

def parse_input(filename: str) -> list[str]:
    with open(filename) as f:
        return [line.strip() for line in f.readlines()]

def dfs(start, strings, visited):
    stack = []

    def push_next_to_stack(start, strings, stack, visited):
        dirs = [(1, 0), (-1, 0), (0, -1), (0, 1)]

        for dir in dirs:
            cur_dir = (start[0] + dir[0], start[1] + dir[1])
            if cur_dir[0] < 0 or cur_dir[0] >= len(strings) or cur_dir[1] < 0 or cur_dir[1] >= len(strings[0]):
                continue
            if visited is None or (visited is not None and cur_dir not in visited):
                if strings[cur_dir[0]][cur_dir[1]] == str(int(strings[start[0]][start[1]]) + 1):
                    stack.append(cur_dir)
                continue
        
    push_next_to_stack(start, strings, stack, visited)

    count = 0
    while len(stack) > 0:
        next_elem = stack.pop()
        if strings[next_elem[0]][next_elem[1]] == '9':
            count += 1
        if visited is not None:
            visited.add(next_elem)
        push_next_to_stack(next_elem, strings, stack, visited)
    
    return count


def part_one(strings: list[str]) -> list[tuple[int, int]]:
    zeroes = [(i, j) for i, string in enumerate(strings) for j, letter in enumerate(string) if letter == '0']
    count = 0

    visited = set()
    for zero in zeroes:
        count += dfs(zero, strings, visited)
        visited = set()

    print(count)
    return zeroes
 
def part_two(strings: list[str], zeroes: list[tuple[int, int]]) -> None:
    count = 0

    for zero in zeroes:
        count += dfs(zero, strings, None)

    print(count)

def main(input_filename: str):
    inp = parse_input(input_filename)
    start_part_one = time.time()
    zeroes = part_one(inp)
    start_part_two = time.time()
    part_two(inp, zeroes)
    end_time = time.time()
    print(f"Part one took {start_part_two - start_part_one:.2f} seconds")
    print(f"Part two took {end_time - start_part_two:.2f} seconds")

if __name__ == "__main__":
    main("input.txt")