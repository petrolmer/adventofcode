max_scenic_score = 0
map = []
with open('aoc-day08-input.txt') as f:
    for line in f:
        x = [i for a,i in enumerate(line.strip())]
        map.append(x)

for row in range(1, len(map)-1):
    for col in range(1, len(map[row])-1):
        curr = int(map[row][col])
        scenic_score = 1
        for (xstep, ystep) in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
            r, c = row, col
            axis_score = 0
            r += xstep
            c += ystep
            while (r >= 0) and (r < len(map)) and (c >= 0) and (c < len(map[row])):
                axis_score += 1
                if int(map[r][c]) >= curr:
                    break
                r += xstep
                c += ystep 
            scenic_score *= axis_score
            print(row, col, axis_score)
        max_scenic_score = max(max_scenic_score, scenic_score)

print(max_scenic_score)
