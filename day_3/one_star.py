def getLines():
    with open("one_star.txt") as f:
        lines = [line.strip() for line in f if line.strip()]
    return lines


def findMaxJoltage(line):
    digits = list(map(int, line))
    n = len(digits)

    lefti = max(range(n - 1), key=lambda i: digits[i])
    left = digits[lefti]

    right = max(digits[lefti + 1:])

    return left * 10 + right


def solve():
    lines = getLines()
    answer = sum(findMaxJoltage(line) for line in lines)
    print(answer)


solve()
