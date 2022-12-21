curr_cal = 0
elves = []
with open('aoc-day01a-input.txt') as f:
    for line in f:
        l = line.strip()
        if l:
            cal = int((line.strip()))
            curr_cal += cal
        else:
            elves.append(curr_cal)
            curr_cal = 0
elves.append(curr_cal)
elves.sort(reverse=True)
print(elves[0] + elves[1] + elves[2])
