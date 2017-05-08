#!/bin/bash
echo '
Starting in the top left corner of a 2×2 grid, and only being able to
move to the right and down, there are exactly 6 routes to the bottom right
corner.
How many such routes are there through a 20 x 20 grid?

I realised that as we are only allowed to go down and right, we will need 2n
moves to get through an n by n grid. Also, we must go right exactly n times,
but once we have chosen the moves that will go right, the down moves are
completely determined.
So all that remains to be calculated is the number of ways to choose n objects
from 2n objects. Which is well defined, since we know m choose k is
m!/((m - k)!k!).

Since 2 * 20 = 40 and 40 choose 20 is 137846528820, this must be the number of
ways.
'
