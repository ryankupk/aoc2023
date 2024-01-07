import sys

def ParseInput(filename):
    with open(filename) as f:
        lines = f.read().splitlines()
        
    return lines

def ParseAssignments(assignment):
    assignment1, assignment2 = assignment.split(',')
    assignment1 = [int(x) for x in assignment1.split('-')]
    assignment2 = [int(x) for x in assignment2.split('-')]
    
    return assignment1, assignment2

def PartOne(data):
    total_with_complete_overlap = 0
    for assignment in data:
        first, second = ParseAssignments(assignment)
        if ((first[0] >= second[0] and first[1] <= second[1]) or (second[0] >= first[0] and second[1] <= first[1])):
            total_with_complete_overlap += 1
            continue
            
    return total_with_complete_overlap

def PartTwo(data):
    total_with_any_overlap = 0
    for assignment in data:
        first, second = ParseAssignments(assignment)
        if (second[0] <= first[0] <= second[1]) or (first[0] <= second[0] <= first[1]):
            total_with_any_overlap += 1
    
    return total_with_any_overlap

def main(filename):
    data = ParseInput(filename)
    print(PartOne(data))
    
    print(PartTwo(data))


if __name__ == "__main__":
    main(sys.argv[1])