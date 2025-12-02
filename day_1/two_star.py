def getLines():
    with open("two_star.txt") as f:
        lines = [line.strip() for line in f if line.strip()]
    return lines

def solve():
    state = 50
    lines = getLines()
    answer = 0

    for line in lines:
        instruction = line[0]
        number = int(line[1:])

        answer += number // 100
        rem = number % 100

        if instruction == 'R':
            if state + rem >= 100:
                answer += 1
            state = (state + number) % 100

        elif instruction == 'L':
            if state != 0 and state - rem <= 0:
                answer += 1
            state = (state - number) % 100

        print(line, state)

    print("Answer:", answer)

solve()

