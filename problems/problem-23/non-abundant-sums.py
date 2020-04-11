""" Chris Milson April 2020
Problem 23

A perfect number is a number for which the sum of its proper divisors is exactly
equal to the number. For example, the sum of the proper divisors of 28 would be
1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n
and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest
number that can be written as the sum of two abundant numbers is 24. By
mathematical analysis, it can be shown that all integers greater than 28123 can
be written as the sum of two abundant numbers. However, this upper limit cannot
be reduced any further by analysis even though it is known that the greatest
number that cannot be expressed as the sum of two abundant numbers is less than
this limit.

Find the sum of all the positive integers which cannot be written as the sum of
two abundant numbers.

Answer : 4179871
"""
import math

def d(n):
  """
  returns the sum of the proper divisors of a number n.
  """
  rt = math.sqrt(n)
  i = 2
  result = 1
  while i < rt:
    if n % i == 0:
      result += i
      result += n // i
    i += 1

  # i == rt implies that n is a square number
  if i == rt and n % i == 0:
    result += i
  return result

def getAbundantNumbers(upperLimit):
  """
  Returns a list of all abundant numbers less than an upper limit
  """
  result = []
  for i in range(1, upperLimit):
    if d(i) > i:
      result.append(i)
  return result
abundantNumbersList = list(getAbundantNumbers(28123))
abundantNumbersSet = set(abundantNumbersList)

def canBeWritten(n):
  """
  Returns true iff the number n can be written as the sum of two abundant
  numbers.
  """
  for a in abundantNumbersList:
    if a >= n: break
    if (n - a) in abundantNumbersSet:
      return True
  return False

def sumUnwriteable():
  return sum(0 if canBeWritten(i) else i for i in range(28123))

print(sumUnwriteable())