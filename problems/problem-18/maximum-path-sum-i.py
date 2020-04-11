""" Chris Milson April 2020
Problem 18

By starting at the top of the triangle below and moving to adjacent numbers on
the row below, the maximum total from top to bottom is 23.

```
     [3]
   [7]  4
  2  [4]  6
8   5  [9]  3
```

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom of the triangle below:

*omitted*

NOTE: As there are only 16384 routes, it is possible to solve this problem by
trying every route. However, Problem 67, is the same challenge with a triangle
containing one-hundred rows; it cannot be solved by brute force, and requires a
clever method!

Answer : 1074
"""
from triangle import triangle

def maxPathSum(triangle):
  # At each loop it should hold the maximum sum from the row above to the top.
  dp = [0, 0]

  for row in triangle:
    # the first and last element on each row has no choice
    nextdp = [0]
    for i, value in enumerate(row):
      nextdp.append(value + max(dp[i], dp[i + 1]))
    nextdp.append(0)
    dp = nextdp
  return max(dp)

print(maxPathSum(triangle))