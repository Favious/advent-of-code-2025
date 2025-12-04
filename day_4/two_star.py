def getLines():
    with open("two_star.txt") as f:
        lines = [line.strip() for line in f if line.strip()]
    return lines

def isRollAccessible(grid, i, j, rowS, colS, new_matrix):
    adjacentRolls = 0

    for x in range(i - 1, i + 2):
        for y in range(j - 1, j + 2):
            if x == i and y == j:
                continue
            if 0 <= x < rowS and 0 <= y < colS:
                if grid[x][y] == '@':
                    adjacentRolls += 1

    if grid[i][j] == '@' and adjacentRolls < 4:
        new_matrix[i][j] = 'x'


def getAccessibleRolls(lines, new_matrix):
    grid = [list(row) for row in lines]

    rowS = len(grid)
    colS = len(grid[0])

    for i in range(rowS):
        for j in range(colS):
            isRollAccessible(grid, i, j, rowS, colS, new_matrix)

    # for row in new_matrix:
    #     print("".join(row))

    return sum(row.count('x') for row in new_matrix)

def solve():
    lines = getLines()
    lines_matrix = [list(r) for r in lines]

    previous_matrix = [row[:] for row in lines_matrix]

    su = 0
    count = 1
    while count > 0:
        new_matrix = [row[:] for row in previous_matrix]
        count = getAccessibleRolls(previous_matrix, new_matrix)
        su += count
        new_matrix = [['.' if cell == 'x' else cell for cell in row] for row in new_matrix]
        previous_matrix = new_matrix
        
    print(su)
solve()
