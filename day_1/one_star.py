def getLines():
    with open("one_star.txt") as f:
        lines = [line.strip() for line in f if line.strip()]
    return lines

def solve():
    state = 50
    lines = getLines()
    answer = 0

    for line in lines:
        instruction = line[0]
        number = int(line[1:])
        if number > 99:
          number = int(line[2:]) 
        if instruction == 'R':
            state += number
            if state > 99:
                state -= 100
        elif instruction == 'L':
            state -= number
            if state < 0:
                state += 100
        else:
            continue
        print(line, state)
        if state == 0:
            answer += 1
    print("Answer:", answer)

solve()

