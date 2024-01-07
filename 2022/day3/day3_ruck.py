import sys
from math import floor

def ParseInput(filename):
    sacks = None
    with open(filename) as f:
        sacks = f.read().splitlines()
        
    return sacks


def LetterToPriority(letter):
    return ord(letter) - 64 + 26 if letter.isupper() else ord(letter) - 64 - 32

def CalculatePriority(sack):
    half_sack = floor(len(sack)/2)
    sack1 = sack[:half_sack]
    sack2 = sack[half_sack:]
    not_allowed = []
    
    sack_priority = 0
    
    for letter in sack1:
        if letter in sack2 and letter not in not_allowed:
            sack_priority += LetterToPriority(letter)
            not_allowed.append(letter)
        
    
    
    return sack_priority


def FindGroups(sacks):
    
    not_allowed = []
    potential = []
    for letter in sacks[0]:
        if letter in sacks[1] and letter not in not_allowed:
            potential.append(letter)
        else:
            not_allowed.append(letter)
            
    for letter in potential:
        if letter in sacks[2] and letter not in not_allowed:
            return letter
            
    
    
    print(sacks)
    potential = list(set(sacks[0]))
    potential_copy = [letter for letter in potential]
    
    for letter in potential:
        if letter not in sacks[1]:
            # print(letter)
            potential_copy.remove(letter)
    print(potential)
    potential = potential_copy
    potential_copy = [letter for letter in potential]
    for letter in potential:
        if letter not in sacks[2]:
            # print(letter)
            potential_copy.remove(letter)
    print(potential)
    return potential[0]


def main(filename):
    sacks = ParseInput(filename)
    total_priority = 0
    for sack in sacks:
        total_priority += CalculatePriority(sack)
        
    group = []
    total_group_priority = 0
    for idx, sack in enumerate(sacks):
        if idx % 3 != 0 or idx == 0:
            group.append(sack)
        else:
            
            total_group_priority += LetterToPriority(FindGroups(group))
            group = [sack]
            
    total_group_priority += LetterToPriority(FindGroups([sack for sack in sacks[-3:]]))
        
    print(total_priority)
    print(total_group_priority)
    

if __name__ == "__main__":
    main(sys.argv[1])