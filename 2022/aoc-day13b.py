import json
import copy

index = 0
ordered = [[[2]], [[6]]]

def compare(left, right):
#    print("will compare", left, right)
    if type(left) is int and type(right) is int:
        if left < right:
#            print("both int, true")
            return True
        elif left > right:
#            print("both int, false")
            return False
        else:
            return
    else:
        if type(left) is int:
            left = [left]
        if type(right) is int:
            right = [right]
        if (not left) and (not right):
            return
        if not left:
            return True
        if not right:
            return False
        l = left.pop(0)
        r = right.pop(0)
        res = compare(l, r)
        if res != None:
            return res
        else:
            return compare(left, right)

    

with open('aoc-day13-input.txt') as f:
    for new_packet in f.read().strip().splitlines():
        try:
            np = json.loads(new_packet)
        except:
            continue
        done = False
        index = 0
        for p in ordered:
            if compare(copy.deepcopy(np), copy.deepcopy(p)):
                ordered.insert(index, np)
                done = True
                break
            index += 1
        if not done:
            ordered.insert(index, np)
for _ in ordered:
    print(_)
            
print((ordered.index([[2]])+1) * (ordered.index([[6]])+1))