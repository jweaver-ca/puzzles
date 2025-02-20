# Seasons Puzzle

Came across this one on reddit.

```
  X
 XXX
XXXXX
 XXX
  X
```

For the thirteen letters `(a e g I m m n p r s t u w)`, place
them in the shape in the pic so that you can trace the name
of each season (summer autumn winter spring) by moving one
square at a time. You can move diagonally in addition to
vertically or diagonally.

## Solution

This was a tough one. I tried to solve just scribbling about in a text
editor but after 15 minutes or so figured maybe it was better to spend
energy thinking letting a computer solve it. 

### Version 1

`season-v1.py`

This is an ugly brute force but it did work after running for an hour+.
I'm not sure how long it really took.  The first million iterations took
about 5 seconds and there 6,227,020,800 total permutations of 13 letters.
This predicts approx 520 min to get through them all given that those first
million were a fair representation of the overall average processing time
for each iteration.

I could have cut the iterations in half by removing the copies where 'M'
was in the same two positions, but I didn't!

To check if the iteration is a solution, I need to make sure that all
rules defined by `adjacents` were satisfied.  `adjacents` was made by going
through each letter and looking at the season names to see all the letters
that appear beside it. e.g. for 'u': in 'summer' we need 's' and 'm' beside it.
In 'autumn', we need 'a', 't', and 'm'.  So the 'u' line in `adjacents` looks
like:

```
    'U': [ 'S', 'M', 'A', 'T' ]
```

Any perumation where all required letters are adjacent for every letter is a
complete solution
