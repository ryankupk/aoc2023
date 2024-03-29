import time
def parse_input(filename: str):
    return [list(map(int, string.split(' '))) for string in open(filename, "r").read().splitlines()]

def get_differences(sequence: list[int]) -> list[int]:
    return [sequence[idx + 1] - value for idx, value in enumerate(sequence[:-1])]

def get_prediction(lsequence: list[int], rsequence: list[int], idx: int) -> int:
    return rsequence[idx] + lsequence[idx] if idx == -1 else rsequence[idx] - lsequence[idx]

def part_one(sequences: list[list[int]]) -> None:
    predictions = []
    
    for sequence in sequences:
        stack = [sequence]
        while stack[-1] != [0 for _ in range(len(stack[-1]))]:
            stack.append(get_differences(stack[-1]))
            
        while difference := stack.pop():
            if len(stack) == 0: break
            stack[-1].append(get_prediction(difference, stack[-1], -1))
            
        predictions.append(difference[-1])
        
    print(sum(predictions))
 
def part_two(sequences: list[list[int]]):
    predictions = []
    
    for sequence in sequences:
        stack = [sequence]
        while stack[-1] != [0 for _ in range(len(stack[-1]))]:
            stack.append(get_differences(stack[-1]))
            
        while difference := stack.pop():
            if len(stack) == 0:  break
            stack[-1].insert(0, get_prediction(difference, stack[-1], 0))
            
        predictions.append(difference[0])
        
    print(sum(predictions))

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
    # main("sample.txt")
    main("input.txt")
