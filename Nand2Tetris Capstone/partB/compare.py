import sys

def lines(path):
    with open(path) as f:
        return [l.strip() for l in f if l.strip()]

mine, official = lines(sys.argv[1]), lines(sys.argv[2])
if mine == official:
    print("MATCH: identical output")
else:
    print(f"DIFFERENT: yours has {len(mine)} lines, official has {len(official)}")
    for i, (a, b) in enumerate(zip(mine, official), 1):
        if a != b:
            print(f"First difference at line {i}:\n  yours:    {a}\n  official: {b}")
            break
