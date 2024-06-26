import time
SYMBOLS = r'%@#-=+&$/*'
COL_LEN = None
ROW_LEN = None

def parse_input(filename: str) -> list[str]:
    return open(filename,"r").read().splitlines()

# def build_string_left()

def find_adjacent_nums(symbol_x: int, symbol_y: int, strings: list[str]) -> int:
    current_nums = []
    skip_up = False
    skip_up_right = False
    skip_down = False
    skip_down_right = False
    
    x_offs = range(-1, 1)
    y_offs = range(-1, 1)
    
    for x_off in x_offs:
        for y_off in y_offs:
            if symbol_x - x_off >= 0 and symbol_y - y_off >= 0 and\
                strings[symbol_y - y_off][symbol_x - x_off].isdigit():
                    
    
                if symbol_x - 1 >= 0 and symbol_y - 1 >= 0 and\
                    strings[symbol_y - 1][symbol_x - 1].isdigit():
                        
                    current_num = ''
                    temp_x = symbol_x - 1
                    
                    while temp_x >= 0 and strings[symbol_y - 1][temp_x].isdigit():
                        current_num += strings[symbol_y - 1][temp_x]
                        temp_x -= 1
                    temp_x = symbol_x
                    current_num = current_num[::-1]
                    
                    while temp_x < ROW_LEN and strings[symbol_y - 1][temp_x].isdigit():
                        if skip_up:
                            skip_up_right = True
                        current_num += strings[symbol_y - 1][temp_x]
                        temp_x += 1
                        skip_up = True

                    current_nums.append(int(current_num))
                        
                if symbol_y - 1 >= 0 and\
                    not skip_up and\
                    strings[symbol_y - 1][symbol_x].isdigit():
                    
                    current_num = ''
                    temp_x = symbol_x
                    while temp_x < ROW_LEN and strings[symbol_y - 1][temp_x].isdigit():
                        current_num += strings[symbol_y - 1][temp_x]
                        temp_x += 1
                        skip_up_right = True

                    current_nums.append(int(current_num))
                    
                if symbol_x + 1 < ROW_LEN and symbol_y - 1 >= 0 and\
                    not skip_up_right and\
                    strings[symbol_y - 1][symbol_x + 1].isdigit():

                    current_num = ''
                    temp_x = symbol_x + 1
                    while temp_x < ROW_LEN and strings[symbol_y - 1][temp_x].isdigit():
                        current_num += strings[symbol_y - 1][temp_x]
                        temp_x += 1
                    current_nums.append(int(current_num))
                
                if symbol_x - 1 >= 0 and\
                    strings[symbol_y][symbol_x - 1].isdigit():
                    current_num = ''
                    temp_x = symbol_x - 1
                    while temp_x >= 0 and strings[symbol_y][temp_x].isdigit():
                        current_num += strings[symbol_y][temp_x]
                        temp_x -= 1
                    current_nums.append(int(current_num[::-1]))
                    
                if symbol_x + 1 < ROW_LEN and\
                    strings[symbol_y][symbol_x + 1].isdigit():
                    current_num = ''
                    temp_x = symbol_x + 1
                    while temp_x < ROW_LEN and strings[symbol_y][temp_x].isdigit():
                        current_num += strings[symbol_y][temp_x]
                        temp_x += 1
                    current_nums.append(int(current_num))
                
                if symbol_x - 1 >= 0 and symbol_y + 1 < COL_LEN and\
                    strings[symbol_y + 1][symbol_x - 1].isdigit():
                    current_num = ''
                    temp_x = symbol_x - 1
                    while temp_x >= 0 and strings[symbol_y + 1][temp_x].isdigit():
                        current_num += strings[symbol_y + 1][temp_x]
                        temp_x -= 1
                    temp_x = symbol_x
                    current_num = current_num[::-1]
                    
                    while temp_x < ROW_LEN and strings[symbol_y + 1][temp_x].isdigit():
                        if skip_down:
                            skip_down_right = True
                        current_num += strings[symbol_y + 1][temp_x]
                        temp_x += 1
                        skip_down = True

                    current_nums.append(int(current_num))
                
                if symbol_y + 1 < COL_LEN and\
                    not skip_down and\
                    strings[symbol_y + 1][symbol_x].isdigit():
                    
                    current_num = ''
                    temp_x = symbol_x
                    while temp_x < ROW_LEN and strings[symbol_y + 1][temp_x].isdigit():
                        current_num += strings[symbol_y + 1][temp_x]
                        temp_x += 1
                        skip_down_right = True

                    current_nums.append(int(current_num))
                
                if symbol_x + 1 < ROW_LEN and symbol_y + 1 < COL_LEN and\
                    not skip_down_right and\
                    strings[symbol_y + 1][symbol_x + 1].isdigit():

                    current_num = ''
                    temp_x = symbol_x + 1
                    while temp_x < ROW_LEN and strings[symbol_y + 1][temp_x].isdigit():
                        current_num += strings[symbol_y + 1][temp_x]
                        temp_x += 1
                    current_nums.append(int(current_num))
    
    return sum(current_nums)

