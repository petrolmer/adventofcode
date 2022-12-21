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
#        print(line)
#        print(stack[from_stack])
#        print(stack[to_stack])
        stack[to_stack].extend(stack[from_stack][-int(many):])
        stack[from_stack] = stack[from_stack][:len(stack[from_stack])-int(many)]
#        print(stack[from_stack])
#        print(stack[to_stack])
print(stack['1'][-1], stack['2'][-1], stack['3'][-1], stack['4'][-1], stack['5'][-1], stack['6'][-1], stack['7'][-1], stack['8'][-1], stack['9'][-1])

