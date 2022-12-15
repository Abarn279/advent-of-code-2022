from aoc_utils import Vector2

with open('./inp/09.txt') as f:
    inp = [line.rstrip() for line in f.readlines()]

DIRECTIONS = {'R': Vector2(1, 0), 'U': Vector2(0, 1), 'L': Vector2(-1, 0), 'D': Vector2(0, -1)}

def get_number_visited(segments):
    tvisited = set()

    for command in inp:
        # direction and number of steps
        direction, magnitude = command.split(' ')

        # for each step collected from inp line...
        for step in range(int(magnitude)):

            # move Head (H), located at segments[0]
            segments[0] = segments[0] + DIRECTIONS[direction]

            # for each tail segment behind H...
            for i in range(1, len(segments)):

                # h is current head, t is the one right behind it. they will act like their own heads and tails. 
                h, t = segments[i-1], segments[i]

                # do the calculation to see if T needs to be moved. 
                if abs(h.x - t.x) > 1 or abs(h.y - t.y) > 1:
                    distance = (h - t).clamped(-1, 1)
                    segments[i] = segments[i] + distance

            # once all have been moved, add the final tail to the visited set
            tvisited.add(segments[-1])

    return len(tvisited)

# Part A
print(get_number_visited([Vector2(0, 0), Vector2(0, 0)]))

# Part B
print(get_number_visited([Vector2(0, 0) for i in range(10)]))