def find_adjacent_nums_gears(symbol_x: int, symbol_y: int, strings: list[str]) -> int:
    current_nums = []
    skip_up = False
    skip_up_right = False
    skip_down = False
    skip_down_right = False
    
    if symbol_x - 1 >= 0 and symbol_y - 1 >= 0 and\
        strings[symbol_y - 1][symbol_x - 1].isdigit():
            
        current_num = ''
        temp_x = symbol_x - 1
        
        while temp_x >= 0 and strings[symbol_y - 1][temp_x].isdigit():
            current_num += strings[symbol_y - 1][temp_x]
            temp_x -= 1
        temp_x = symbol_x
        current_num = current_num[::-1]
        
        while temp_x < ROW_LEN and strings[symbol_y - 1][temp_x].isdigit():
            if skip_up:
                skip_up_right = True
            current_num += strings[symbol_y - 1][temp_x]
            temp_x += 1
            skip_up = True

        current_nums.append(int(current_num))
            
    if symbol_y - 1 >= 0 and\
        not skip_up and\
        strings[symbol_y - 1][symbol_x].isdigit():
        
        current_num = ''
        temp_x = symbol_x
        while temp_x < ROW_LEN and strings[symbol_y - 1][temp_x].isdigit():
            current_num += strings[symbol_y - 1][temp_x]
            temp_x += 1
            skip_up_right = True

        current_nums.append(int(current_num))
        
    if symbol_x + 1 < ROW_LEN and symbol_y - 1 >= 0 and\
        not skip_up_right and\
        strings[symbol_y - 1][symbol_x + 1].isdigit():

        current_num = ''
        temp_x = symbol_x + 1
        while temp_x < ROW_LEN and strings[symbol_y - 1][temp_x].isdigit():
            current_num += strings[symbol_y - 1][temp_x]
            temp_x += 1
        current_nums.append(int(current_num))
    
    if symbol_x - 1 >= 0 and\
        strings[symbol_y][symbol_x - 1].isdigit():
        current_num = ''
        temp_x = symbol_x - 1
        while temp_x >= 0 and strings[symbol_y][temp_x].isdigit():
            current_num += strings[symbol_y][temp_x]
            temp_x -= 1
        current_nums.append(int(current_num[::-1]))
        
    if symbol_x + 1 < ROW_LEN and\
        strings[symbol_y][symbol_x + 1].isdigit():
        current_num = ''
        temp_x = symbol_x + 1
        while temp_x < ROW_LEN and strings[symbol_y][temp_x].isdigit():
            current_num += strings[symbol_y][temp_x]
            temp_x += 1
        current_nums.append(int(current_num))
    
    if symbol_x - 1 >= 0 and symbol_y + 1 < COL_LEN and\
        strings[symbol_y + 1][symbol_x - 1].isdigit():
        current_num = ''
        temp_x = symbol_x - 1
        while temp_x >= 0 and strings[symbol_y + 1][temp_x].isdigit():
            current_num += strings[symbol_y + 1][temp_x]
            temp_x -= 1
        temp_x = symbol_x
        current_num = current_num[::-1]
        
        while temp_x < ROW_LEN and strings[symbol_y + 1][temp_x].isdigit():
            if skip_down:
                skip_down_right = True
            current_num += strings[symbol_y + 1][temp_x]
            temp_x += 1
            skip_down = True

        current_nums.append(int(current_num))
    
    if symbol_y + 1 < COL_LEN and\
        not skip_down and\
        strings[symbol_y + 1][symbol_x].isdigit():
        
        current_num = ''
        temp_x = symbol_x
        while temp_x < ROW_LEN and strings[symbol_y + 1][temp_x].isdigit():
            current_num += strings[symbol_y + 1][temp_x]
            temp_x += 1
            skip_down_right = True

        current_nums.append(int(current_num))
    
    if symbol_x + 1 < ROW_LEN and symbol_y + 1 < COL_LEN and\
        not skip_down_right and\
        strings[symbol_y + 1][symbol_x + 1].isdigit():

        current_num = ''
        temp_x = symbol_x + 1
        while temp_x < ROW_LEN and strings[symbol_y + 1][temp_x].isdigit():
            current_num += strings[symbol_y + 1][temp_x]
            temp_x += 1
        current_nums.append(int(current_num))
    
    if len(current_nums) == 2:
        return current_nums[0] * current_nums[1]
    else: return 0


def part_one(strings: list[str]) -> None:
    global COL_LEN
    COL_LEN = len(strings)
    global ROW_LEN
    ROW_LEN = len(strings[0])
    
    parts_total = 0
    for y, line in enumerate(strings):
        for x, char in enumerate(line):
            if char not in SYMBOLS: continue

            parts_total += find_adjacent_nums(x, y, strings)
            
    print(parts_total)
                
def part_two(strings: list[str]) -> None:
    ratio_total = 0
    for y, line in enumerate(strings):
        for x, char in enumerate(line):
            if char != '*': continue

            ratio_total += find_adjacent_nums_gears(x, y, strings)
            
    print(ratio_total)

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
    main("input.txt")
