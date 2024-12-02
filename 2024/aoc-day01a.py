left = []
right = []
right_count = {}
sim_score = 0
with open('01input.txt') as f:
    for line in f:
        l, r = map(int, line.split())
        left.append(l)
        right.append(r)
        try:
            right_count[r] += 1
        except:
            right_count[r] = 1
left.sort()
right.sort()
diff = [abs(l - r) for l, r in zip(left, right)]
total_diff = sum(diff)
print("Part 1:", total_diff)
for l in left:
    try:
        sim_score += l * right_count[l]
    except:
        continue
print("Part 2:", sim_score)