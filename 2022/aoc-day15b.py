sensors = {}
beacons = {}

size = 4000000
#size = 20

map = []
for y in range(size+1):
    map.append([])

print("map is set")
def distance(a, b):
    x1, y1 = a
    x2, y2 = b
    return (abs(x1-x2) + abs(y1-y2))

def remove(s, d):
    global map
    sx, sy = s
    wide = 0
    while d >= 0:
        try:
            map[sy-d].append((max(0,sx-wide), min(size,sx+wide)))
        except:
            pass
        try:
            map[sy+d].append((max(0,sx-wide), min(size,sx+wide)))
        except:
            pass
        d -= 1
        wide += 1

print(len(map))

with open('aoc-day15-input.txt') as f:
    for line in f.read().strip().splitlines():
        print(line)
        q = line.strip().split()
        sx = int(q[2].strip(",").split("=")[1])
        sy = int(q[3].strip(":").split("=")[1])
        bx = int(q[8].strip(",").split("=")[1])
        by = int(q[9].split("=")[1])
        remove((sx, sy), distance((bx, by), (sx, sy)))
        print(map[0])
        sensors[sx, sy] = distance((bx, by), (sx, sy))
        beacons[bx, by] = "B"
        print(sensors[sx, sy])

yy = 0

print(map[0])

for y in map:
    y.sort()
#    print(y)
    xmin, xmax = y[0]
    for x in y:
        x1, x2 = x
        if x1 <= xmax+1:
            xmax = max(xmax, x2)
    if (xmin <= 0) and (xmax >= size):
        pass
    else:
        print(4000000*(xmax+1)+yy)
    yy += 1

#print(xmin, xmax)
#print(ymin, ymax)

#print(len(map))
