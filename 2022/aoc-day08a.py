map = []
visible = []
with open('aoc-day08-input.txt') as f:
    for line in f:
        x = [i for a,i in enumerate(line.strip())]
        map.append(x)
        y = [' ' for a,i in enumerate(line.strip())]
        visible.append(y)

for row in range(len(map)):
    max = -1
    for col in range(len(map[row])):
        curr = int(map[row][col])
        if curr > max:
            visible[row][col] = 'Y'
            max = curr

for row in range(len(map)):
    max = -1
    for col in reversed(range(len(map[row]))):
        curr = int(map[row][col])
        if curr > max:
            visible[row][col] = 'Y'
            max = curr

for col in range(len(map[0])):
    max = -1
    for row in range(len(map)):
        curr = int(map[row][col])
        if curr > max:
            visible[row][col] = 'Y'
            max = curr

for col in range(len(map[0])):
    max = -1
    for row in reversed(range(len(map))):
        curr = int(map[row][col])
        if curr > max:
            visible[row][col] = 'Y'
            max = curr

count = 0
for r in visible:
    for c in r:
        if c == 'Y':
            count += 1

print(count)

