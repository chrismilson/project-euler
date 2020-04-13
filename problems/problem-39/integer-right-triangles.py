""" Chris Milson April 2020
Problem 39

If p is the perimeter of a right angle triangle with integral length sides,
{a,b,c}, there are exactly three solutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p ≤ 1000, is the number of solutions maximised?

## Solution

We can generate all pythagorean triples a^2 + b^2 = c^2 uniquely as a function
of three integers; k, m, and n with Euclid's formula:

```
a = k * (m^2 - n^2), b = k * (2mn), c = k * (m^2 + n^2)
where m > n, m and n are coprime and not both odd.
```

Answer : 840
"""

def gcd(a, b):
  while b > 0:
    a, b = b, a % b
  return a

def countSolutions(upperBound):
  count = {}

  # perimeter is increasing with m, and n.
  def perimeter(m, n):
    return 2 * m * (m + n)

  n = 1
  while perimeter(2, n) < upperBound:
    m = n + 1
    while perimeter(m, n) < upperBound:
      if gcd(m, n) == 1 and m % 2 != n % 2:
        p = perimeter(m, n)
        s = p
        while s < upperBound:
          if s in count: count[s] += 1
          else: count[s] = 1
          s += p
      m += 1
    n += 1

  return count

count = countSolutions(1000)
maxSoFar = 0
culprit = 0
for solution in count:
  if count[solution] > maxSoFar:
    maxSoFar = count[solution]
    culprit = solution

print(culprit, maxSoFar)