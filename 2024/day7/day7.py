import time

def parse_input(filename: str) -> list[str]:
    with open(filename) as f:
        return f.readlines()

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
            result = int(str(result) + str(params[i+1]))
    return result

def backtrack(test, params, operators):
    if len(operators) == len(params) - 1:
        return evaluate_ltr(params, operators) == test
    
    operators.append('+')
    if backtrack(test, params, operators):
        return True
    operators.pop()
    
    operators.append('*')
    if backtrack(test, params, operators):
        return True
    operators.pop()
    
    return False

def part_one(strings: list[str]) -> None:
    count = 0
    for line in strings:
        test_raw, params_raw = line.split(':')
        test = int(test_raw)
        params = list(map(int, params_raw.strip().split(' ')))

        if backtrack(test, params, []):
            count += test
    print(count)
 
def backtrack_concat(test, params, operators):
    if len(operators) == len(params) - 1:
        return evaluate_ltr(params, operators) == test

    operators.append('+')
    if backtrack_concat(test, params, operators):
        return True
    operators.pop()
    
    operators.append('*')
    if backtrack_concat(test, params, operators):
        return True
    operators.pop()

    operators.append('||')
    if backtrack_concat(test, params, operators):
        return True
    operators.pop()
    
    return False

def part_two(strings: list[str]) -> None:
    count = 0
    for line in strings:
        test_raw, params_raw = line.split(':')
        test = int(test_raw)
        params = list(map(int, params_raw.strip().split(' ')))

        if backtrack_concat(test, params, []):
            count += test
    print(count)

def main(input_filename: str):
    inp = parse_input(input_filename)
    start_part_one = time.time()
    part_one(inp)
    start_part_two = time.time()
    part_two(inp)
    end_time = time.time()
    print(f"Part one took {start_part_two - start_part_one:.2f} seconds")
    print(f"Part two took {end_time - start_part_two:.2f} seconds")

if __name__ == "__main__":
    main("input.txt")
    # main("sample.txt")
