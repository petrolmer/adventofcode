Hx = 0
Hy = 0
Tx = 0
Ty = 0
visited = {"0-0"}
with open('aoc-day09-input.txt') as f:
    for line in f:
        l = line.strip()
        (direction, steps) = l.split()
        for i in range(int(steps)):
            if direction == "U":
                Hy += 1
                if Hy == Ty+2:
                    Ty += 1
                    if Hx != Tx:
                        Tx = Hx
            elif direction == "D":
                Hy -= 1
                if Hy == Ty-2:
                    Ty -= 1
                    if Hx != Tx:
                        Tx = Hx
            elif direction == "L":
                Hx -= 1
                if Hx == Tx-2:
                    Tx -= 1
                    if Hy != Ty:
                        Ty = Hy
            elif direction == "R":
                Hx += 1
                if Hx == Tx+2:
                    Tx += 1
                    if Hy != Ty:
                        Ty = Hy
            pos = str(Tx) + "-" + str(Ty)
            visited.add(pos)

print(len(visited))