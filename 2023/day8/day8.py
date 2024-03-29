import time
import re
from math import lcm

START_NODE = 'AAA'
END_NODE = 'ZZZ'

def parse_input(filename: str) -> tuple[str, dict[str, tuple[str, str]]]:
    with open(filename, "r") as f:
        instructions = f.readline().strip()
        maze_raw = f.read().strip().splitlines()
        maze = {}
        for line in maze_raw:
            node, left, right = re.search(r"(\w+) = \((\w+), (\w+)\)", line).groups()
            maze[node] = (left, right)
    return (instructions, maze)

def part_one(instructions: str, maze: dict[str, tuple[str, str]]) -> None:
    cur_node = START_NODE
    step_count = 0
    wrap = len(instructions)
    while cur_node != END_NODE:
        if   instructions[step_count % wrap] == 'L':
            cur_node = maze[cur_node][0]
        elif instructions[step_count % wrap] == 'R':
            cur_node = maze[cur_node][1]
        
        step_count += 1
    
    print(step_count)
    

def part_two_iterative_and_way_too_slow(instructions: str, maze: dict[str, tuple[str, str]]) -> None:
    cur_nodes = [node for node in maze.keys() if node.endswith('A')]
    step_count = 0
    wrap = len(instructions)
    cur_z_nodes = 0
    needed_z_nodes = len(cur_nodes)
    while cur_z_nodes != needed_z_nodes:
        cur_nodes = [maze[node][0] if instructions[step_count % wrap] == 'L' else maze[node][1] for node in cur_nodes]
        cur_z_nodes = len([node for node in cur_nodes if node.endswith('Z')])
        step_count += 1
        if step_count % 1_000_000 == 0: print(step_count)
    
    print(step_count)
    
def circuit_length(node: str, instructions: str, maze: dict[str, tuple[str, str]]) -> int:
    step_count = 0
    wrap = len(instructions)
    while not node.endswith('Z'):
        node = maze[node][0] if instructions[step_count % wrap] == 'L' else maze[node][1]
        step_count += 1
    return step_count
    
def part_two(instructions: str, maze: dict[str, tuple[str, str]]) -> None:
    start_nodes = [node for node in maze.keys() if node.endswith('A')]
    circuit_lengths = [circuit_length(node, instructions, maze) for node in start_nodes]
    
    print(lcm(*circuit_lengths))

def main(input_filename: str):
    instructions, maze = parse_input(input_filename)
    start_part_one = time.time()
    part_one(instructions, maze)
    start_part_two = time.time()
    part_two(instructions, maze)
    end_time = time.time()
    print(f"Part one took {start_part_two - start_part_one} seconds")
    print(f"Part two took {end_time - start_part_two} seconds")

if __name__ == "__main__":
    # main("sample.txt")
    # main("sample2.txt")
    main("input.txt")
    # main("sample3.txt")
