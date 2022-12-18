with open('./inp/10.txt') as f:
    inp = [line.rstrip() for line in f.readlines()]

is_intersecting = lambda c: c in [20, 60, 100, 140, 180, 220]

def check_intersection():
    global cycle
    global _sm
    global x
    if is_intersecting(cycle): 
        _sm += x * cycle

def draw_to_crt():
    global x
    global crt
    
    crt_ind = len(crt) % 40
    sprite_inds = ([x - 1, x, x + 1])

    if crt_ind in sprite_inds: crt.append('#')
    else: crt.append('.')

cycle = 1
x = 1
_sm = 0
crt = []

for cmd in inp:
    cycle += 1
    if cmd.startswith("noop"):
        check_intersection()
        draw_to_crt()

    elif cmd.startswith("addx"):
        check_intersection()
        draw_to_crt()

        cycle += 1
        draw_to_crt()
        x += int(cmd.split(' ')[1])

        check_intersection()

# Part A
print(_sm)

# Part B 
while len(crt):
    for i in range(40):
        print(crt[0], end="")
        crt.pop(0)
    print()
    