from searches import astar, bfs
from aoc_utils import Grid2d, Vector2

with open('./inp/12.txt') as f:
    map = Grid2d(None, [line.rstrip() for line in f.readlines()])

DIRECTIONS = [Vector2(1, 0), Vector2(0, 1), Vector2(-1, 0), Vector2(0, -1)]

start = [k for k in map.keys() if map[k] == 'S'][0]
map[start] = 'a'

end = [k for k in map.keys() if map[k] == 'E'][0]
map[end] = 'z'

# Part A
res = astar(
    start = start,
    is_goal_fn = lambda n: n == end,
    heuristic_fn = lambda n: n.manhattan_distance(end),
    cost_fn = lambda n, m: 1,
    get_neighbors_fn = lambda n: [n + d for d in DIRECTIONS if n + d in map and ord(map[n + d]) - ord(map[n]) <= 1],
    get_key_fn = lambda n: n
)
print(res.cost)

# Part B
print(min(i for i in [astar(
    start = p,
    is_goal_fn = lambda n: n == end,
    heuristic_fn = lambda n: n.manhattan_distance(end),
    cost_fn = lambda n, m: 1,
    get_neighbors_fn = lambda n: [n + d for d in DIRECTIONS if n + d in map and ord(map[n + d]) - ord(map[n]) <= 1],
    get_key_fn = lambda n: n
).cost for p in [k for k in map.keys() if map[k] == 'a']] if i is not None))