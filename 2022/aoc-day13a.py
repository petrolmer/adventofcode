import json

index = 0
correct = []

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
    index = 0
    for group in f.read().strip().split("\n\n"):
        index += 1
        pair = group.splitlines()
        if compare(json.loads(pair[0]), json.loads(pair[1])):
            correct.append(index)

print(sum(correct))
            
