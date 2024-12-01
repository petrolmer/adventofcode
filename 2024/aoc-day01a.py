total_diff = 0
left = []
right = []
right_count = {}
sim_score = 0
with open('01input.txt') as f:
    for line in f:
        (l, r) = line.strip().split()
        left.append(l)
        right.append(r)
        try:
            right_count[r] += 1
        except:
            right_count[r] = 1
left.sort()
right.sort()
for i in range(len(left)):
    diff = abs(int(left[i]) - int(right[i]))
    total_diff += diff
print("Part 1:", total_diff)

for l in left:
    try:
        sim_score += int(l) * right_count[l]
    except:
        continue

print("Part 2:", sim_score)