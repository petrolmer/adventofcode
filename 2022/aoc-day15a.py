sensors = {}
beacons = {}
xmax = 3088287
xmin = 3088287
ymax = 2966967
ymin = 2966967
xmax = 0
xmin = 0
ymax = 0
ymin = 0

def distance(a, b):
    x1, y1 = a
    x2, y2 = b
    return (abs(x1-x2) + abs(y1-y2))

with open('aoc-day15-input.txt') as f:
    for line in f.read().strip().splitlines():
        q = line.strip().split()
        sx = int(q[2].strip(",").split("=")[1])
        sy = int(q[3].strip(":").split("=")[1])
        bx = int(q[8].strip(",").split("=")[1])
        by = int(q[9].split("=")[1])
        xmax = max(xmax, sx + distance((bx, by), (sx, sy)), bx)
        xmin = min(xmin, sx - distance((bx, by), (sx, sy)), bx)
        ymax = max(ymax, sy, by)
        ymin = min(ymin, sy, by)
        sensors[sx, sy] = distance((bx, by), (sx, sy))
        beacons[bx, by] = "B"

print(xmin, xmax)
print(ymin, ymax)

y = 2000000
#y=10
sum = 0
for x in range(xmin, xmax+1):
    found = False
#    print("check", x, y)
    for s in sensors:
#        print("  sensor", s)
        if sensors[s] >= distance((x, y), s):
            found = True
#            print("  OK")
            break
    if found:
        sum += 1
#        print("#", end="")
#    else:
#        print(".", end="")
for b in beacons:
    (bx, by) = b
    if by == y:
        sum -=1

print()
print(sum)
