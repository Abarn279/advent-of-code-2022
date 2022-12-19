from re import match
from aoc_utils import Vector2, Grid2d

with open('./inp/15.txt') as f:
    scan = [line.rstrip() for line in f.readlines()]

class Sensor:
    def __init__(self, pos, beaconPos):
        self.pos = pos
        self.beaconPos = beaconPos
        self.range = self.pos.manhattan_distance(self.beaconPos)

    def is_possible_for_beacon(self, newBeaconPos):
        return self.pos.manhattan_distance(newBeaconPos) > self.range

    def get_bounding_coordinates(self):
        coords = set()
        distance = self.range + 1
        top = self.pos + Vector2(0, -(distance))
        right = self.pos + Vector2(distance, 0)
        bottom = self.pos + Vector2(0, distance)
        left = self.pos + Vector2(-distance, 0)
        points = [top, right, bottom, left]

        for p in range(len(points) - 1):
            p1 = points[p]
            p2 = points[p + 1]
            d = (p2 - p1).clamped(-1, 1)

            coords.add(p1)
            while p1 != p2:
                p1 = p1 + d
                coords.add(p1)
            coords.add(p2)
        
        return coords

    def __repr__(self):
        return f'Sensor at ({self.pos.x}, {self.pos.y}) tied to beacon at ({self.beaconPos.x}, {self.beaconPos.y})'

# Grab beacons and sensor locations
sensors = []
beacons = []
grid = Grid2d('.')
for sensor_string in scan:
    sx, sy, bx, by = match(r'Sensor at x=(\d+), y=(\d+): closest beacon is at x=(-*\d+), y=(-*\d+)', sensor_string).groups()
    sensors.append(Sensor(Vector2(int(sx), int(sy)), Vector2(int(bx), int(by))))
    beacons.append(Vector2(int(bx), int(by)))

for s in sensors:
    grid[s.pos] = 'S'

for b in beacons:
    grid[b] = 'B'


# Part A
# _sm = 0
# row_to_check = 2000000
# minx, maxx = [i.x for i in grid.get_bounds()]

# for x in range(minx - 1000000, maxx + 1000000):
#     if grid[Vector2(x, row_to_check)] == '.' and not all(s.is_possible_for_beacon(Vector2(x, row_to_check)) for s in sensors):
#         _sm += 1

# print(_sm)

# Part B
all_bounding_coordinates = set()
for s in sensors:
    all_bounding_coordinates.update(s.get_bounding_coordinates())

overall_bounds = 4000000
for abc in all_bounding_coordinates:
    if abc.x < 0 or abc.y < 0 or abc.x > overall_bounds or abc.y > overall_bounds: continue
    if grid[Vector2(abc.x, abc.y)] == '.' and all(s.is_possible_for_beacon(Vector2(abc.x, abc.y)) for s in sensors):
        print(abc.x * 4000000 + abc.y)
        break
