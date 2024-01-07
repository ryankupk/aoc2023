DIRECTIONS = { #DIRECTIONS[<character>][0] represents entering from the left/top of the character. 
    '|': [(0, 1), (0, -1)],
    '-': [(0, 1), ("oopsy")],
    'L': [("oopsy"), (1, 1)],
    'J': [(-1, 1), ()], # index 0 represents the left, index 1 represents the top
    '7': [(1, 1), ("oopsy")],
    'F': [("oopsy"), ("")],
    '.': (None, None),
    'S': 'start'
}

def parse_input(filename: str):
    return open(filename, "r").read().splitlines()

def take_step(current_pos: tuple[int, int], dir: int, map: list[str]) -> tuple[tuple[int, int], int]:
    new_pos = ()
    
    return (new_pos, dir)

def part_one(map: list[str]) -> None:
    l = len(map)
    w = len(map[0])
    start = (-1, -1)
    for y, line in enumerate(map):
        if 'S' in line:
            start = (y, line.index('S'))
            
    first_dir = 0
    first_char = ''
    if start[0] > 0 and map[start[0] - 1][start[1]] in '|7F': # up
        first_char = map[start[0] - 1][start[1]]
        first_dir = 1
    elif start[0] < l - 1 and map[start[0] + 1][start[1]] in '|JL': # down
        first_char = map[start[0] + 1][start[1]]
        first_dir = 0
    elif start[0] > 0 and map[start[0]][start[1] - 1] in '-FL': # left
        first_char = map[start[0]][start[1] - 1]
        first_dir = 0
    elif start[0] < w - 1 and map[start[0]][start[1] + 1] in '-7J': # right
        first_char = map[start[0]][start[1] + 1]
        first_dir = 1
    else: 
        print("oopsy")
        exit(999)
        
    current_pos: tuple[int, int] = (start[0] + first_dir[0], start[1] + first_dir[1])
    step_count = 1
    while current_pos != start:
        current_pos, dir = take_step(current_pos, dir, map)
        step_count += 1
        
 
def part_two(strings: list):
    pass

def main(input_filename: str):
    inp = parse_input(input_filename)
    part_one(inp)
    part_two(inp)

if __name__ == "__main__":
    main("sample.txt")
    # main("input.txt")