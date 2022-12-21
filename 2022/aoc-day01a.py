max_cal = 0
curr_cal = 0
with open('aoc-day01a-input.txt') as f:
    for line in f:
        l = line.strip()
        if l:
            cal = int((line.strip()))
            curr_cal += cal
            max_cal = max(curr_cal, max_cal)
        else:
            curr_cal = 0
print(max_cal)
