from aoc_utils import Grid2d, Vector2

with open('./inp/14.txt') as f:
    scan = [line.rstrip() for line in f.readlines()]

DIRECTIONS = {"DOWN": Vector2(0, 1), "DOWNLEFT": Vector2(-1, 1), "DOWNRIGHT": Vector2(1, 1)}

grid = Grid2d('.')

# Setup walls
for structure in scan:
    structure = structure.split(' -> ')
    for point_i in range(len(structure) - 1):
        # get p1 and p2 as vectors and the distance between them
        p1, p2 = structure[point_i], structure[point_i + 1]
        p1, p2 = Vector2(*map(int, p1.split(','))), Vector2(*map(int, p2.split(',')))
        d = p2 - p1

        # Start filling in everything between p1 and p2
        grid[p1] = '#'
        while p1 != p2:
            p1 = p1 + d.clamped(-1, 1)
            grid[p1] = '#'

source = Vector2(500, 0)
grid[source] = '+'
sandchar = 'o'

###########
# Part A
###########

# produce sand for infinity!
is_abyss = False
while True:
    new_sand_pos = Vector2(source.x, source.y)

    times_down = 0
    # Sand moves til it's not at rest!
    while True:

        down = new_sand_pos + DIRECTIONS["DOWN"]
        if grid[down] == '.': 
            new_sand_pos = down
            times_down += 1
            if times_down == 50: 
                is_abyss = True
                break
            continue

        times_down = 0

        downleft = new_sand_pos + DIRECTIONS["DOWNLEFT"]
        if grid[downleft] == '.': 
            new_sand_pos = downleft
            continue

        downright = new_sand_pos + DIRECTIONS["DOWNRIGHT"]
        if grid[downright] == '.': 
            new_sand_pos = downright
            continue
    
        grid[new_sand_pos] = sandchar
        break

    if is_abyss: break

grid.recompute_bounds()
print(grid)
print(sum(1 for i in grid.values() if i == sandchar))

###########
# Part B
###########

# produce sand for infinity!
floor = max(v.y for v in grid.keys()) + 2
while True:
    new_sand_pos = Vector2(source.x, source.y)

    # Sand moves til it's not at rest!
    while True:

        down = new_sand_pos + DIRECTIONS["DOWN"]

        if down.y != floor:

            if grid[down] == '.': 
                new_sand_pos = down
                continue

            times_down = 0

            downleft = new_sand_pos + DIRECTIONS["DOWNLEFT"]
            if grid[downleft] == '.': 
                new_sand_pos = downleft
                continue

            downright = new_sand_pos + DIRECTIONS["DOWNRIGHT"]
            if grid[downright] == '.': 
                new_sand_pos = downright
                continue
    
        grid[new_sand_pos] = sandchar
        break

    if new_sand_pos == source:
        break


grid.recompute_bounds()
print(grid)
print(sum(1 for i in grid.values() if i == sandchar))