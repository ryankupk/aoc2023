import sys

plays = []
scores = {
    "A": 1,
    "B": 2,
    "C": 3,
    "X": 1,
    "Y": 2,
    "Z": 3,
    "loss": 0,
    "draw": 3,
    "win": 6
}

def ParseInput(filename):
    global plays
    with open(filename) as f:
        plays = f.readlines()

def CalculateScorePart1(play1, play2):
    current_score = 0
    result = None
    
    current_score += scores[play2]
    
    if play1 == "A" and play2 == "X":
        result = "draw"
    elif play1 == "A" and play2 == "Y":
        result = "win"
    elif play1 == "A" and play2 == "Z":
        result = "loss"
    elif play1 == "B" and play2 == "X":
        result = "loss"
    elif play1 == "B" and play2 == "Y":
        result = "draw"
    elif play1 == "B" and play2 == "Z":
        result = "win"
    elif play1 == "C" and play2 == "X":
        result = "win"
    elif play1 == "C" and play2 == "Y":
        result = "loss"
    elif play1 == "C" and play2 == "Z": 
        result = "draw"
    else:
        result = "wtf"
        print(f"play1={play1}", f"play2={play2}", f"{len(play1)}", f"{len(play2)}")
    
    return current_score + scores[result]


def CalculateScorePart2(play1, play2):
    current_score = 0
    result = None
    
    # current_score += scores[play2]
    
    if play1 == "A" and play2 == "X":
        current_score += scores["C"]
        result = "loss"
    elif play1 == "A" and play2 == "Y":
        current_score += scores["A"]
        result = "draw"
    elif play1 == "A" and play2 == "Z":
        current_score += scores["B"]
        result = "win"
        
    elif play1 == "B" and play2 == "X":
        current_score += scores["A"]
        result = "loss"
    elif play1 == "B" and play2 == "Y":
        current_score += scores["B"]
        result = "draw"
    elif play1 == "B" and play2 == "Z":
        current_score += scores["C"]
        result = "win"
        
    elif play1 == "C" and play2 == "X":
        current_score += scores["B"]
        result = "loss"
    elif play1 == "C" and play2 == "Y":
        current_score += scores["C"]
        result = "draw"
    elif play1 == "C" and play2 == "Z":
        current_score += scores["A"] 
        result = "win"
    else:
        result = "wtf"
        print(f"play1={play1}", f"play2={play2}", f"{len(play1)}", f"{len(play2)}")
    
    
    current_score += scores[result]
    return current_score


def main(filename):
    global plays
    ParseInput(filename)
    total_score = 0
    for play in plays:
        play1, play2 = play.split(' ')
        total_score += CalculateScorePart2(play1, play2.strip())
        
    print(total_score)

if __name__ == "__main__":
    main(sys.argv[1])