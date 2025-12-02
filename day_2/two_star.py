def checkIfIsInvalid(num):
    s = str(num)
    L = len(s)

    for size in range(1, L // 2 + 1):
        if L % size != 0:
            continue 

        pattern = s[:size]
        if pattern * (L // size) == s:
            return num
    return 0


def getSumOfInvalidNumbers(lower, upper):
    count = 0
    for i in range(lower, upper + 1):
        count += checkIfIsInvalid(i)
    return count

def readRangesFromFile(filename):
    with open(filename, "r") as f:
        data = f.read().strip()

    parts = data.split(",")
    ranges = []

    for p in parts:
        if not p.strip():
            continue
        a, b = p.split("-")
        ranges.append((int(a), int(b)))

    return ranges

def solve():
    ranges = readRangesFromFile("two_star.txt")
    count = 0
    for a, b in ranges:
        count += getSumOfInvalidNumbers(a, b)
    print("RESULT:", count)

solve()
