import time
from collections import Counter

STRENGTHS = {
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    'T': 10,
    'J': 1, # set to 11 for part 1, or 1 for part 2
    'Q': 12,
    'K': 13,
    'A': 14
}

def parse_input(filename: str):
    return open(filename, "r").read().splitlines()

# return True if lhand is higher rank than rhand else False
def higher_rank(lhand: str, rhand: str, joker: bool) -> bool:
    lhand_count = Counter(lhand)
    if 'J' in lhand and joker:
        # add to the highest non-J count
        for letter, _ in sorted(sorted(lhand_count.items(), key=lambda x: -STRENGTHS[x[0]]), key=lambda x: -x[1]):
            if letter != 'J':
                lhand_count[letter] += lhand_count['J']
                del lhand_count['J']
                break
    max_lhand_count = max(lhand_count.values())
    rhand_count = Counter(rhand)
    if 'J' in rhand and joker:
        for letter, _ in sorted(sorted(rhand_count.items(), key=lambda x: -STRENGTHS[x[0]]), key=lambda x: -x[1]):
            if letter != 'J':
                rhand_count[letter] += rhand_count['J']
                del rhand_count['J']
                break
    max_rhand_count = max(rhand_count.values())
    
    
    if max_lhand_count != max_rhand_count: # if one hand beats another, return it directly
        return max_lhand_count > max_rhand_count
    
    # check full house vs 3 of a kind
    if max_lhand_count == max_rhand_count == 3:
        if min(lhand_count.values()) > min(rhand_count.values()):
            return True
        elif min(lhand_count.values()) < min(rhand_count.values()):
            return False
        # there is an implicit third condition to do nothing if these counts are equal
        # therefore we cannot return min(lhand_count.values()) > min(rhand_count.values())
    
    # check two pair
    if max_lhand_count == max_rhand_count == 2:
        if len(lhand_count) == 3 and len(rhand_count) != 3: # 2 pair would result in length of 3
            return True
        elif len(lhand_count) == len(rhand_count):
            pass
        else:
            return False
         
    # break the tie
    for lcard, rcard in zip(lhand, rhand):
        if STRENGTHS[lcard] < STRENGTHS[rcard]:
            return False
        if STRENGTHS[lcard] > STRENGTHS[rcard]:
            return True
    else: return False
    
def calculate_winnings(strings: list[str], joker: bool) -> int:
    hands_bids = {}
    ordered_hands = []
    for string in strings:
        cur_hand, bid = string.split(' ')
        hands_bids[cur_hand] = int(bid)
        for idx, existing_hand in enumerate(ordered_hands):
            if (higher_rank(cur_hand, existing_hand, joker)):
                ordered_hands.insert(idx, cur_hand)
                break
        else:
            ordered_hands.append(cur_hand)
    total_winnings = 0
    total_len = len(ordered_hands)
    for idx, hand in enumerate(ordered_hands):
        rank = total_len - idx
        total_winnings += hands_bids[hand] * rank
        
    return total_winnings
    
def part_one(strings: list[str]) -> None:
    total_winnings = calculate_winnings(strings, False)
    print(total_winnings)
 
def part_two(strings: list[str]) -> None:
    total_winnings = calculate_winnings(strings, True)
    print(total_winnings)

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
