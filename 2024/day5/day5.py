import time
from collections import defaultdict
from functools import cmp_to_key

def parse_input(filename: str): # -> dict[int,int], list[list[int]]:
    with open(filename) as f:
        nl_flag = False
        rules = defaultdict(set)
        pages = []
        for line in f.readlines():
            if line == '\n':
                nl_flag = True
                continue
            if not nl_flag:
                rule_one, rule_two = list(map(int, line.strip().split('|')))
                rules[rule_one].add(rule_two)
            if nl_flag:
                pages.append(list(map(int, line.split(','))))
        return rules, pages


def part_one(rules: dict[int, set[int]], pages: list[list[int]]) -> list[list[int]]:
    count = 0
    incorrect = []
    for page_list in pages:
        break_outer = False
        middle = len(page_list) // 2
        middle_page = None
        for i, parent_page in enumerate(page_list):
            if break_outer:
                break
            if i == middle:
                middle_page = parent_page
            for child_page in page_list[i+1:]:
                if child_page not in rules[parent_page]:
                    break_outer = True
                    incorrect.append(page_list)
                    break
        if not break_outer:
            count += middle_page

    print(count)
    return incorrect


def part_two(rules: dict[int, set[int]], pages: list[list[int]]) -> None:
    def sort_key(i, j):
        if i in rules[j]:
            return 1
        elif j in rules[i]:
            return -1
        else:
            return 0

    count = 0
    for page_list in pages:
        middle = len(page_list) // 2
        page_list.sort(key=cmp_to_key(sort_key))
        count += page_list[middle]

    print(count)


def main(input_filename: str):
    rules, pages = parse_input(input_filename)
    start_part_one = time.time()
    incorrect = part_one(rules, pages)
    start_part_two = time.time()
    part_two(rules, incorrect)
    end_time = time.time()
    print(f"Part one took {start_part_two - start_part_one:.2f} seconds")
    print(f"Part two took {end_time - start_part_two:.2f} seconds")

if __name__ == "__main__":
    # main("sample.txt")
    main("input.txt")
