def is_safe(rep):
    delta_rep = []
    for i in range(len(rep)-1):
        delta = rep[i+1] - rep[i]
        delta_rep.append(delta)
    if max(delta_rep) <= 3 and min(delta_rep) >= 1:
        return 1
    elif max(delta_rep) <= -1 and min(delta_rep) >= -3:
        return 1
    else:
        return 0

safe1 = 0
with open('02input.txt') as f:
    for line in f:
        report = list(map(int, line.split()))
        if is_safe(report):
            safe1 += 1
print("Part 1:", safe1)

safe2 = 0
with open('02input.txt') as f:
    for line in f:
        report = list(map(int, line.split()))
        safe = 0
        for i in range(len(report)):
            new_report = list(report)
            del new_report[i]
            if is_safe(new_report):
                safe = 1
        safe2 += safe
print("Part 2:", safe2)
