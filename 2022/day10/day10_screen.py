import sys

def parse_input(filename):
    with open(filename) as f:
        return f.read().splitlines()
    
def solve_part_one(data):
    relevant_cycles = [20, 60, 100, 140, 180, 220]
    total_signal_strength = 0
    cycle = 0
    x = 1
    
    for line in data:
        if line == "noop":
            cycle += 1
            if cycle in relevant_cycles:
                total_signal_strength += cycle * x
            continue
        _, value = line.split(' ')
        cycle += 1
        if cycle in relevant_cycles:
                total_signal_strength += cycle * x
        cycle += 1
        if cycle in relevant_cycles:
                total_signal_strength += cycle * x
        x += int(value)
        
        
    return total_signal_strength

def draw_pixel(screen, cycle, x):
    pixel = (cycle - 1) % 40
    if x - 1 <= pixel < x + 2:
        screen += "#"
    else:
        screen += " "
    if cycle % 40 == 0:
        screen += '\n'
    return screen

def solve_part_two(data):
    cycle = 1
    x = 1
    screen = ""
    for line in data:
        
        if line == "noop":
            screen = draw_pixel(screen, cycle, x)
            cycle += 1
            
            continue
            
        _, value = line.split(' ')
        screen = draw_pixel(screen, cycle, x)
        cycle += 1
        
        screen = draw_pixel(screen, cycle, x)
        x += int(value)
        cycle += 1
        
    return screen



def main(filename):
    data = parse_input(filename)
    print(solve_part_one(data))
    print(solve_part_two(data))
    
if __name__ == "__main__":
    main(r"input.txt")
    
    
    
    


#### ###   ### #### #  ####### ### #  #
#    #  # #  # #  # #  # #    ## # #  ##
###  #  # #    #  ###### #### ##   #####
##   #### # ######  ## # #    #### #  ##
##   #    ## # #    ## # #    #  # #  ##
##   ##    ######   ## ####    ### #  #