""" Chris Milson April 2020
Problem 28

Starting with the number 1 and moving to the right in a clockwise direction a 5
by 5 spiral is formed as follows:

```
21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13
```

It can be verified that the sum of the numbers on the diagonals is 101.

What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed
in the same way?

## Solution

We can see that the sum, S, will be

```
S = 1 + sum_{i in {3, 5, 7, ..., n}} (
  i^2 +
  (i^2 - (i - 1)) +
  (i^2 - 2 * (i - 1)) +
  (i^2 - 3 * (i - 1))
)
= 1 + sum_{i in {3, 5, 7, ..., n}} (4i^2 - 6(i - 1))
```

This will calculate in O(n) time in O(1) space.

Alternatively, we can find a closed form for this sum, since it is fairly
simple. Such a form would be:

S = 1 + 4m + (2m(m + 1)(8m + 7) / 3)

Answer : 669171001
"""

def numberSpiralDiagonalSum(sideLength):
  # this should only be done on spirals with odd side length
  assert(sideLength % 2 == 1)
  m = sideLength // 2

  return 1 + 4 * m + 2 * m * (m + 1) * (8 * m + 7) / 3

print(numberSpiralDiagonalSum(12398768976321331234546511))