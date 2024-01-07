

def main():
    efin = None
    with open("efin_input.txt") as f:
        efin = f.read().splitlines()
        
    ryab = None
    with open("ryab_input.txt") as f:
        ryab = f.read().splitlines()
        
    for ryab_line, efin_line in zip(ryab, efin):
        print(ryab_line == efin_line)

if __name__ == "__main__":
    main()