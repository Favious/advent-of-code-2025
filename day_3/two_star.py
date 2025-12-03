def getLines():
    with open("two_star.txt") as f:
        lines = [line.strip() for line in f if line.strip()]
    return lines


def findMaxJoltage(line, size=12):
    digits = list(map(int, line))
    stack = []

    canRemove = len(digits) - size

    for d in digits:
        while stack and stack[-1] < d and canRemove > 0:
            stack.pop()
            canRemove -= 1
        stack.append(d)

    stack = stack[:size]

    max_number = int("".join(map(str, stack)))
    print(max_number)
    return max_number


def solve():
    lines = getLines()
    answer = sum(findMaxJoltage(line) for line in lines)
    print(answer)


solve()
