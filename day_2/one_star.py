def checkIfIsInvalid(num):
    s = str(num)
    mid = len(s) // 2

    first = int(s[:mid])
    com = int(str(first) + str(first))
    if com == num:
        print("INVALID:", num)
        return num
    else:
        return 0

def getSumOfInvalidNumbers(lower, upper):
    count = 0
    for i in range(lower, upper + 1):
        il = len(str(i))
        if il & 1:
            continue
        else:
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
    ranges = readRangesFromFile("one_star.txt")
    count = 0
    for a, b in ranges:
        count += getSumOfInvalidNumbers(a, b)
    print("RESULT:", count)

solve()
