from aoc_utils import Vector2, Grid2d

with open('./inp/08.txt') as f:
    grid = Grid2d(None, [list(map(int, line.rstrip())) for line in f.readlines()])

DIRECTIONS = [Vector2(1, 0), Vector2(0, 1), Vector2(-1, 0), Vector2(0, -1)]

def is_visible(grid, coord):
    for d in DIRECTIONS:

        # get the tree in this direction, begin listing all of the tree coordinates in this direction until we hit the edge
        new_coord = coord + d
        trees_in_way = []

        while new_coord in grid:
            trees_in_way.append(new_coord)
            new_coord = new_coord + d
        
        if all(grid[tree] < grid[coord] for tree in trees_in_way):
            return True
    return False

def get_viewing_score(grid, coord):
    score = 1
    height = grid[coord]

    for d in DIRECTIONS:
        viewing_distance = 0
        new_coord = coord + d

        while new_coord in grid:
            viewing_distance += 1
            if grid[new_coord] >= height:
                break
            new_coord = new_coord + d
        
        score *= viewing_distance
    
    return score

# Part A
print(sum(1 for t in grid.keys() if is_visible(grid, t)))

# Part B
print(max(get_viewing_score(grid, t) for t in grid.keys()))