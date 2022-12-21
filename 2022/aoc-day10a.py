x = 1
h = [0]
with open('aoc-day10-input.txt') as f:
    for line in f:
        command = line.strip().split()
        if command[0] == "noop":
            h.append(x)
        elif command[0] == "addx":
            h.append(x)
            h.append(x)
            x = x + int(command[1])
h.append(x)
print(20*h[20] + 60*h[60] + 100*h[100] + 140*h[140] + 180*h[180] + 220*h[220])