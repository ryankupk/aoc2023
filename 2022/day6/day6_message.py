import sys

def parse_data(filename):
    with open(filename) as f:
        return f.read().strip()
    
    
def solve(data, num_unique):
    for idx, _ in enumerate(data):
        if idx < num_unique - 1:
            continue
        

        if len(set(data[idx - (num_unique - 1):idx+1])) == num_unique:
            return idx + 1



def main(filename):
    data = parse_data(filename)
    print(solve(data, 4))
    print(solve(data, 14))

if __name__ == "__main__":
    main(sys.argv[1])