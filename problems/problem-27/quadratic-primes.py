# -*- coding: utf-8 -*-
""" Chris Milson April 2020
Problem 27

Euler discovered the remarkable quadratic formula:

```
n^2 + n + 41
```

It turns out that the formula will produce 40 primes for the consecutive integer
values 0 <= n <= 39. However, when n = 40, 40^2 + 40 + 41 = 40(40+1) + 41 is
divisible by 41, and certainly when n = 41, 41^2 + 41 + 41 is clearly divisible
by 41.

The incredible formula n^2 − 79n + 1601 was discovered, which produces 80 primes
for the consecutive values 0 <= n <= 79. The product of the coefficients, -79
and 1601, is -126479.

Considering quadratics of the form:

```
n^2 + an + b, where |a| < 1000 and |b| <= 1000

where |n| is the modulus/absolute value of n e.g. |11| = 11 and |−4| = 4
```

Find the product of the coefficients, a and b, for the quadratic expression that
produces the maximum number of primes for consecutive values of n, starting with
n = 0.

Answer : -59231
"""

primes = [2, 3, 5]
primeSet = set(primes)
def nextPrime():
  """
  Calculates the next prime and puts it on the end of the primes array.
  """
  candidate = primes[-1] + 2

  while True:
    for task in primes:
      if task * task > candidate:
        primes.append(candidate)
        primeSet.add(candidate)
        return candidate
      if candidate % task == 0:
        break
    candidate += 2

def quadraticPrimes(a, b):
  """
  Calculates the maximum N such that f(n) = n^2 + an + b will produce primes for
  all n less than or equal to N.

  This will be bounded by the smallest factor in b, since if b = xy for some x
  and y, then x^2y^2 + axy + xy is divisible by x. Thus, if b is NOT prime, then
  this will be bounded above by sqrt(b) at best.

  Also, b must be non-negative, since if b < 0, then f(0) = b < 0 which is not
  prime.

  Now, since b is prime, it is odd (once it's large enough), then f(n) will be
  even if n^2 + an is odd. Thus a should be odd.
  """
  candidates = [i ** 2 + i * a + b for i in range(b)]
  for i, candidate in enumerate(candidates):
    while candidate > primes[-1]: nextPrime()
    if candidate not in primeSet: return i - 1
  return len(candidates)


def maxInBounds(A, B):
  while B >= primes[-1]: nextPrime()

  maxSoFar = 0
  culprits = (0, 0)
  for a in range(1 - A, A):
    for b in primes:
      if b > B:
        # this must happen, since we iterated the primes at the beginning
        break
      N = quadraticPrimes(a, b)
      if N > maxSoFar:
        maxSoFar = N
        culprits = (a, b)
  return culprits

a, b = maxInBounds(1000, 1000)
print(a * b)