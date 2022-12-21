class Monkey:
    def __init__(self, items, operation, y, test, iftrue, iffalse):
        self.items = items
        self.operation = operation
        self.test = test
        self.y = y
        self.iftrue = iftrue
        self.iffalse = iffalse
        self.inspected = 0

    def turn(self):
        for it in self.items:
            if self.y == "old":
                it = self.operation(it, it)
            else:
                it = self.operation(it, int(self.y))
            it = it//3
            if it % self.test == 0:
                m[self.iftrue].throw(it)
            else:
                m[self.iffalse].throw(it)
        self.inspected += len(self.items)
        self.items = []

    def throw(self, item):
        self.items.append(item)

m = []

with open('aoc-day11-input.txt') as f:
    for line in f:
        c = line.strip().split()
        if len(c) == 0:
            continue
        elif c[0] == "Starting":
            items = list(map(int, ''.join(c[2:]).split(',')))
        elif c[0] == "Operation:":
            if c[4] == "*":
                op = lambda x, y: x * y
            elif c[4] == "+":
                op = lambda x, y: x + y
            y = c[5]
        elif c[0] == "Test:":
            test = int(c[3])
        elif c[0] == "If":
            if c[1] == "true:":
                iftrue = int(c[5])
            elif c[1] == "false:":
                iffalse = int(c[5])
                m.append(Monkey(items, op, y, test, iftrue, iffalse))
#                print(m[0].operation(1))

for round in range(20):
    for i in m:
        i.turn()

insp = []
for i in m:
    insp.append(i.inspected)

insp = sorted(insp)
print(insp[-1] * insp[-2])