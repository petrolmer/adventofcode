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

def calcSize(node: TreeNode):
    if node.children:
        node_size = 0
        for child in node.children.values():
            s = calcSize(child)
            node_size += s
        node.size = node_size
    return node.size

calcSize(root)

task1size = 0

def task1(node: TreeNode):
    global task1size
    if node.children:
        if node.size <= 100000:
            task1size += node.size
        for child in node.children.values():
            task1(child)

task1(root)
print(task1size)
