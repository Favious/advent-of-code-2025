def readInput():
    with open("two_star.txt") as f:
        lines = [line.rstrip("\n") for line in f if line.rstrip("\n")]

    numberLines = lines[:-1]
    operatorRow = lines[-1]

    maxLen = max(len(line) for line in lines)
    numberLines = [line.ljust(maxLen) for line in numberLines]
    operatorRow = operatorRow.ljust(maxLen)

    problems = []
    currentProblemCols = []
    currentProblemOps = []

    for i in range(maxLen):
        col = [line[i] for line in numberLines]
        op = operatorRow[i]
        if all(c == " " for c in col):
            if currentProblemCols:
                currentProblemOps.append(op if op != ' ' else currentProblemOps[-1])
                problems.append((currentProblemCols, currentProblemOps[-1]))
                currentProblemCols = []
                currentProblemOps = []
        else:
            currentProblemCols.append(col)
            if op != ' ':
                currentProblemOps.append(op)

    if currentProblemCols:
        op = currentProblemOps[-1] if currentProblemOps else '+'
        problems.append((currentProblemCols, op))

    return problems

def buildNumber(col):
    return int(''.join(c for c in col if c != ' '))

def solve():
    problems = readInput(filename)
    total = 0

    for cols, op in reversed(problems):
        numbers = [buildNumber(col) for col in cols]
        result = numbers[0]
        for num in numbers[1:]:
            if op == '+':
                result += num
            elif op == '*':
                result *= num
        total += result

    print(total)

solve()
