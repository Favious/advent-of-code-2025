from functools import reduce

def read_input():
    with open("one_star.txt") as f:
        raw = [line.strip() for line in f if line.strip()]

    number_rows = []
    operator_row = None

    for line in raw:
        parts = line.split()

        # If all parts are digits → it's a number row
        if all(p.isdigit() for p in parts):
            number_rows.append(list(map(int, parts)))

        # Otherwise it must be operators
        else:
            operator_row = parts

    # Convert rows → columns
    columns = list(zip(*number_rows))
    return columns, operator_row

def applyOperation(paired):
    operator = paired[1]
    lambdaSum = lambda a, b: a + b
    lambdaMul = lambda a, b: a * b
    if operator == '+':
        return reduce(lambdaSum, paired[0])
    elif operator == '*':
        return reduce(lambdaMul, paired[0])
    else:
        return 0


def solve():
    columns, operators = read_input()
    paired = [(col, op) for col, op in zip(columns, operators)]
    print(paired)
    count = 0
    for pair in paired:
        count += applyOperation(pair)
    print(count)

solve()
