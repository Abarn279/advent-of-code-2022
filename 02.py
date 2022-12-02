with open('./inp/02.txt') as f:
    guide = [i.split(' ') for i in [j.rstrip() for j in f.readlines()]]

points = { 'X': 1, 'Y': 2, 'Z': 3 }
im_beaten_by = { 'X': 'B', 'Y': 'C', 'Z': 'A' }
theyre_beaten_by = { 'A': 'Y', 'B': 'Z', 'C': 'X' }
draws = { 'X': 'A', 'Y': 'B', 'Z': 'C', 'A': 'X', 'B': 'Y', 'C': 'Z' }

# Part A
score = 0
for g in guide:
    theirs, mine = g[0], g[1]
    score += points[mine]

    if draws[mine] == theirs:
        score += 3
    elif im_beaten_by[mine] != theirs:
        score += 6
    
print(score)

# Part B
score = 0
for g in guide:
    theirs, needed_outcome = g[0], g[1]

    if needed_outcome == 'Y': score += 3 
    if needed_outcome == 'Z': score += 6

    if needed_outcome == 'X':
        [i_play] = [i for i in im_beaten_by if im_beaten_by[i] == theirs]
    elif needed_outcome == 'Y': 
        i_play = draws[theirs]
    elif needed_outcome == 'Z':
        i_play = theyre_beaten_by[theirs]

    score += points[i_play]

print(score)