from aoc_utils import Vector2

with open('./inp/09.txt') as f:
    inp = [line.rstrip() for line in f.readlines()]

DIRECTIONS = {'R': Vector2(1, 0), 'U': Vector2(0, 1), 'L': Vector2(-1, 0), 'D': Vector2(0, -1)}

h = Vector2(0, 0)
t = Vector2(0, 0)

tvisited = set()

for command in inp:
    direction, magnitude = command.split(' ')

    for step in range(int(magnitude)):

        # update H
        h = h + DIRECTIONS[direction]

        if abs(h.x - t.x) > 1 or abs(h.y - t.y) > 1:
            distance = (h - t).clamped(-1, 1)
            t = t + distance

        tvisited.add(t)

        # for y in reversed(range(6)):
        #     for x in range(6):
        #         if Vector2(x, y) == h: char = 'H'
        #         elif Vector2(x, y) == t: char = 'T'
        #         elif Vector2(x, y) == Vector2(0, 0): char = 's'
        #         else: char = '.'
        #         print(char, end="")
        #     print()
        # print()

# for y in reversed(range(6)):
#     for x in range(6):
#         print('#' if Vector2(x, y) in tvisited else '.', end="")
#     print()


print(len(tvisited))