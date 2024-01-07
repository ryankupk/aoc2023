import sys
import os
from collections import defaultdict

# class Node:
#     def __init__(self, name, weight):
#         self.name = name
#         self.weight = weight
#         self.children = []
#         self.parent = None
    
    
# class Tree:
#     def __init__(self):
#         self.root = None
        
#     def add_child(self, child):
#         if self.root is None:
#             self.root = child
#             return
#         if
        



def parse_data(filename):
    tree = defaultdict(list)
    with open(filename) as f:
        data = f.read().splitlines()
        for idx, line in enumerate(data): # could do this reading directly from file
            # current line is listing contents of current dir
            if line == "$ ls":
                # current dir is the dir that was cd'd to on the line above
                current_dir = data[idx-1].split(' ')[-1]
                i = idx + 1
                next_line = data[i]
                # if not changing dir and if not listing, append dirs and files to tree
                while "$ cd" not in next_line and "$ ls" not in next_line:
                    if "dir " in next_line:
                        tree[current_dir].append([0, next_line.split()[1]])
                        tree[next_line.split(' ')[1]] = []
                    else:
                        tree[current_dir].append(next_line.split())
                    
                    i += 1
                    if i != len(data):
                        next_line = data[i]
                    else: break
                
    return tree

def sum_dir(tree, current_item, all_dirs):
    pass

def solve_part_one(tree):
    for parent_dir, sub_dirs in tree:
        for dir in sub_dirs:
            if dir[0] == 0:
                tree[sum_dir(tree, dir)

def solve_part_two(tree):
    pass

def main(filename):
    tree = parse_data(filename)
    
    print(solve_part_one(tree))
    print(solve_part_two(tree))
    
    
if __name__ == "__main__":
    main(r"input2.txt")