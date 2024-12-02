import time

def parse_input(filename: str) -> list[str]:
    with open(filename) as f:
        lines = f.readlines()
        return lines

def check_report(report):
    for i, _ in enumerate(report[:-1]):
        if report[i+1] > report[i] + 3:
            return False
    return True

def part_one(strings: list[str]) -> None:
    safe = 0
    for line in strings:
        report = list(map(int, line.split(' ')))

        increasing = all([report[i+1] > report[i] for i, _ in enumerate(report[:-1])])
        if increasing:
            if check_report(report):
                safe += 1

        decreasing = all([report[i+1] < report[i] for i, _ in enumerate(report[:-1])])
        if decreasing:
            if check_report(report[::-1]):
                safe += 1

    print(safe)

 
def part_two(strings: list[str]) -> None:
    safe = 0
    for line in strings:
        report = list(map(int, line.split(' ')))
        reports = []

        for i in range(len(report)):
            cur_report = report[:i] + report[i+1:]
            reports.append(cur_report)

        for report in reports:

            increasing = all([report[i+1] > report[i] for i, _ in enumerate(report[:-1])])
            if increasing:
                cur_safe = check_report(report)
                if cur_safe:
                    safe += 1
                    break

            decreasing = all([report[i+1] < report[i] for i, _ in enumerate(report[:-1])])
            if decreasing:
                cur_safe = check_report(report[::-1])
                if cur_safe:
                    safe += 1
                    break


    print(safe)

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