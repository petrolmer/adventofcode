map = []
path = {}
with open('aoc-day12-input.txt') as f:
    i = 0
    j = 0
    for line in f:
        row = line.strip()
        for _ in row:
            if _ == "S":
                start = [i, j]
                row = row.replace("S", "a")
            elif _ == "E":
                end = [i, j]
                row = row.replace("E", "z")
            j += 1
        map.append(row)
        i += 1
        j = 0

xmax = len(map)-1
ymax = len(map[0])-1
been = []
check = [start]
path[str(start)] = 0

print(start, end)

def go(pos):
    global been, check, path
    curr = map[pos[0]][pos[1]]
    been.append(pos)
    if pos == end:
        return
#    print("position", pos, curr)
    for step in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
        p = list(pos)
        p[0] = pos[0] + step[0]
        p[1] = pos[1] + step[1]
        if (p[0] < 0) or (p[1] < 0) or (p[0] > xmax) or (p[1] > ymax):
            continue #outside map
        new = map[p[0]][p[1]]
        if ord(new) > ord(curr) + 1:
            continue # not reachable
#        print(step, p, new)
        if (p not in been) and (p not in check):
            check.append(p)
            path[str(p)] = path[str(pos)] + 1

while end not in been:
    p = check.pop(0)
    go(p)
    qq = len(been)
#    print(qq)

print(path[str(end)])