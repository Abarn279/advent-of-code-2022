with open('./inp/04.txt') as f:
    inp = [line.rstrip().split(',') for line in f.readlines()]

# Part A
count = 0
for pair in inp:
    pair = list(sorted(map(lambda p: tuple(map(int, p.split('-'))), pair)))
    if pair[0][0] <= pair[1][0] and pair[0][1] >= pair[1][1] or pair[1][0] <= pair[0][0] and pair[1][1] >= pair[0][1]: count += 1

print(count)

# Part B (sorry, not optimized)
count = 0
for pair in inp:
    pair = list(sorted(map(lambda p: tuple(map(int, p.split('-'))), pair)))
    if len(set(range(pair[0][0], pair[0][1] + 1)).intersection(set(range(pair[1][0], pair[1][1] + 1)))): count += 1

print(count)