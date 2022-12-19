from functools import cmp_to_key

with open('./inp/13.txt') as f:
    pairStrings = [i.split('\n') for i in f.read().split('\n\n')]

def zip_with_none(a, b):
    '''
    using this instead of built in zip() so it can include Nones when one list is longer than another
    '''
    maxlen = max(len(a), len(b))
    zipped = []
    for i in range(maxlen):
        zipped.append((a[i] if i < len(a) else None, b[i] if i < len(b) else None))
    return zipped

def is_ordered(a, b):
    '''
    Recurisve function to see if two lists are ordered
    '''
    if (isinstance(a, int) or a is None) and (isinstance(b, int) or b is None):
        if a is None: return True
        if b is None: return False
        return True if a <= b else False
    
    if isinstance(a, list) and isinstance(b, list):
        if not len(b): return False 
        if not len(a): return True

        for pair in zip_with_none(a, b):
            if pair[0] == pair[1]: continue
            return is_ordered(pair[0], pair[1])

    else:
        if isinstance(a, int): return is_ordered([a], b)
        elif isinstance(b, int): return is_ordered(a, [b])

    return True

# Part A 
_sm = 0
for i in range(len(pairStrings)):
    pair = pairStrings[i]
    a = eval(pair[0])
    b = eval(pair[1])
    if is_ordered(a, b):
        _sm += i + 1
print(_sm)

# Part B 
all_packets = []
for i in range(len(pairStrings)):
    pair = pairStrings[i]
    a = eval(pair[0])
    b = eval(pair[1])
    all_packets.append(a);all_packets.append(b)

# Add divider packets per rules
all_packets.append([[2]])
all_packets.append([[6]])

# Custom cort comparison func
def cmpr(a, b):
    val = is_ordered(a, b)
    if val == True: return -1
    if val == False: return 1
    if val == None: return 0

# Sort with custom comparison function, find the divider packets, multiply
srted = list(sorted(all_packets, key=cmp_to_key(cmpr)))
first, second = srted.index([[2]]) + 1, srted.index([[6]]) + 1
print(first * second)