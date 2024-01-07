import sys
elves = None

calories_elves = {}

def ParseInput(filename):
    global elves
    with open(filename) as f:
        elves = f.readlines()
            
    

def GetMaxElf():
    global elves
    cur_elf = 1
    for cur_calories in elves:
        if cur_calories != "" and cur_calories != '\n':
            try:
                calories_elves[cur_elf] += int(cur_calories)
            except:
                calories_elves[cur_elf] = int(cur_calories)
        else:
            cur_elf += 1
            
    print(calories_elves)
    
    max_cals = float('-inf')
    
    sorted_calories_elves = sorted(calories_elves.values())
    # return sorted_calories_elves[-1] # part 1
    return sum(sorted_calories_elves[-3:]) # part 2
        

def main(filename):
    ParseInput(filename)
    
    print(GetMaxElf())
            

if __name__ == "__main__":
    main(sys.argv[1])