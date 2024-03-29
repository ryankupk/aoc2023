import time
from typing import Union
from collections import defaultdict

def parse_input(filename: str) -> list[str]:
    return open(filename, "r").read().strip().split(",")

def calculate_hash(string: str) -> int:
    cur_value = 0
    for char in string:
        cur_value += ord(char)
        cur_value *= 17
        cur_value %= 256
    return cur_value

def part_one(strings: list[str]) -> None:
    total_values = 0
    for string in strings:
        total_values += calculate_hash(string)
    print(total_values)

def remove_lens(box: int, label: str, boxes: dict[int, list[list[Union[int, str]]]]) -> tuple[dict[int, list[list[Union[int, str]]]], int]:
    for idx, lens in enumerate(boxes[box]):
        if label in lens:
            boxes[box].remove(lens)
            return boxes, idx
    
    return boxes, -1

def add_lens(box: int, label: str, lens: int, boxes: dict[int, list[list[Union[int, str]]]]) -> dict[int, list[list[Union[int, str]]]]:
    boxes, idx = remove_lens(box, label, boxes)
    if idx == -1:
        boxes[box].append([label, lens])
    else:
        boxes[box].insert(idx, [label, lens])
    return boxes

def calculate_focusing_power(boxes: dict[list[list[Union[int, str]]]]) -> int:
    focusing_power = 0
    for box, lenses in boxes.items():
        for idx, lens in enumerate(lenses):
            focusing_power += (1 + box) * (1 + idx) * lens[1]
    return focusing_power

def part_two(strings: list[str]) -> None:
    boxes = defaultdict(list)
    for string in strings:
        if '-' in string:
            label = string[:-1]
            box = calculate_hash(label)
            boxes, _ = remove_lens(box, label, boxes)
            
        elif '=' in string:
            label, focal_length = string.split('=')
            box = calculate_hash(label)
            boxes = add_lens(box, label, int(focal_length), boxes)
            
    print(calculate_focusing_power(boxes))
            

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
