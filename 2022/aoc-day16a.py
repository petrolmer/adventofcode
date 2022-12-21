import copy
valves = {}

with open('aoc-day16-input.txt') as f:
    for line in f.read().strip().splitlines():
        q = line.strip().split()
        v = q[1]
        f = int(q[4].strip(";").split("=")[1])
        t = list(map(lambda x: x.strip(","), q[9:]))
        valves[v] = [False, f, t]

print(valves)
print()

def go(valves, v, min, flow, visited_no_reason):
    min += 1
    if min > 30:
        x = sum(flow[0:-1])
        if x>=1651:
            print(x)
        return flow
#    print("minute", min, "  valve", v, "  path", path)
    next = valves[v][2]
    visited_no_reason.append(v)
    for n in next:
        if n not in visited_no_reason:
#            if valves[n][0]:
#                npp = n.upper()
#            else:
#                npp = n.lower()
            f = flow.copy()
            f.append(f[-1])
            go(copy.deepcopy(valves), n, min, f, visited_no_reason)
    if not valves[v][0]:
        valves[v][0] = True
        newf = valves[v][1] + flow[-1]
        f = flow.copy()
        f.append(newf)
        go(copy.deepcopy(valves), v, min, f, [])
        #go(copy.deepcopy(valves), v, min, path + v + "-", [])
    for _ in range(min, 30):
        flow.append(flow[-1])
    x = sum(flow)
    if x>=1651:
        print(x)
    return flow
    



go(valves, "AA", 0, [0], [])
