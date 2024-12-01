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
        split_perms = list(map(lambda x: list(filter(lambda y: y != '', x.split('.'))), all_perms))
        filtered = list(filter(lambda x: len(x) == len(patterns), split_perms))
        for perm in filtered:
            # compare against patterns and count valid
            if list(map(lambda x: len(x), perm)) == patterns:
                valid_count += 1
    print(valid_count)

 
def part_two(strings: list[str]) -> None:
    valid_count: int = 0
    for string in strings: 
        springs, pattern = string.split(' ')
        springs = '?'.join([springs] * 5)
        patterns = list(map(int, pattern.split(','))) * 5
        all_perms: list[str] = []
        get_permutation_of_springs(springs, all_perms)
        # reduce to list of groups split by '.'
        split_perms = list(map(lambda x: list(filter(lambda y: y != '', x.split('.'))), all_perms))
        filtered = list(filter(lambda x: len(x) == len(patterns), split_perms))
        for perm in filtered:
            # compare against patterns and count valid
            if list(map(lambda x: len(x), perm)) == patterns:
                valid_count += 1
        print("completed a string")
    print(valid_count)

def main(input_filename: str):
    inp = parse_input(input_filename)
    start_part_one = time.time()
    part_one(inp)
    start_part_two = time.time()
    # part_two(inp)
    end_time = time.time()
    print(f"Part one took {start_part_two - start_part_one} seconds")
    print(f"Part two took {end_time - start_part_two} seconds")

if __name__ == "__main__":
    # main("sample.txt")
    main("input.txt")