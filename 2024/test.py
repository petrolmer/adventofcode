l = [list(map(int, line.split())) for line in open('01input.txt').read().splitlines()][0]
r = [list(map(int, line.split())) for line in open('01input.txt').read().splitlines()][1]
print(sum(x * r.count(x) for x in l))
