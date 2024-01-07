import sys

def parse_file(filename):
    data = None
    with open(filename) as f:
        data = f.read().splitlines()
        
    return data
        
        
def solve_part_one(data):
    total_visible = (len(data) + (len(data[0]) - 2)) * 2
    
    for i, row in enumerate(data):
        # skip first and last row
        if i == 0 or i == len(data) - 1:
            continue
        for j, tree in enumerate(row):
            # skip left- and right-most columns
            if j == 0 or j == len(data) - 1:
                continue
        
            i_cpy = i - 1
            j_cpy = j
            # check top
            invisible = False
            while i_cpy > -1:
                if data[i_cpy][j_cpy] >= tree:
                    invisible = True
                    break
                else:
                    i_cpy -= 1
            if not invisible:
                
                total_visible += 1
                continue
                    
            i_cpy = i + 1
            j_cpy = j
            # check bottom
            invisible = False
            while i_cpy < len(data) :
                if data[i_cpy][j_cpy] >= tree:
                    invisible = True
                    break
                else:
                    i_cpy += 1
            if not invisible:
                
                total_visible += 1
                continue
            
            i_cpy = i
            j_cpy = j - 1
            # check left
            invisible = False
            while j_cpy > -1:
                if data[i_cpy][j_cpy] >= tree:
                    invisible = True
                    break
                else:
                    j_cpy -= 1
            if not invisible:
                
                total_visible += 1
                continue
            
            i_cpy = i
            j_cpy = j + 1
            # check right
            invisible = False
            while j_cpy < len(data) :
                if data[i_cpy][j_cpy] >= tree:
                    invisible = True
                    break
                else:
                    j_cpy += 1
            if not invisible:
                
                total_visible += 1
                continue
            
    return total_visible


def solve_part_two(data):
    max_scenic = float('-inf')
    
    for i, row in enumerate(data):
        if i == 0 or i == len(data) - 1:
            continue
        for j, tree in enumerate(row):
            if j == 0 or j == len(data) - 1:
                continue
                
            current_scenic_u = 0
            current_scenic_r = 0
            current_scenic_d = 0
            current_scenic_l = 0
            i_cpy = i - 1
            j_cpy = j
            # check top
            while i_cpy > -1:
                if data[i_cpy][j_cpy] >= tree:
                    current_scenic_u += 1
                    break
                else:
                    i_cpy -= 1
                    current_scenic_u += 1
            
                    
            i_cpy = i + 1
            j_cpy = j
            # check bottom
            while i_cpy < len(data) :
                if data[i_cpy][j_cpy] >= tree:
                    current_scenic_d += 1
                    break
                else:
                    i_cpy += 1
                    current_scenic_d += 1
            
            
            i_cpy = i
            j_cpy = j - 1
            # check left
            while j_cpy > -1:
                if data[i_cpy][j_cpy] >= tree:
                    current_scenic_l += 1
                    break
                else:
                    j_cpy -= 1
                    current_scenic_l += 1
            
            
            i_cpy = i
            j_cpy = j + 1
            # check right
            while j_cpy < len(data) :
                if data[i_cpy][j_cpy] >= tree:
                    current_scenic_r += 1
                    break
                else:
                    j_cpy += 1
                    current_scenic_r += 1
            
            
            max_scenic = max(max_scenic, current_scenic_r * current_scenic_l * current_scenic_d * current_scenic_u)
            
    return max_scenic



def main(filename):
    data = parse_file(filename)
    print(solve_part_one(data))
    print(solve_part_two(data))
    
if __name__ == "__main__":
    main(sys.argv[1])