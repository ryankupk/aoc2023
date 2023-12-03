INTS = '1234567890'
SYMBOLS = r'%@#-=+&$/*'
COL_LEN = None
ROW_LEN = None

def parse_input(filename: str):
    return open(filename,"r").read().splitlines()

def find_adjacent_nums(symbol_x: int, symbol_y: int, strings: list):
    current_nums = []
    skip_up = False
    skip_up_right = False
    skip_down = False
    skip_down_right = False
    
    if symbol_x - 1 >= 0 and symbol_y - 1 >= 0 and\
        strings[symbol_y - 1][symbol_x - 1] in INTS:
            
        current_num = ''
        temp_x = symbol_x - 1
        
        while temp_x >= 0 and strings[symbol_y - 1][temp_x] in INTS:
            current_num += strings[symbol_y - 1][temp_x]
            temp_x -= 1
        temp_x = symbol_x
        current_num = current_num[::-1]
        
        while temp_x < ROW_LEN and strings[symbol_y - 1][temp_x] in INTS:
            if skip_up:
                skip_up_right = True
            current_num += strings[symbol_y - 1][temp_x]
            temp_x += 1
            skip_up = True

        current_nums.append(int(current_num))
            
    if symbol_y - 1 >= 0 and\
        not skip_up and\
        strings[symbol_y - 1][symbol_x] in INTS:
        
        current_num = ''
        temp_x = symbol_x
        while temp_x < ROW_LEN and strings[symbol_y - 1][temp_x] in INTS:
            current_num += strings[symbol_y - 1][temp_x]
            temp_x += 1
            skip_up_right = True

        current_nums.append(int(current_num))
        
    if symbol_x + 1 < ROW_LEN and symbol_y - 1 >= 0 and\
        not skip_up_right and\
        strings[symbol_y - 1][symbol_x + 1] in INTS:

        current_num = ''
        temp_x = symbol_x + 1
        while temp_x < ROW_LEN and strings[symbol_y - 1][temp_x] in INTS:
            current_num += strings[symbol_y - 1][temp_x]
            temp_x += 1
        current_nums.append(int(current_num))
    
    if symbol_x - 1 >= 0 and\
        strings[symbol_y][symbol_x - 1] in INTS:
        current_num = ''
        temp_x = symbol_x - 1
        while temp_x >= 0 and strings[symbol_y][temp_x] in INTS:
            current_num += strings[symbol_y][temp_x]
            temp_x -= 1
        current_nums.append(int(current_num[::-1]))
        
    if symbol_x + 1 < ROW_LEN and\
        strings[symbol_y][symbol_x + 1] in INTS:
        current_num = ''
        temp_x = symbol_x + 1
        while temp_x < ROW_LEN and strings[symbol_y][temp_x] in INTS:
            current_num += strings[symbol_y][temp_x]
            temp_x += 1
        current_nums.append(int(current_num))
    
    if symbol_x - 1 >= 0 and symbol_y + 1 < COL_LEN and\
        strings[symbol_y + 1][symbol_x - 1] in INTS:
        current_num = ''
        temp_x = symbol_x - 1
        while temp_x >= 0 and strings[symbol_y + 1][temp_x] in INTS:
            current_num += strings[symbol_y + 1][temp_x]
            temp_x -= 1
        temp_x = symbol_x
        current_num = current_num[::-1]
        
        while temp_x < ROW_LEN and strings[symbol_y + 1][temp_x] in INTS:
            if skip_down:
                skip_down_right = True
            current_num += strings[symbol_y + 1][temp_x]
            temp_x += 1
            skip_down = True

        current_nums.append(int(current_num))
    
    if symbol_y + 1 < COL_LEN and\
        not skip_down and\
        strings[symbol_y + 1][symbol_x] in INTS:
        
        current_num = ''
        temp_x = symbol_x
        while temp_x < ROW_LEN and strings[symbol_y + 1][temp_x] in INTS:
            current_num += strings[symbol_y + 1][temp_x]
            temp_x += 1
            skip_down_right = True

        current_nums.append(int(current_num))
    
    if symbol_x + 1 < ROW_LEN and symbol_y + 1 < COL_LEN and\
        not skip_down_right and\
        strings[symbol_y + 1][symbol_x + 1] in INTS:

        current_num = ''
        temp_x = symbol_x + 1
        while temp_x < ROW_LEN and strings[symbol_y + 1][temp_x] in INTS:
            current_num += strings[symbol_y + 1][temp_x]
            temp_x += 1
        current_nums.append(int(current_num))
    
    return sum(current_nums)

def part_one(strings: list):
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
                
                
 
def part_two(strings: list):
    pass

def main(input_filename: str):
    inp = parse_input(input_filename)
    part_one(inp)
    part_two(inp)

if __name__ == "__main__":
    main("input.txt")