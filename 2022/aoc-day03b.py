priorities = 0
in_group = 1
with open('aoc-day03-input.txt') as f:
    for line in f:
        if in_group == 1:
            first = set(line.strip())
            in_group = 2
        elif in_group == 2:
            second = set(line.strip())
            in_group = 3
        else:
            third = set(line.strip())
            inter = list(first.intersection(second).intersection(third))
            common = inter[0]
            if ord(common) >= ord('a'):
                p = ord(common) - ord('a') + 1
            else:
                p = ord(common) - ord('A') + 27
            priorities += p
            in_group = 1
print(priorities)