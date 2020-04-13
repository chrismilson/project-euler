""" Chris Milson April 2020
Problem 38

Take the number 192 and multiply it by each of 1, 2, and 3:

192 × 1 = 192 192 × 2 = 384 192 × 3 = 576 By concatenating each product we get
the 1 to 9 pandigital, 192384576. We will call 192384576 the concatenated
product of 192 and (1,2,3)

The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and
5, giving the pandigital, 918273645, which is the concatenated product of 9 and
(1,2,3,4,5).

What is the largest 1 to 9 pandigital 9-digit number that can be formed as the
concatenated product of an integer with (1,2, ... , n) where n > 1?

Answer : 932718654
"""
import math
from pprint import pprint

def isPandigital(n):
  if 123456789 > n or n > 987654321: return False
  seen = set()
  while n > 0:
    digit = n % 10
    n //= 10
    if digit == 0 or digit in seen: return False
    seen.add(digit)
  return True

def concatenateNums(*nums):
  result = 0
  for num in nums:
    result *= 10 ** math.floor(math.log10(num) + 1)
    result += num
  return result

def pandigitalProduct(n):
  conc = concatenateNums(n, 2 * n)
  i = 3
  while conc < 123456789:
    conc = concatenateNums(conc, n * i)
    i += 1
  return conc if isPandigital(conc) else None

def findPandigitalProducts():
  # The concatenation must be at least twict the length of the number, so 10000 is
  # a good upper bound
  special = {}
  for i in range(1, 10000):
    p = pandigitalProduct(i)
    if p: special[i] = p
    
  return special

special = findPandigitalProducts()
print('The pandigital products (and their generators) are:')
pprint(special)
print('The maximum product is', max(special.values()), end='.\n')
