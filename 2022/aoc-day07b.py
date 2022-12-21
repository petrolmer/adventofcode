class TreeNode:
    def __init__(self, name, size = 0, parent = None):
        self.name = name
        self.size = size
        self.children = {}
        self.parent = parent

root = TreeNode("/")
with open('aoc-day07-input.txt') as f:
    for line in f:
        l = line.strip()
        if l[0] == '$':
            command = l[2:]
            if command[0:2] == "cd":
                dir = command[3:]
                if dir == "..":
                    curr_dir = curr_dir.parent
                elif dir == "/":
                    curr_dir = root
                else:
                    curr_dir = curr_dir.children[dir]
        else:
            (first, name) = l.split()
            if first == "dir":
                size = 0 
            else:
                size = int(first)
            if curr_dir.name != "/":
                child_name = curr_dir.name + "/" + name
            else:
                child_name = "/" + name
            curr_dir.children[name] = TreeNode(child_name, size, curr_dir)

def printTree(node: TreeNode):
    print(node.name, node.size)
    for child in node.children:
        printTree(node.children[child])

def calcSize(node: TreeNode):
    if node.children:
        node_size = 0
        for child in node.children:
            s = calcSize(node.children[child])
            node_size += s
        node.size = node_size
    return node.size

calcSize(root)
printTree(root)

task2size = root.size
size_needed = 30000000 - (70000000 - root.size)

def task2(node: TreeNode):
    global task2size
    if node.children:
        if node.size >= size_needed:
            task2size = min(task2size, node.size)
            for child in node.children.values():
                task2(child)

task2(root)
print(task2size)