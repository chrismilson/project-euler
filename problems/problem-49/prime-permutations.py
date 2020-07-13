""" Chris Milson July 2020
Problem 49

Prime Permutations

The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases
by 3330, is unusual in two ways: (i) each of the three terms are prime, and,
(ii) each of the 4-digit numbers are permutations of one another.

There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes,
exhibiting this property, but there is one other 4-digit increasing sequence.

What 12-digit number do you form by concatenating the three terms in this
sequence?

## Solution

We can do a search through the possible arithmetic sequences. Since the sequency
is arithmetic, the first two values will define the third value. They must all
be prime, so that cuts out a lot of checking we have to do, and after that we
can check that they are palindromes of each other.

Answer : 296962999629
"""
from collections import Counter

digits = 4

primes = [2, 3, 5]
def nextPrime():
  candidate = primes[-1] + 2
  while True:
    for prime in primes:
      if prime * prime > candidate:
        primes.append(candidate)
        return
      if candidate % prime == 0:
        break
    candidate += 2

while primes[-1] < 10 ** (digits / 2):
  nextPrime()

def isPrime(candidate):
  for prime in primes:
    if prime * prime > candidate:
      return True
    if candidate % prime == 0:
      return False

def arePalindromes(*args):
  target = Counter(str(args[0]))
  for other in args[1:]:
    if Counter(str(other)) != target:
      return False
  return True

for a in filter(isPrime, range(10 ** (digits - 1), 10 ** digits)):
  for b in filter(isPrime, range(a + 1, (10 ** digits + a) // 2)):
    c = 2 * b - a
    if isPrime(c) and arePalindromes(a, b, c):
      print(a, b, c)
