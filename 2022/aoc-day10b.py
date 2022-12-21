x = 1
h = [0]

pos = 0

def draw(x):
    global pos
    if abs(pos - x) <= 1:
        print("#", end="")
    else:
        print(" ", end="")
    pos += 1
    if pos >= 40:
        pos = 0
        print()


with open('aoc-day10-input.txt') as f:
    for line in f:
        command = line.strip().split()
        if command[0] == "noop":
            draw(x)
        elif command[0] == "addx":
            draw(x)
            draw(x)
            x = x + int(command[1])
