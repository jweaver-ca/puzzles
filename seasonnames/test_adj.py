
coords = [ (2,0), 
    (1,1), (2,1), (3,1), 
    (0,2), (1,2), (2,2), (3,2), (4,2),
    (1,3), (2,3), (3,3),
    (2,4) ]

#adjacents = [ ('M', 'M'), ('U','M'), 
def is_adjacent(c1, c2):
    return abs(c1[0]-c2[0]) <= 1 and abs(c1[1]-c2[1]) <= 1

for i in range(len(coords)):
    c1 = coords[i]
    for j in range(i+1, len(coords)):
        c2 = coords[j]
        print (f"{c1} {c2} : {is_adjacent(c1,c2)}")

adjacents = {
    'M': [ 'M', 'U', 'N' ],
    'A': [ 'U'],
    'G': [ 'N' ],
    'P': [ 'S', 'R' ],
    'W': [ 'I'],
    'E': [ 'M', 'T', 'R' ],
    'I': [ 'W', 'N', 'R' ],
    'S': [ 'P', 'U'],
    'T': [ 'U', 'N', 'E' ],
    'N': [ 'M', 'I', 'T', 'G'],
    'R': [ 'E', 'P', 'I' ],
    'U': [ 'S', 'M', 'A', 'T' ]
    }

tot = 0
for p in itertools.permutations(letters):
    tot += 1
    lkuPos = dict()
    blnOk = True
    for i in range(len(letters)):
        lkuPos[p[i]] = i
    for i in range(len(letters)):
        c1 = coords[i]
        adj_key = letters[i]
        if adj_key[0] == 'M':
            adj_key = 'M'

        for adj in adjacents[adj_key]:
            if adj == 'M':
                if not (is_adjacent(c1, coords[lkuPos['M1']]) or is_adjacent(c1, coords[lkuPos['M2']])):
                    blnOk = False
                    break
            else:
                c2 = coords[lkuPos[adj]]
                if not is_adjacent(c1, c2):
                    blnOk = False
                    #print (f"{p}\nRejected cuz {letters[i]} is not adjacent to {adj}")
                    break
        if not blnOk:
            break
    if blnOk:
        break
print (p)
