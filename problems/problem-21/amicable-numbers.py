""" Chris Milson April 2020
Problem 21

Let d(n) be defined as the sum of proper divisors of n (numbers less than n
which divide evenly into n). If d(a) = b and d(b) = a, where a != b, then a and
b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55
and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and
142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.

Answer : 31626
"""
import math

def d(n):
  """
  returns the sum of the proper divisors of a number n.
  """
  rt = math.sqrt(n)
  i = 2
  result = 1
  while i <= rt:
    if n % i == 0:
      result += i
      result += n / i
    i += 1
  return result

def isAmicable(n):
  dual = d(n)
  if dual == n:
    # perfect numbers are not amicable
    return False 
  return d(dual) == n

def sumAmicables(upperBound):
  result = 0
  for i in range(2, upperBound):
    if isAmicable(i):
      result += i
  return result

print(sumAmicables(10000))