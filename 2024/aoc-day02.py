def is_safe(rep):
    delta_rep = [i-j for i, j in zip(rep, rep[1:])]
    return all(1 <= x <= 3 for x in delta_rep) or all(-3 <= x <= -1 for x in delta_rep)

safe1 = 0
with open('02input.txt') as f:
    for line in f:
        report = list(map(int, line.split()))
        if is_safe(report):
            safe1 += 1
print("Part 1:", safe1)

safe2 = 0
for line in open('02input.txt'):
    report = list(map(int, line.split()))
    safe = 0
    for i in range(len(report)):
        new_report = list(report)
        del new_report[i]
        if is_safe(new_report):
            safe = 1
    safe2 += safe
print("Part 2:", safe2)
