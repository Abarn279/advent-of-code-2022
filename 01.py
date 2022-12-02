with open('./inp/01.txt') as f:
    calorieSums = [sum(map(int, i.split('\n'))) for i in f.read().split('\n\n')]

# Part A
print(max(calorieSums))

# Part B
print(sum(sorted(calorieSums)[-3:]))