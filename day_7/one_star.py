def solveTachyonManifold():
    with open('one_star.txt', 'r') as f:
        data = f.read()

    grid = [list(line) for line in data.strip().split('\n')]
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0

    start_pos = None
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 'S':
                start_pos = (r, c)
                break
        if start_pos:
            break

    if not start_pos:
        print("Error: Start position 'S' not found.")
        return

    splitters_hit = set()
    visited_starts = set()
    stack = [(start_pos[0] + 1, start_pos[1])]

    while stack:
        r, c = stack.pop()

        if (r, c) in visited_starts:
            continue
        visited_starts.add((r, c))

        curr_r, curr_c = r, c

        while 0 <= curr_r < rows and 0 <= curr_c < cols:
            cell = grid[curr_r][curr_c]

            if cell == '^':
                splitters_hit.add((curr_r, curr_c))
                
                if curr_c - 1 >= 0:
                    stack.append((curr_r, curr_c - 1))
                
                if curr_c + 1 < cols:
                    stack.append((curr_r, curr_c + 1))
                
                break
            
            curr_r += 1

    print(len(splitters_hit))

solveTachyonManifold()