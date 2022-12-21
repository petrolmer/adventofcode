stack = {}
stack['1'] = ['N', 'D', 'M', 'Q', 'B', 'P', 'Z']
stack['2'] = ['C', 'L', 'Z', 'Q', 'M', 'D', 'H', 'V']
stack['3'] = ['Q', 'H', 'R', 'D', 'V', 'F', 'Z', 'G']
stack['4'] = ['H', 'G', 'D', 'F', 'N']
stack['5'] = ['N', 'F', 'Q']
stack['6'] = ['D', 'Q', 'V', 'Z', 'F', 'B', 'T']
stack['7'] = ['Q', 'M', 'T', 'Z', 'D', 'V', 'S', 'H']
stack['8'] = ['M', 'G', 'F', 'P', 'N', 'Q']
stack['9'] = ['B', 'W', 'R', 'M']

with open('aoc-day05-input.txt') as f:
    for line in f:
        (move, many, fr, from_stack, to, to_stack) = line.strip().split()
        for i in range(int(many)):
            stack[to_stack].append(stack[from_stack].pop())
print(stack['1'].pop())
print(stack['2'].pop())
print(stack['3'].pop())
print(stack['4'].pop())
print(stack['5'].pop())
print(stack['6'].pop())
print(stack['7'].pop())
print(stack['8'].pop())
print(stack['9'].pop())
