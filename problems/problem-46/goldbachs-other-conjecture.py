""" Chris Milson April 2020
Problem 46

It was proposed by Christian Goldbach that every odd composite number can be
written as the sum of a prime and twice a square.

9 = 7 + 2×1^2
15 = 7 + 2×2^2
21 = 3 + 2×3^2
25 = 7 + 2×3^2
27 = 19 + 2×2^2
33 = 31 + 2×1^2

It turns out that the conjecture was false.

What is the smallest odd composite that cannot be written as the sum of a prime
and twice a square?

## Solution

Since this is a conjecture by a serious mathematician, it probably doesnt have a
nice trick that will help us find the counterexample. Therefore we will just
iterate until we find the counterexample.

Answer : 
"""
import math

primes = [2, 3, 5, 7]
def isSquare(n): return math.sqrt(n) % 1 == 0

def checkGOC(task):
  """
  Checks whether a number follows Goldbachs Other Conjecture.
  That is, it is equal to the sum of a prime and twice a square.
  """
  for prime in primes:
    if isSquare((task - prime) / 2): return True
  return False

found = 0
task = 9
while found < 2 and task < 1000000000:
  # The task may be prime.
  for prime in primes:
    if prime * prime > task:
      # If prime add it to the list.
      primes.append(task)
      break
    if task % prime == 0:
      # If composite check it.
      if not checkGOC(task):
        print(task, 'is divisible by', prime)
        found += 1
      break
  task += 2