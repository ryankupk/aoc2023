import time

def parse_input(filename: str) -> list[str]:
    return open(filename).read().splitlines()

def get_permutation_of_springs(current_string: str, all_strings: list[str]):
    if '?' not in current_string:
        all_strings.append(current_string)
    else:
        get_permutation_of_springs(current_string.replace('?','.',1), all_strings)
        get_permutation_of_springs(current_string.replace('?','#',1), all_strings)


def part_one(strings: list[str]) -> None:
    valid_count: int = 0
    for string in strings: 
        springs, pattern = string.split(' ')
        patterns = list(map(int, pattern.split(',')))
        all_perms: list[str] = []
        get_permutation_of_springs(springs, all_perms)
        # reduce to list of groups split by '.'
        split_perms = list(map(lambda x: x.split('.'), all_perms))
        for perm in split_perms:
            # transform perm into pattern
            perm_pattern = [len(spring_set) for spring_set in perm if spring_set != '']
            # compare against patterns and count valid
            if perm_pattern == patterns:
                valid_count += 1
    print(valid_count)

 
def part_two(strings: list[str]) -> None:
    pass

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