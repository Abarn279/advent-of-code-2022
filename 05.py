from collections import deque
import re

with open('./inp/05.txt') as f:
    stacksraw, directionsraw = f.read().split('\n\n')
    
def get_stacks(stacksraw):
    stacksraw = stacksraw.split('\n')
    n_stacks = int(stacksraw.pop()[-2])

    stacks = {i: deque() for i in range(1, n_stacks+1)}
        
    for line_i in reversed(range(len(stacksraw))):
        for stack_i in range(n_stacks):
            char = stacksraw[line_i][stack_i*4:stack_i*4 + 4][1]
            
            if not char.isspace(): stacks[stack_i+1].appendleft(char)
    return stacks

# Part A
stacks = get_stacks(stacksraw[:])
for direction in directionsraw.split('\n'):
    [n_to_move, from_stack, to_stack] = map(int, re.match(r'move (\d+) from (\d+) to (\d+)', direction).groups())
    
    for n in range(n_to_move):
        stacks[to_stack].appendleft(stacks[from_stack].popleft())


print("".join(i[0] for i in stacks.values()))

# Part B
stacks = get_stacks(stacksraw[:])
for direction in directionsraw.split('\n'):
    [n_to_move, from_stack, to_stack] = map(int, re.match(r'move (\d+) from (\d+) to (\d+)', direction).groups())
    
    to_add = []
    for n in range(n_to_move):
        to_add.append(stacks[from_stack].popleft())
    
    for a in reversed(to_add):
        stacks[to_stack].appendleft(a)


print("".join(i[0] for i in stacks.values()))