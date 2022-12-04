import string

with open('./inp/03.txt') as f:
    inp = [line.rstrip() for line in f.readlines()]

get_prio = lambda s: ord(s) - 96 if s in string.ascii_lowercase else ord(s) - 38

# Part A
_sum = 0
for i in inp:
    same = set(i[:len(i) // 2]).intersection(set(i[len(i) // 2:]))
    for s in same:
        _sum += get_prio(s)

print(_sum)

# Part B
_sum = 0
for i in range(0, len(inp), 3):
    same = set(inp[i]).intersection(set(inp[i+1])).intersection(set(inp[i+2]))
    _sum += get_prio(min(same))

print(_sum)
