import time

def parse_input(filename: str) -> list[str]:
    with open(filename) as f:
        return f.readlines()

x = 'X'
m = 'M'
a = 'A'
s = 'S'

def part_one(strings: list[str]) -> None:
    xmas_count = 0
    hi = len(strings) - 3
    hr = len(strings[0]) - 3
    for i, row in enumerate(strings):
        for j, val in enumerate(row):
            if val != x:
                continue
            # up-left
            if i >= 3 and j >= 3 and strings[i-1][j-1] == m and strings[i-2][j-2] == a and strings[i-3][j-3] == s:
                xmas_count += 1
            # up
            if i >= 3 and strings[i-1][j] == m and strings[i-2][j] == a and strings[i-3][j] == s:
                xmas_count += 1
            # up-right
            if i >= 3 and j < hr and strings[i-1][j+1] == m and strings[i-2][j+2] == a and strings[i-3][j+3] == s:
                xmas_count += 1
            # left
            if j >= 3 and strings[i][j-1] == m and strings[i][j-2] == a and strings[i][j-3] == s:
                xmas_count += 1
            # right
            if j < hr and strings[i][j+1] == m and strings[i][j+2] == a and strings[i][j+3] == s:
                xmas_count += 1
            # down-left
            if i < hi and j >= 3 and strings[i+1][j-1] == m and strings[i+2][j-2] == a and strings[i+3][j-3] == s:
                xmas_count += 1
            # down
            if i < hi and strings[i+1][j] == m and strings[i+2][j] == a and strings[i+3][j] == s:
                xmas_count += 1
            # down-right
            if i < hi and j < hr and strings[i+1][j+1] == m and strings[i+2][j+2] == a and strings[i+3][j+3] == s:
                xmas_count += 1
    
    print(xmas_count)
 
def part_two(strings: list[str]) -> None:
    mas_count = 0
    for i, row in enumerate(strings[1:-1], 1):
        for j, val in enumerate(row[1:-1], 1):
            if val != a:
                continue
            # M M
            #  A
            # S S
            if strings[i-1][j-1] == m and strings[i-1][j+1] == m and strings[i+1][j-1] == s and strings[i+1][j+1] == s:
                mas_count += 1
            # S M
            #  A
            # S M
            if strings[i-1][j-1] == s and strings[i-1][j+1] == m and strings[i+1][j-1] == s and strings[i+1][j+1] == m:
                mas_count += 1
            # M S
            #  A
            # M S
            if strings[i-1][j-1] == m and strings[i-1][j+1] == s and strings[i+1][j-1] == m and strings[i+1][j+1] == s:
                mas_count += 1
            # S S
            #  A 
            # M M
            if strings[i-1][j-1] == s and strings[i-1][j+1] == s and strings[i+1][j-1] == m and strings[i+1][j+1] == m:
                mas_count += 1

    print(mas_count)


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
    main("input.txt")
    # main("sample.txt")