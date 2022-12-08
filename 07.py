from collections import deque

with open('./inp/07.txt') as f:
    inp = [line.rstrip() for line in f.readlines()]

class Node:
    def __init__(self, name, size=0):
        self.name = name
        self.size = size
        self.children = []
        self.parent = None

    def add_child(self, node):
        self.children.append(node)
        node.parent = self

    def search(self, name):
        for c in self.children:
            if c.name == name: return c
        raise Exception()

    def get_subd_under_10k(self):
        candidates = []

        for c in self.children:
            if c.size != 0: continue
            if c.get_size() < 100000:
                candidates.append(c)

            candidates += c.get_subd_under_10k()
        
        return candidates
            
    def get_size(self):
        _sm = self.size

        for c in self.children:
            _sm += c.get_size()

        return _sm

    def get_all_subd_with_size(self):
        subd = {}
        for c in self.children:
            if c.size != 0: continue
            subd[c.name] = c.get_size()

            subd.update(c.get_all_subd_with_size())
        return subd
            

    def __repr__(self):
        if self.size == 0: 
            return f'dir {self.name}'
        else:
            return f'{self.size} {self.name}'

###### 
# Part A
######

# Set up filesystem, hold onto root as we'll use fs to traverse tree
fs = Node('/')
root = fs

# Set up input
output = deque(inp)
output.popleft()

while len(output) > 0:
    command = output.popleft()

    # list
    if command.startswith('$ ls'):
        while len(output) and not output[0].startswith('$'):
            listcommand = output.popleft()

            size, name = listcommand.split(' ')
            if size == 'dir':
                fs.add_child(Node(name))
            else:
                fs.add_child(Node(name, int(size)))

    # cd
    elif command.startswith("$ cd"):
        subc = command.split(' ')[2]

        if subc == '..':
            fs = fs.parent
        
        elif subc == '/':
            fs = root

        else:
            fs = fs.search(subc)

print(sum(i.get_size() for i in root.get_subd_under_10k()))

###### 
# Part B
######
all_subd = root.get_all_subd_with_size()
size_values = list(all_subd.values())
used_space = root.get_size()
unused_space = 70000000 - used_space
needed_free_up = 30000000 - unused_space

space_after = [s for s in size_values if s - needed_free_up > 0]
print(min(space_after))

