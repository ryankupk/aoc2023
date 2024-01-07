import sys

def parse_data(filename):
    data = None
    with open(filename) as f:
        data = f.read().splitlines()
        
    return data

def move_rope(direction, head, tail, head_move):
    moves = {
        "U": (0,1),
        "D": (0,-1),
        "L": (-1,0),
        "R": (1,0)
    }
    if head == tail and head_move:
        head = (head[0] + moves[direction][0], head[1] + moves[direction][1])
        return head, tail
    elif head == tail and not head_move:
        return head, tail
    if head_move:
        head = (head[0] + moves[direction][0], head[1] + moves[direction][1])
        # check if tail should move
        if abs(head[0] - tail[0]) == 2 or abs(head[1] - tail[1]) == 2:
            # tail moves
            # axis-aligned movement
            if head[0] == tail[0] or head[1] == tail[1]:
                tail = (tail[0] + moves[direction][0], tail[1] + moves[direction][1])
            # diagonal movement
            else:
                # up-right
                if head[0] > tail[0] and head[1] > tail[1]:
                    tail = (tail[0] + moves["U"][0], tail[1] + moves["U"][1])
                    tail = (tail[0] + moves["R"][0], tail[1] + moves["R"][1])
                # down-right
                if head[0] > tail[0] and head[1] < tail[1]:
                    tail = (tail[0] + moves["D"][0], tail[1] + moves["D"][1])
                    tail = (tail[0] + moves["R"][0], tail[1] + moves["R"][1])
                # up-left
                if head[0] < tail[0] and head[1] > tail[1]:
                    tail = (tail[0] + moves["U"][0], tail[1] + moves["U"][1])
                    tail = (tail[0] + moves["L"][0], tail[1] + moves["L"][1])
                # down-left
                if head[0] < tail[0] and head[1] < tail[1]:
                    tail = (tail[0] + moves["D"][0], tail[1] + moves["D"][1])
                    tail = (tail[0] + moves["L"][0], tail[1] + moves["L"][1])
    else:
        # check if tail should move
        if abs(head[0] - tail[0]) == 2 or abs(head[1] - tail[1]) == 2:
            # tail moves
            
            # axis-aligned movement
            if head[0] == tail[0] or head[1] == tail[1]:
                # find direction to head
                new_dir = [0,0]
                if head[0] - tail[0] == 2: new_dir[0] = 1
                elif head[0]-tail[0] == -2:new_dir[0] = -1
                if head[1] - tail[1] == 2: new_dir[1] = 1
                elif head[1]-tail[1] == -2:new_dir[1] = -1
                tail = (tail[0] + new_dir[0], tail[1] + new_dir[1])
            # diagonal movement
            else:
                # up-right
                if head[0] > tail[0] and head[1] > tail[1]:
                    tail = (tail[0] + moves["U"][0], tail[1] + moves["U"][1])
                    tail = (tail[0] + moves["R"][0], tail[1] + moves["R"][1])
                # down-right
                if head[0] > tail[0] and head[1] < tail[1]:
                    tail = (tail[0] + moves["D"][0], tail[1] + moves["D"][1])
                    tail = (tail[0] + moves["R"][0], tail[1] + moves["R"][1])
                # up-left
                if head[0] < tail[0] and head[1] > tail[1]:
                    tail = (tail[0] + moves["U"][0], tail[1] + moves["U"][1])
                    tail = (tail[0] + moves["L"][0], tail[1] + moves["L"][1])
                # down-left
                if head[0] < tail[0] and head[1] < tail[1]:
                    tail = (tail[0] + moves["D"][0], tail[1] + moves["D"][1])
                    tail = (tail[0] + moves["L"][0], tail[1] + moves["L"][1])
                    
    return head, tail
                    
        
        

def solve_part_one(data):
    visited_points = set()
    visited_points.add((0,0))
    head = (0,0)
    tail = (0,0)
    for instruction in data:
        direction, distance = instruction.split(' ')
        for _ in range(int(distance)):
            head, tail = move_rope(direction, head, tail, True)
            visited_points.add(tail)
                
    return len(visited_points)
    

def solve_part_two(data):
    visited_points = set()
    visited_points.add((0,0))
    head = (0,0)
    tail_list = [(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0)]
    for instruction in data:
        direction, distance = instruction.split(' ')
        for _ in range(int(distance)):
            head, tail_list[0] = move_rope(direction, head, tail_list[0], True)
            for idx, tail_part in enumerate(tail_list):
                if idx == 0: continue # first tail segment was moved already, skip it
                tail_list[idx-1], tail_list[idx] = move_rope(direction, tail_list[idx-1], tail_list[idx], False)
                visited_points.add(tail_list[-1])
                
    return len(visited_points)

def main(filename):
    data = parse_data(filename)
    
    print(solve_part_one(data))
    print(solve_part_two(data))
    
    
if __name__ == "__main__":
    main(r"input.txt")