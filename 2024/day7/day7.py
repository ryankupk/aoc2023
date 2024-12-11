import time

def parse_input(filename: str) -> list[str]:
    with open(filename) as f:
        return f.readlines()

def get_num_digits(n):
    if n == 0:
        return 1
    count = 0
    while n:
        count += 1
        n //= 10
    return count

def evaluate_ltr(params, operators):
    if not operators:
        return params[0]
    
    result = params[0]
    for i in range(len(operators)):
        if operators[i] == '*':
            result *= params[i + 1]
        elif operators[i] == '+':
            result += params[i + 1]
        elif operators[i] == '||':
            result = result * (10 ** get_num_digits(params[i+1])) + params[i+1]
    return result

def backtrack(test: int, params: list[int], operators: list[str], concat: bool) -> int:
    if len(operators) == len(params) - 1:
        return evaluate_ltr(params, operators) == test

    operators.append('+')
    if backtrack(test, params, operators, True):
        return True
    operators.pop()
    
    operators.append('*')
    if backtrack(test, params, operators, True):
        return True
    operators.pop()

    if concat:
        operators.append('||')
        if backtrack(test, params, operators, True):
            return True
        operators.pop()
    
    return False

def part_one(strings: list[str]) -> int | dict[int, list[int]]:
    count = 0
    invalid_tests = {}
    for line in strings:
        test_raw, params_raw = line.split(':')
        test = int(test_raw)
        params = list(map(int, params_raw.strip().split(' ')))

        if backtrack(test, params, [], False):
            count += test
        else:
            invalid_tests[test] = params

    print(count)
    return count, invalid_tests

def part_two(count, invalid_tests) -> None:
    for test, params in invalid_tests.items():

        if backtrack(test, params, [], True):
            count += test
    print(count)

def main(input_filename: str):
    inp = parse_input(input_filename)
    start_part_one = time.time()
    count, items = part_one(inp)
    start_part_two = time.time()
    part_two(count, items)
    end_time = time.time()
    print(f"Part one took {start_part_two - start_part_one:.2f} seconds")
    print(f"Part two took {end_time - start_part_two:.2f} seconds")

if __name__ == "__main__":
    main("input.txt")
    # main("sample.txt")
