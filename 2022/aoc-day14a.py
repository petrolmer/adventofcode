map = {}

with open('aoc-day14-input.txt') as f:
    for line in f.read().strip().splitlines():
        rocks = line.strip().split(" -> ")
        for i in range(len(rocks)-1):
            if i == 0:
                map[rocks[i]] = "#"
            fr = rocks[i].split(",")
            to = rocks[i+1].split(",")
            fr[0] = int(fr[0])
            fr[1] = int(fr[1])
            to[0] = int(to[0])
            to[1] = int(to[1])
            if fr[0] == to[0]:
                dx = 0
            elif fr[0] < to[0]:
                dx = 1
            else:
                dx = -1
            if fr[1] == to[1]:
                dy = 0
            elif fr[1] < to[1]:
                dy = 1
            else:
                dy = -1
            while fr != to:
                fr[0] += dx
                fr[1] += dy
                newpos = str(fr[0]) + "," + str(fr[1])
                map[newpos] = "#"

xmin = 500
xmax = 500
ymin = 0
ymax = 0

for xy in map:
    q = xy.split(",")
    xmin = min(xmin, int(q[0]))
    xmax = max(xmax, int(q[0]))
    ymin = min(ymin, int(q[1]))
    ymax = max(ymax, int(q[1]))

xmin -= 1
xmax += 1
ymax += 1
print(xmin, xmax)
print(ymin, ymax)

def draw_map():
    for y in range(ymin, ymax+1):
        for x in range(xmin, xmax+1):
            xy = str(x) + "," + str(y)
            try:
                d = map[xy]
                print(d, end="")
            except:
                print(" ", end="")
        print()

def sand_fall(xsand, ysand):
    global map
    void = True
    x = xsand
    done = False
    while not done:
        for y in range(ysand, ymax+1):
            xy = str(xsand) + "," + str(y)
            try:
                d = map[xy]
                void = False
                break
            except:
                continue
        if void:
            return False
        ysand = y-1
        try:
            xy = str(xsand-1) + "," + str(ysand+1)
            d = map[xy]
            try:
                xy = str(xsand+1) + "," + str(ysand+1)
                d = map[xy]
                done = True
            except:
                xsand += 1
                ysand += 1
                void = True
        except:
            xsand -= 1
            ysand += 1
            void = True
    xy = str(xsand) + "," + str(ysand)
    map[xy] = "o"
    return True

i = 0
while sand_fall(500, 0):
    i += 1

draw_map()
print(i)
