def getLines():
    with open("two_star.txt") as f:
        return [line.rstrip("\n") for line in f]
    
def mergeRanges(ranges):
    ranges.sort()
    merged = [ranges[0]]

    for a, b in ranges[1:]:
        la, lb = merged[-1]
        if a <= lb:
            merged[-1] = (la, max(lb, b))
        else:
            merged.append((a, b))
    return merged

def isAvailable(ranges, e):
    l = 0
    r = len(ranges) - 1

    while l <= r:
        mid = (l + r) // 2
        a, b = ranges[mid]
        if a <= e <= b:
            return 1
        if e < a:
            r = mid - 1
        elif e > b:
            l = mid + 1
    
    return 0

def solve():
    lines = getLines()

    ranges = []
    values = []

    reading_ranges = True

    for line in lines:
        stripped = line.strip()

        if stripped == "":
            reading_ranges = False
            continue

        if reading_ranges:
            if "-" not in stripped:
                print("Invalid range line:", repr(line))
                continue
            a, b = map(int, stripped.split("-"))
            ranges.append((a, b))
        else:
            values.append(int(stripped))

    merged = mergeRanges(ranges)
    print(merged)

    count = 0
    for r in merged:
        a, b = r
        count += b - a + 1

    print(count) 
solve()

