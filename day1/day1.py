ints = '1234567890'
intstrs = {'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}

def parse_input(filename: str):
    return open(filename, "r").read().splitlines()

def part_one(strings: list):
    nums = []
    for string in strings:
        num = ''
        for char in string:
            if char in ints:
                num += char
                break
        for char in string[::-1]:
            if char in ints:
                num += char
                break
        nums.append(int(num))
        
    print(sum(nums))
    
def string_contains_digit(string: str):
    if string[-1] in ints:
        return string[-1]
    for intstr, num in intstrs.items():
        if intstr in string:
            return num
    return -1

def part_two(strings: list):
    nums = []
    for string in strings:
        num = ''
        build = ''
        for char in string:
            build += char
            append = string_contains_digit(build)
            if append != -1:
                num += append
                break
        build = ''
        for char in string[::-1]:
            if char in ints:
                num += char
                break
            build += char
            append = string_contains_digit(build[::-1])
            if append != -1:
                num += append
                break
        nums.append(int(num))
    print(sum(nums))

def main(input_filename: str):
    inp = parse_input(input_filename)
    part_one(inp)
    part_two(inp)

if __name__ == "__main__":
    main("input.txt")