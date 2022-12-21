with open('aoc-day06-input.txt') as f:
    for line in f:
        l = line.strip()
for i in range(14, len(l)+1):
    code = l[i-14:i]
    s = set(list(code))
    if len(s) == 14:
        break
print(i)
print(code)
