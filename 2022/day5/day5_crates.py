import sys

def ParseData(filename):
    with open(filename) as f:
        data = f.read().splitlines()
        
        crates = data[:9]
        procedure = data[10:]
        return crates, procedure
    
def CreateCrateDict(crates):
    # each set of 4 chars is the crate for that column
    # map the second, sixth, tenth etc char to the column for that crate
    
    crate_dict = {i: [] for i in range(1, 10)}
    
    for i in range(1, 10):
        if crates[i-1][2] != ' ':
            crate_dict[1].append(crates[i-1][1])
        if crates[i-1][6] != ' ':
            crate_dict[2].append(crates[i-1][5])
        if crates[i-1][10] != ' ':
            crate_dict[3].append(crates[i-1][9])
        if crates[i-1][14] != ' ':
            crate_dict[4].append(crates[i-1][13])
        if crates[i-1][18] != ' ':
            crate_dict[5].append(crates[i-1][17])
        if crates[i-1][22] != ' ':
            crate_dict[6].append(crates[i-1][21])
        if crates[i-1][26] != ' ':
            crate_dict[7].append(crates[i-1][25])
        if crates[i-1][30] != ' ':
            crate_dict[8].append(crates[i-1][29])
        if crates[i-1][34] != ' ':
            crate_dict[9].append(crates[i-1][33])
            
    for key, val in crate_dict.items():
        crate_dict[key] = list(reversed(val))
    print(crate_dict)
    return crate_dict
        

def MoveCratesOne(crates, move):
    for _ in range(move[0]):
        crates[move[2]].append(crates[move[1]].pop())
    return crates


def MoveCratesTwo(crates, move):
    crates[move[2]] = crates[move[2]] + crates[move[1]][move[0] * -1:]
    for _ in range(move[0]):
        crates[move[1]].pop()
    return crates

def PartOne(crates_raw, procedure):
    ret = ""
    crates = CreateCrateDict(crates_raw)
    for move in procedure:
        crates = MoveCratesOne(crates, (int(move.split()[1]), int(move.split()[3]), int(move.split()[5])))
    for crate in crates.values():
        ret += crate.pop()
        
    print(ret)

def PartTwo(crates_raw, procedure):
    ret = ""
    crates = CreateCrateDict(crates_raw)
    for move in procedure:
        crates = MoveCratesTwo(crates, (int(move.split()[1]), int(move.split()[3]), int(move.split()[5])))
    
    for crate in crates.values():
        ret += crate.pop()
        
    print(ret)

def main(filename):
    
    crates_raw, procedure = ParseData(filename)
    
    PartOne(crates_raw, procedure)
    PartTwo(crates_raw, procedure)
    
if __name__ == "__main__":
    main(r".\input.txt")