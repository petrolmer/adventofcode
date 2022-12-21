priorities = 0
with open('aoc-day03-input.txt') as f:
    for line in f:
        l = len(line)
        first = set(line[:l//2])
        second = set(line[l//2:])
        inter = list(first.intersection(second))
        common = inter[0]
        if ord(common) >= ord('a'):
            p = ord(common) - ord('a') + 1
        else:
            p = ord(common) - ord('A') + 27
        priorities += p
print(priorities)