contained = 0
with open('aoc-day04-input.txt') as f:
    for line in f:
        (f, s) = line.strip().split(',')
        first = f.split('-')
        second = s.split('-')
        if int(first[0]) <= int(second[0]):
            if int(second[1]) <= int(first[1]):
                contained += 1
                continue
        if int(second[0]) <= int(first[0]):
            if int(first[1]) <= int(second[1]):
                contained += 1
print(contained)