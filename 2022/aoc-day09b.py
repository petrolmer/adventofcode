Hx = [0] * 10
Hy = [0] * 10
visited = {"0-0"}

def move():
    global Hx, Hy
    for i in range(1, 10):
        if Hy[i-1] == Hy[i]+2:
            Hy[i] += 1
            if Hx[i-1] > Hx[i]:
                Hx[i] += 1
            elif Hx[i-1] < Hx[i]:
                Hx[i] -= 1
        elif Hy[i-1] == Hy[i]-2:
            Hy[i] -= 1
            if Hx[i-1] > Hx[i]:
                Hx[i] += 1
            elif Hx[i-1] < Hx[i]:
                Hx[i] -= 1
        elif Hx[i-1] == Hx[i]-2:
            Hx[i] -= 1
            if Hy[i-1] > Hy[i]:
                Hy[i] += 1
            elif Hy[i-1] < Hy[i]:
                Hy[i] -= 1
        elif Hx[i-1] == Hx[i]+2:
            Hx[i] += 1
            if Hy[i-1] > Hy[i]:
                Hy[i] += 1
            elif Hy[i-1] < Hy[i]:
                Hy[i] -= 1

q = 0
with open('aoc-day09-input.txt') as f:
    for line in f:
        q += 1
        l = line.strip()
        (direction, steps) = l.split()
        for i in range(int(steps)):
            if direction == "U":
                Hy[0] += 1
            elif direction == "D":
                Hy[0] -= 1
            elif direction == "L":
                Hx[0] -= 1
            elif direction == "R":
                Hx[0] += 1
            move()
            pos = str(Hx[9]) + "-" + str(Hy[9])
            visited.add(pos)

print(len(visited))