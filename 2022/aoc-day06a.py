with open('aoc-day06-input.txt') as f:
    for line in f:
        l = line.strip()
for i in range(4, len(l)+1):
    code = l[i-4:i]
    s = set(list(code))
    if len(s) == 4:
        break
print(i)
print(code)
