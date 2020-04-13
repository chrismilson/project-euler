""" Chris Milson April 2020
Problem 34

145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of their
digits.

Note: as 1! = 1 and 2! = 2 are not sums they are not included.

## Solution

Similarly to problem 30, we can find an upper bound for these numbers. Let F(n)
be the factorial sum of a number n, consider the function u(n) = log10(n) * 9! U
will be an upper bound for F for all n, so if N is the first n such that n >
U(n), there is no possibility that F(n) = n for any n >= N.

We can find this bound quickly, and then exhaustively search the remaining
numbers to find all of these numbers.

Answer : 40730
"""
from functools import lru_cache
import math

def getDigits(n):
  result = []
  while n > 0:
    result.append(n % 10)
    n //= 10
  return result

@lru_cache(maxsize=None)
def factorial(n):
  if n == 0: return 1
  return n * factorial(n - 1)

def digitFactorialSum(n):
  return sum(map(factorial, getDigits(n)))

def findUpperBound():
  def u(n):
    numDigits = math.floor(math.log10(n) + 1)
    return numDigits * factorial(9)
  candidate = factorial(9)
  while candidate <= u(candidate): candidate *= 2
  return candidate

def curiousNumbers():
  result = []
  for i in range(3, findUpperBound()):
    if i == digitFactorialSum(i):
      result.append(i)
  return result

print(sum(curiousNumbers()))