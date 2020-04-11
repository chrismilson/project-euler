""" Chris Milson April 2020
Problem 67

By starting at the top of the triangle below and moving to adjacent numbers on
the row below, the maximum total from top to bottom is 23.

```
     [3]
   [7]  4
  2  [4]  6
8   5  [9]  3
```

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom in triangle.txt (in string form in an
adjacent file), a 15K text file containing a triangle with one-hundred
rows.

Answer : 7273
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